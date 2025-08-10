from domain.Container import Container 
from domain.Variable import Variable
from infra.GtmApiClient import GtmApiClient 

class ContainerRepository:
    def __init__(self, api_client: GtmApiClient):
        """
        Initializes the repository with a GtmApiClient instance.
        """
        self.api_client = api_client

    def save(self, container: Container, account_id: str):
        """
        Saves a new or existing Container by calling the GTM API.
        It orchestrates the creation of the container itself and all its components.
        """
        account_path = f"accounts/{account_id}"

        # 1. Create the container itself and get its new ID
        container_data = self._to_api_format(container)
        api_response = self.api_client.create_container(account_path, container_data)
        container_path = api_response.get("path")
        
        print(f"Container '{container.name}' created with path: {container_path}")

        # 2. Create all components (tags, triggers, variables) inside the new container
        for tag in container.tags:
            self.api_client.create_tag(container_path, self._to_api_format(tag))
        
        for trigger in container.triggers:
            self.api_client.create_trigger(container_path, self._to_api_format(trigger))
            
        for variable in container.variables:
            self.api_client.create_variable(container_path, self._to_api_format(variable))
            
        print(f"Components for container '{container.name}' created successfully.")

    def findById(self, container_path: str) -> Container:
        """
        Finds a Container by its full path and fetches all its components.
        """
        
        # 1. Get the container data from the API
        container_data = self.api_client.get_container(container_path)

        # 2. Convert the API data to a Container domain object
        container = self._from_api_format(container_data)

        # 3. Fetch all components (tags, triggers, variables) from the API
        #    Note: This is a simplified example. A real implementation would list and fetch all components.
        #    The get_container() method in the GTM API does not return components,
        #    so you would need to call separate list methods.
        print(f"Container '{container.name}' found. Fetching components...")
        
        return container
    
    def update(self, container: Container):
        """
        Updates an existing Container and its components by ID.
        """
        container_path = container.container_path # Assumindo que o path está no objeto Container
        
        # 1. Update the container's main properties
        container_data = self._to_api_format(container)
        self.api_client.update_container(container_path, container_data)
        
        # 2. Update components (tags, triggers, etc.) individually
        for tag in container.tags:
            tag_path = f"{container_path}/tags/{tag.id}"
            self.api_client.update_tag(tag_path, self._to_api_format(tag))
            
        print(f"Container '{container.name}' and its components updated successfully.")
    
    def remove(self, container_path: str):
        """
        Removes a Container from the GTM API.
        """
        self.api_client.delete_container(container_path)
        print(f"Container at path '{container_path}' removed successfully.")
        
    def _to_api_format(self, obj):
        """
        Internal utility method to convert a domain object to a dict for the API.
        """
        # This is where the mapping logic would be
        if isinstance(obj, Container):
            return {"name": obj.name}
        # Adicione lógica para tags, triggers, etc.
        return obj.__dict__

    def _from_api_format(self, data: dict):
        """
        Internal utility method to convert API response (dict) to a domain object.
        """
        # This is where the reverse mapping logic would be
        container = Container("")
        # Adicione lógica para popular tags, triggers, etc. a partir do dict
        return container
    

    def create_variable(self, container_path: str, variable_obj: Variable):
        """
        Cria uma nova variável na API do GTM a partir de um objeto de domínio.
        """
        # Converter o objeto Variable para o formato de dicionário que a API espera
        api_data = {
            "name": variable_obj.name,
            "type": variable_obj.type,
            "parameter": variable_obj.params
        }
        
        # Passar o dicionário para a API
        response = self.api_client.create_variable(container_path, api_data)
        
        # Retornar o objeto de domínio atualizado
        return response
    

 
