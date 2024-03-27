## Inference Audiocraft Musicgen on Amazon SageMaker

Deploy Audiocraft Musicgen on Amazon SageMaker using SageMaker Endpoints for Async Inference.

AudioCraft consists of three models: MusicGen, AudioGen, and EnCodec. This repo aims to deploy MusicGen models on Amazon SageMaker for Asynchronous inferencing.

## Asynchronous Inference Sequence flow for facebook/musicgen-large on Amazon SageMaker

![alt text](image.png)

## Deployment and inference notebooks

The deployment notebooks used in this repo uses Huggingface as model provider for the musicgen models. The corresponding deployment and inference noteboks for the respective models are tablulated below.

| Huggingace Model ID | Deploy Notebook | Inference Notebook |
| -- | -- | -- |
| facebook/musicgen-large | [Deploy](musicgen-large/deploy-musicgen-large.ipynb) | [Inference](musicgen-large/infer-async.ipynb) |
| facebook/musicgen-small | [Deploy](musicgen-small/deploy-musicgen-small.ipynb) | [Inference](musicgen-small/infer-async.ipynb) |

## References
- [Open sourcing AudioCraft: Generative AI for audio made simple and available to all](https://ai.meta.com/blog/audiocraft-musicgen-audiogen-encodec-generative-ai-audio/)
- https://huggingface.co/facebook/musicgen-large
- https://huggingface.co/docs/transformers/model_doc/musicgen#generation
- https://github.com/facebookresearch/audiocraft/blob/main/README.md
- https://sagemaker.readthedocs.io/en/stable/frameworks/huggingface/sagemaker.huggingface.html#hugging-face-model
- https://sagemaker.readthedocs.io/en/stable/api/inference/predictors.html#sagemaker.predictor.Predictor.predict
- https://github.com/aws/amazon-sagemaker-examples/blob/main/async-inference/Transcription_on_SM_endpoint.ipynb


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## Citation
```
@inproceedings{copet2023simple,
    title={Simple and Controllable Music Generation},
    author={Jade Copet and Felix Kreuk and Itai Gat and Tal Remez and David Kant and Gabriel Synnaeve and Yossi Adi and Alexandre Défossez},
    booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
    year={2023},
}
```

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

