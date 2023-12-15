# BonsAgi

![BonsAgi mascot](./assets/mascot.png)
<br/>
_"To shape a bonsai, is to shape a soul"_

## Abstract

BonsAgi is an attempt at AGI, by letting a python application write itself, while executing.
Theoretically this allows it to do anything, but realistically the application is limited by the understanding of the LLM used to write the code.
Built in is a safety check after each code iteration. Take your time to check the generated code, and do not run BonsAgi without safety measurements. Treat it like a virus that you set free on your computer.

## Setup

Download any LLM model, but recommended are:

- CodeLlama 7b/13b/34b for code writing. [Example](https://huggingface.co/TheBloke/CodeLlama-13B-GGUF)
- Mistral 7B for introspection. [Example](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)

Create a conda profile
`conda create -n bonsagi python=3.10.8`

Install dependencies
`pip install -r requirements.txt`

## Running

`python src/seed.py -c "Find me all prime numbers up to 1000 that are also palindromes, and calculate the sum of these."`

## Local development

Don't.

## TODO

Currently still in development

**Phase 1**

- Loop the thing
- Let it check yourself before you shrek yourself
- Freeze dependencies
- Promote

**Phase 2**

- Multi text modal
- Reflection with Mistral-7b
- Write logs
- CLI for human input
