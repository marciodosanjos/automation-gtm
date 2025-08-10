from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# Configurações
SCOPES = [
    'https://www.googleapis.com/auth/tagmanager.readonly',  # só leitura para teste
]
    # --- Step 1: Configure the env vars ---    
CREDENTIALS_PATH = "C:/projetos/gtm-automation/client_secrets.json"
ACCOUNT_ID = "6257662716"       
CONTAINER_ID = "199910509"    
    
    # Build the complete container path, which is what the API expects
container_path = f"accounts/{ACCOUNT_ID}/containers/{CONTAINER_ID}"


def test():
    # Carrega credenciais da service account e aplica scopes
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=SCOPES
    )

    # Força refresh para garantir token válido
    request = Request()
    credentials.refresh(request)

    print(f"Access token obtido: {credentials.token[:20]}...")

    # Cria o client da API GTM
    service = build('tagmanager', 'v2', credentials=credentials, cache_discovery=False)

    # Tenta listar as contas do GTM para essa credencial
    try:

        
        container = service.accounts().containers().get(path=container_path).execute()

        print(container)

    except Exception as e:
        print(f"Erro ao listar contas GTM: {e}")

test()
