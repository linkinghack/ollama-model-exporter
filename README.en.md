# Ollama Model Exporter

> IMPORTANT: This project was developed using OpenAI/GPT-4o.
> The prompt is located in: prompt.md

## Functionality
This script locates the appropriate model directory based on the provided `models_dir`.
It reads the manifest file for the specified model and tag, and parses the layers within.
The manifest file and corresponding blob files are copied to the target path, maintaining the original directory structure.

## Usage
Run the script from the command line, specifying the model name, tag name, and target path. Example:

`python exporter.py <model_name> <tag_name> <target_path> --models_dir <models_dir>`

For instance:

`python exporter.py my_model v1.0 /path/to/export --models_dir /custom/ollama/models`

## Use Cases
When you need to export a local model to run on another host, or package a specific model into a container image, you can use this tool to copy the target model to a fixed directory, and then proceed with other actions.

### Packaging Local Model into a Container Image
1. Export the model using this tool: `python exporter.py qwen2 7b ./qwen-exported --models_dir 'e:\ollama-models'`

2. Build the Docker image:
```dockerfile
FROM ollama/ollama
ARG MODEL_DIR=./codeqwen-7b
COPY $MODEL_DIR /root/.ollama/models
EXPOSE 11434
```

`docker build --build-arg MODEL_DIR=./exporterd-model -t llm-ollama:7b-qint4 .`