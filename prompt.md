已知ollama的数据目录默认位于 ~/.ollama下，Ollama保存的模型文件通过这样的方式组织：

~/.ollama/models/manifests/registry.ollama.ai/library/<model_name>/<tag_name> 这个文本文件中保存模型的manifest定义文件，这个文件是docker manifest v2标准的，一个模型文件Manifest例子如下：
```json
{
    "schemaVersion": 2,
    "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
    "config": {
        "mediaType": "application/vnd.docker.container.image.v1+json",
        "digest": "sha256:ff66e414ed4e7dbb276d7972f9c7e96177f6c22bf66eccf9ed46d420ad9da19d",
        "size": 559
    },
    "layers": [
        {
            "mediaType": "application/vnd.ollama.image.model",
            "digest": "sha256:504cedf78c8f1cd869102b2a6533211785d88393875e7c247d231e5b2aa970f0",
            "size": 4179437664
        },
        {
            "mediaType": "application/vnd.ollama.image.license",
            "digest": "sha256:9cdf4ff2dc84c60b3d5598dfc439c877788660207d2cd54dd6dab50d4a7cf15d",
            "size": 41
        },
        {
            "mediaType": "application/vnd.ollama.image.template",
            "digest": "sha256:62fbfd9ed093d6e5ac83190c86eec5369317919f4b149598d2dbb38900e9faef",
            "size": 182
        },
        {
            "mediaType": "application/vnd.ollama.image.system",
            "digest": "sha256:75357d685f238b6afd7738be9786fdafde641eb6ca9a3be7471939715a68a4de",
            "size": 28
        },
        {
            "mediaType": "application/vnd.ollama.image.params",
            "digest": "sha256:f02dd72bb2423204352eabc5637b44d79d17f109fdb510a7c51455892aa2d216",
            "size": 59
        }
    ]
}
```

其中layers字段定义的每一个layer都是一个文件，这些文件统一保存在 ~/.ollama/models/blobs目录下，在这个目录里，文件名都是'sha256-xxxxxxxx'这样的格式，也就是这里的文件名等于manifest中每一个layer的digest值。

请你使用python开发一个命令行工具程序，给定参数<model_name>和<tag_name>，自动导出它的manifest和blobs文件，复制这些文件保存到一个新位置<target_path>；
具体有以下要求：
1. ~/.ollama 这个目录只是一个例子，有的用户将这个目录修改到了其他地方，此工具应该支持设定一个models_dir参数来指定其他的models目录的位置，最终程序处理数据时应该将此目录当作 ~/.ollama/models目录来处理；
2. 将文件复制到新的<target_path>目录后，需要保持和原来目录结构一致，将<target_path>作为新的models目录，在<target_path>中创建blobs目录、创建manifests目录以及registry.ollama.ai等必要的子目录，最后将manifest文件按照相同的文件名保存。

如果你理解了我的全部需求，请回复已理解，如果你有任何不确定的问题，请向我提问。