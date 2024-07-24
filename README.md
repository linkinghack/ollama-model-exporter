# Ollama 模型导出工具 -- Ollama model exporter

> IMPORTAN: 此项目使用OpenAI/GPT-4o 开发
> 提示词位于：prompt.md 

## 功能说明
该脚本会根据提供的 models_dir 定位到对应的模型目录。
读取指定模型和标签的 manifest 文件，并解析其中的 layers。
将 manifest 文件和对应的 blobs 文件复制到目标路径，保持原有的目录结构。

## 使用说明
通过命令行运行该脚本，指定模型名称、标签名称和目标路径，示例如下：

`python exporter.py <model_name> <tag_name> <target_path> --models_dir <models_dir>`

例如：

`python exporter.py my_model v1.0 /path/to/export --models_dir /custom/ollama/models`

## 使用场景
当需要将本地某一个模型导出到其他主机运行，或者需要将指定的模型打包到容器镜像中时，可以使用此工具将目标模型拷贝到固定的目录下，随后执行其他动作。

### 容器镜像打包本地模型
1. 使用此工具导出模型：`python exporter.py qwen2 7b ./qwen-exported --models_dir 'e:\ollama-models'`

2. docker build打包
```dockerfile
FROM ollama/ollama
COPY ./qwen-exported /root/.ollama/models
```