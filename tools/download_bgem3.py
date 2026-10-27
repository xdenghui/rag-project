from modelscope.hub.snapshot_download import snapshot_download

# 下载模型到 Mac 本地指定目录
model_dir = snapshot_download('BAAI/bge-m3', cache_dir='/Users/xdh_1024/ai_models/modelscope')

print(f"模型已下载到: {model_dir}")