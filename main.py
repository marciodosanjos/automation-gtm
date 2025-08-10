import os
from domain.Variable import Variable
from infra.GtmApiClient import GtmApiClient
from infra.AccountRepository import AccountRepository
from infra.ContainerRepository import ContainerRepository
from services.AccountService import AccountService
from services.ContainerService import ContainerService


formData = {

}

def main():
    # --- Step 1: Configure the env vars ---    
    CREDENTIALS_PATH = "C:/projetos/gtm-automation/client_secrets.json"
    ACCOUNT_ID = "6257662716"       
    CONTAINER_ID = "199910509"    
    
    # Build the complete container path, which is what the API expects
    container_path = f"accounts/{ACCOUNT_ID}/containers/{CONTAINER_ID}"
    
    # --- Step 2: Initialize the Architecture Layers ---

    try:
        # Infrastructure Layer: Initializes the API client        
        gtm_api_client = GtmApiClient(CREDENTIALS_PATH)
    
        # Persistence Layer: Initializes the repositories with the client
        account_repository = AccountRepository(gtm_api_client)
        container_repository = ContainerRepository(gtm_api_client)
        
        # Service Layer: Initializes the services with the repositories
        account_service = AccountService(account_repository)
        container_service = ContainerService(account_service, container_repository)
        
    except Exception as e:
        print(f"Error initializing layers: {e}")
        return

    # --- Passo 3: Performing the Test Operation ---
    print(f"\n--- Starting the container search '{CONTAINER_ID}' ---")
    
    try:
        
        #get workspace path
        workspace_path = gtm_api_client.get_workspace_id(ACCOUNT_ID, CONTAINER_ID)

        #criar uma variavel no container
        ga4_mess_id = Variable("MessID", "c", {"type": "template", "key":"value", "value":"12344"})
        container_repository.create_variable(workspace_path, ga4_mess_id)

        # If the object was returned successfully, communication with the API worked
        print("Container successfully found in the API.")
        
    except Exception as e:
        print(f"Error: {e}")

main()