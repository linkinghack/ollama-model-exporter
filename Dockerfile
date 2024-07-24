FROM ollama/ollama
ARG MODEL_DIR=./codeqwen-7b
COPY $MODEL_DIR /root/.ollama/models
COPY id_ed25519 /root/.ollama/
COPY id_ed25519.pub /root/.ollama/