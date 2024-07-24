FROM ollama/ollama
ARG MODEL_DIR=./codeqwen-7b
COPY $MODEL_DIR /root/.ollama/models
EXPOSE 11434