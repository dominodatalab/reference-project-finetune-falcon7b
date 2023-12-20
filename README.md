# Fine Tuning Falcon-7b

## License
This template is licensed under Apache 2.0 and contains the following components: 
* Falcon 7B [Apache 2.0](https://huggingface.co/tiiuae/falcon-7b)
* lit-gpt [Apache 2.0](https://github.com/Lightning-AI/lit-gpt/blob/main/LICENSE)

## About this project
This reference project shows how to fine tune the Falcon-7b and Falcon-7b-instruct models on a conversational dataset using PyTorch Lightning. The code is based on the the `lit-gpt` project by PyTorch Lightning with changes made for it to run on Domino and the conversational dataset that we have curated.

Here are a list of important files in the project that you might need to edit in order to customize this further for your use case.

* [falcon_7b.ipynb](https://github.com/dominodatalab/reference-project-finetune-falcon7b/blob/main/falcon_7b.ipynb) : This file contains a list of preprocessing and setup steps that are required to fine tune the model. This also has code to trigger the fine tuning of the model. Specificaly the code in this file downloads the `Falcon-7b` model, converts it to a format that PyTorch Lightning can use, prepares the dataset for the fine tuning and starts the fine tuning.Once the fine tuning is done, it also has code cells where outputs can be generated from user supplied prompts.

* [falcon_7b_instruct.ipynb](https://github.com/dominodatalab/reference-project-finetune-falcon7b/blob/main/falcon_7b_instruct.ipynb) : This file contains a list of preprocessing and setup steps that are required to fine tune the model. This also has code to trigger the fine tuning of the model. Specificaly the code in this file downloads the `Falcon-7b-instruct` model, converts it to a format that PyTorch Lightning can use, prepares the dataset for the fine tuning and starts the fine tuning.Once the fine tuning is done, it also has code cells where outputs can be generated from user supplied prompts.

* [data.json](https://github.com/dominodatalab/reference-project-finetune-falcon7b/blob/main/lit-gpt/conversation_data/data.json) : This file contains a list of conversations that we will use as a dataset to tune the Falcon-7b and Falcon-7b-instruct models

* [lit-gpt/finetune](https://github.com/dominodatalab/reference-project-finetune-falcon7b/blob/main/lit-gpt/finetune) : This directory contains files for different fine tuning mechanisms. Change the parameters in the `setup` function in case you want to change the default location of where data is read from, where results and checkpoints are stored and precision to use. The format of `sample` has also been modified to match the conversation dataset we are using for the finetuning. Please change this if you are changing the dataset for finetuning

* [lit-gpt/generate](https://github.com/dominodatalab/reference-project-finetune-falcon7b/blob/main/lit-gpt/generate): This directory contains files to generate outputs from the fine tuned models. Change the paramteres in the `main` function in case you want to change the defaults being used. Also modify the `sample` variable to match the dataset that you are used for fine tuning the model 

## Setup instructions

This project requires the following [compute environments](https://docs.dominodatalab.com/en/latest/user_guide/f51038/environments/) to be present. Also please ensure the [Automatically make compatible with Domino](https://docs.dominodatalab.com/en/latest/user_guide/4e0c34/create-a-domino-environment-with-a-pre-built-image/) checkbox is selected and create the environment afresh instead of duplicating an existing environment that does not use the same base image and dependencies.

Please note that you will need a GPU with 24GB VRAM for this project. This project was tested on an Nvidia `A10G` GPU with 24 GB of RAM . Also take care to provision adequate disc space for your workspace as the model binary occupies ~15GB on disc.

### Environment Requirements

`nvcr.io/nvidia/pytorch:21.10-py3`

**Dockerfile Instructions**

```
RUN pip install --index-url https://download.pytorch.org/whl/nightly/cu118 --pre 'torch>=2.1.0dev'

RUN pip install lightning@git+https://github.com/Lightning-AI/lightning@master \
                tokenizers \
                jsonargparse[signatures]  \ 
                bitsandbytes>=0.40.0  \
                scipy \
                datasets \ 
                zstandard 
```

Once you have spun up a workspace, clone this repo.
```
git clone https://github.com/dominodatalab/reference-project-falcon7b.git
```

### Hardware Requirements
This fine tuning was tested successfully on a T4 GPU with 16GB of GPU RAM.
