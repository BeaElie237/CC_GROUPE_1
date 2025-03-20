from huggingface_hub import HfApi, Repository

# Remplacez par votre token Hugging Face
hf_token = "Hugging_face_token"

# Nom du repository sur Hugging Face
repo_name = "armelmbia/CC_GROUPE_1"

# Chemin vers votre repository local
local_repo_path = "c:/Users/HP/Documents/GitHub/CC_GROUPE_1"

# Créer un repository sur Hugging Face
api = HfApi()
api.create_repo(repo_name, token=hf_token)

# Cloner le repository Hugging Face dans le répertoire local
repo = Repository(local_dir=local_repo_path, clone_from=repo_name, use_auth_token=hf_token)

# Ajouter tous les fichiers et pousser les changements
repo.git_add()
repo.git_commit("Dernier commit")
repo.git_push()