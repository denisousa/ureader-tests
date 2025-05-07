from huggingface_hub import snapshot_download

# Baixar o repositório completo
snapshot_download(repo_id="Mizukiluke/ureader-v1", local_dir="./ureader-v1")
