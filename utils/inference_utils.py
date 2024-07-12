import os
import uuid
import json


def generate_json(data):
    suffix = str(uuid.uuid1())
    filename = f'payload_{suffix}.json'
    with open(filename, 'w') as fp:
        json.dump(data, fp)
    return filename


def upload_input_json(sm_session, filename):
    return sm_session.upload_data(
        filename,
        bucket=sm_session.default_bucket(),
        key_prefix='musicgen_large/input_payload',
        extra_args={"ContentType": "application/json"},
    )


def delete_file_on_disk(filename):
    if os.path.isfile(filename):
        os.remove(filename)


import urllib, time
from botocore.exceptions import ClientError
import random

def get_output(sm_session, output_location):
    output_url = urllib.parse.urlparse(output_location)
    
    icons = ["🪘","🪇","🎷","🎸","🎺","🎻","🥁", "🪗", "🪕"]
    print("generating music")
    while True:
        try:
            res = sm_session.read_s3_file(bucket=output_url.netloc, key_prefix=output_url.path[1:])
            print("\nMusic is ready!🎉")
            return res
        except ClientError as e:
            if e.response["Error"]["Code"] == "NoSuchKey":
                
                print(random.choice(icons), end = '')
                time.sleep(2)
                continue
            raise
    

import botocore
import boto3
def download_from_s3(url):
    """ex: url = s3://bucketname/prefix1/music.wav"""
    url_parts = url.split("/")  # => ['s3:', '', 'sagemakerbucketname', 'data', ...
    bucket_name = url_parts[2]
    key = os.path.join(*url_parts[3:])
    filename = url_parts[-1]
    if not os.path.exists(filename):
        try:
            # Create an S3 client
            s3 = boto3.resource('s3')
            print('Downloading {} to {}'.format(url, filename))
            s3.Bucket(bucket_name).download_file(key, filename)
            return filename
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print('The object {} does not exist in bucket {}'.format(
                    key, bucket_name))
            else:
                raise


from IPython.display import Audio
import IPython
def play_output_audios(filenames, texts):
    for filename, text in zip(filenames, texts):
        # Create an Audio object
        if not filename:
            continue
        audio = Audio(filename=filename)
        # Display the audio
        print(f"{text}:\n{filename}")
        print()
        display(audio)
        print()