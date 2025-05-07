from huggingface_hub import snapshot_download
import os

# Define o ID do repositório
repo_id = "Mizukiluke/ureader-instruction-1.0"

# Define o diretório local onde os arquivos serão salvos
local_dir = "dataset"

# Cria o diretório se ele não existir
os.makedirs(local_dir, exist_ok=True)

# Baixa todos os arquivos do repositório
snapshot_download(repo_id=repo_id, repo_type="dataset", local_dir=local_dir)

print(f"Todos os arquivos do dataset '{repo_id}' foram baixados para a pasta '{local_dir}'.")