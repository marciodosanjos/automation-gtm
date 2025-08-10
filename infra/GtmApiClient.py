from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

from domain.Variable import Variable


class GtmApiClient:
    def __init__(self, credentials_path: str):
        self.service = self.authenticate(credentials_path)

    def authenticate(self, credentials_path:str):

        SCOPES = [
        'https://www.googleapis.com/auth/tagmanager.readonly',  
        'https://www.googleapis.com/auth/tagmanager.edit.containers',
        'https://www.googleapis.com/auth/tagmanager.edit.containerversions',
        'https://www.googleapis.com/auth/tagmanager.publish',
        #'https://www.googleapis.com/auth/tagmanager.delete.containers',
       ]
    
        credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=SCOPES
        )
        # Força refresh para garantir token válido
        request = Request()
        credentials.refresh(request)

        print(f"Access token obtido: {credentials.token[:20]}...")

        # Creates the client API GTM
        service = build('tagmanager', 'v2', credentials=credentials, cache_discovery=False)
        return service


    def list_methods(self):
        return self.service.accounts().containers().get.__doc__

    # -------------------------------------------------------------
    #  METHODS FOR ACCOUNT OPERATIONS
    # -------------------------------------------------------------
    def create_account(self, account_data: dict):
        """Creates a new account in the GTM API."""
        return self.service.accounts().create(body=account_data).execute()

    def get_account(self, account_path: str):
        """Fetches an existing account from the API."""
        return self.service.accounts().get(path=account_path).execute()

    def update_account(self, account_path: str, account_data: dict):
        """Updates an existing account."""
        return self.service.accounts().update(path=account_path, body=account_data).execute()

    def delete_account(self, account_path: str):
        """Deletes an account."""
        return self.service.accounts().delete(path=account_path).execute()

    # -------------------------------------------------------------
    #  METHODS FOR CONTAINER OPERATIONS
    # -------------------------------------------------------------
    def create_container(self, account_path: str, container_data: dict):
        """Creates a new container in the GTM API."""
        return self.service.accounts().containers().create(parent=account_path, body=container_data).execute()

    def get_container(self, container_path: str):
        """Fetches an existing container from the API."""
        return self.service.accounts().containers().get(path=container_path).execute()

    def update_container(self, container_path: str, container_data: dict):
        """Updates an existing container."""
        return self.service.accounts().containers().update(path=container_path, body=container_data).execute()

    def delete_container(self, container_path: str):
        """Deletes a container."""
        return self.service.accounts().containers().delete(path=container_path).execute()

    # -------------------------------------------------------------
    #  METHODS FOR TAG OPERATIONS
    # -------------------------------------------------------------
    def create_tag(self, container_path: str, tag_data: dict):
        """Creates a new tag inside a container."""
        return self.service.accounts().containers().tags().create(parent=container_path, body=tag_data).execute()

    def get_tag(self, tag_path: str):
        """Fetches a specific tag."""
        return self.service.accounts().containers().tags().get(path=tag_path).execute()

    def update_tag(self, tag_path: str, tag_data: dict):
        """Updates an existing tag."""
        return self.service.accounts().containers().tags().update(path=tag_path, body=tag_data).execute()

    def delete_tag(self, tag_path: str):
        """Deletes a tag."""
        return self.service.accounts().containers().tags().delete(path=tag_path).execute()

    # -------------------------------------------------------------
    #  METHODS FOR TRIGGER OPERATIONS
    # -------------------------------------------------------------
    def create_trigger(self, container_path: str, trigger_data: dict):
        """Creates a new trigger inside a container."""
        return self.service.accounts().containers().triggers().create(parent=container_path, body=trigger_data).execute()

    def get_trigger(self, trigger_path: str):
        """Fetches a specific trigger."""
        return self.service.accounts().containers().triggers().get(path=trigger_path).execute()

    def update_trigger(self, trigger_path: str, trigger_data: dict):
        """Updates an existing trigger."""
        return self.service.accounts().containers().triggers().update(path=trigger_path, body=trigger_data).execute()
        
    def delete_trigger(self, trigger_path: str):
        """Deletes a trigger."""
        return self.service.accounts().containers().triggers().delete(path=trigger_path).execute()

    # -------------------------------------------------------------
    #  METHODS FOR VARIABLE OPERATIONS
    # -------------------------------------------------------------
    def create_variable(self, workspace_path: str, variable_data: dict):
        """Creates a new variable inside a workspace."""
        return self.service.accounts().containers().workspaces().variables().create(
            parent=workspace_path,
            body=variable_data
        ).execute()


    def get_variable(self, variable_path: str):
        """Fetches a specific variable."""
        return self.service.accounts().containers().variables().get(path=variable_path).execute()
    
    def update_variable(self, variable_path: str, variable_data: dict):
        """Updates an existing variable."""
        return self.service.accounts().containers().variables().update(path=variable_path, body=variable_data).execute()

    def delete_variable(self, variable_path: str):
        """Deletes a variable."""
        return self.service.accounts().containers().variables().delete(path=variable_path).execute()

    # -------------------------------------------------------------
    #  METHODS FOR VERSION OPERATIONS
    # -------------------------------------------------------------
    def get_version(self, version_path: str):
        """Fetches a specific version."""
        return self.service.accounts().containers().versions().get(path=version_path).execute()

    def publish_container_version(self, container_path: str, version_notes: str):
        """Publishes the latest version of a container."""
        return self.service.accounts().containers().versions().publish(
            path=container_path, body={"notes": version_notes}
        ).execute()

    def update_version(self, version_path: str, version_data: dict):
        """Updates an existing version (e.g., notes)."""
        return self.service.accounts().containers().versions().update(path=version_path, body=version_data).execute()

    def delete_version(self, version_path: str):
        """Deletes a version."""
        return self.service.accounts().containers().versions().delete(path=version_path).execute()
    

    def get_workspace_id(self, account_id:str, container_id:str):
    
        workspace_list = self.service.accounts().containers().workspaces().list(
        parent=f"accounts/{account_id}/containers/{container_id}"
        ).execute()

        workspace_id = workspace_list['workspace'][0]['workspaceId']  # geralmente o primeiro é o "Default Workspace"
        workspace_path = f"accounts/{account_id}/containers/{container_id}/workspaces/{workspace_id}"
        return workspace_path