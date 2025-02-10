[![Python application test with Github Actions](https://github.com/ldself/azure-ci-cd-pipeline/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/ldself/azure-ci-cd-pipeline/actions/workflows/pythonapp.yml)

# azure-ci-cd-pipeline

## Introduction
In this project, a Github repository will be built from scratch and scaffolding will be created that will assist in performing both Continuous Integration and Continuous Delivery. Github Actions will be used along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Then, this project will be integrated with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Getting Started
[Create](https://github.com) a GitHub account
[Create](https://azure.microsoft.com) an Azure subscription
[Install](https://github.com/marketplace/azure-pipelines) Azure Pipelines from GitHub marketplace 
Generate ssh keys (ssh-keygen).  Add private key to GitHub account

## Dependencies
This project assumes that you have a public and private key pair generated that will be used to communicate with GitHub.  It is expected that a copy of the public key will be associated to your GitHub account.

To create the key pair, open up a cloud shell in Azure and type the following
```sh
ssh-keygen -t rsa
```
The contents of the ./.ssh/id_rsa.pub should be stored in your GitHub account using the linked [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

## Instructions

### Creating the Cloud Shell structure
* Fork this repo to your own GitHub account then clone the repo to your cloud shell environment
* Navigate to the newly created folder.  The folder will contain the following files:
  
| file | description |
| ------ | ------ |
| Makefile | shortcuts to build, test, and deploy a project|
| requirements.txt| project's package dependencies |
| <span>hello.py</span> | basic python app |
| test_hello.py | tests for the basic python file |

* Create a virtual environment using the following code `python3 -m venv .venv`
  * This will create a hidden subfolder called `.venv` that will contain your project's libraries
  * `.venv` is included in `.gitignore` so it won't be pushed to the repository
* Install the required files by executing `make all` at a command prompt
  * This will also run a test and a lint check against the code
  * The result should look similar to the following:
![alt text](image.png)

### Configure GitHub Actions
![alt text](image-1.png)
