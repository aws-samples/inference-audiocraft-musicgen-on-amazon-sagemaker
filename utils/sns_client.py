import logging
import time
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns/client/create_topic.html

class SnsClient:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self, sns_client):
        """
        :param sns_client: A Boto3 Amazon SNS client.
        """
        self.sns_client = sns_client


    def create_topic(self, name):
        """
        Creates a notification topic.

        :param name: The name of the topic to create.
        :return: Response from CreateTopic action of type dict.
        """
        try:
            response = self.sns_client.create_topic(Name=name)
            logger.info("Created topic %s with ARN %s.", name, response['TopicArn'])
        except ClientError:
            logger.exception("Couldn't create topic %s.", name)
            raise
        else:
            return response

    
    
    def get_topic_attributes(self, topic_arn):
        """
        Returns all of the properties of a topic. Topic properties returned might differ based on the authorization of the user.

        :return: A dict the with topic attributes.
        """
        try:
            response = self.sns_client.get_topic_attributes(TopicArn = topic_arn)

            logger.info("Got topics.")
        except ClientError:
            logger.exception("Couldn't get topics.")
            raise
        else:
            return response
    

    def delete_topic(self, topic_arn):
        """
        Deletes a topic and all its subscriptions. Deleting a topic might prevent some 
        messages previously sent to the topic from being delivered to subscribers. 
        This action is idempotent, so deleting a topic that does not exist does not result in an error.
        """
        try:
            self.sns_client.delete_topic(TopicArn=topic_arn)

            logger.info("Deleted topic %s.", topic_arn)
        except ClientError:
            logger.exception("Couldn't delete topic %s.", topic_arn)
            raise