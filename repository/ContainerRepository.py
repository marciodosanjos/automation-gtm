from model.Container import Container

class ContainerRepository:

    apiClient: str

    def save(self, container: Container):
        print("Container Repository: Creating container")

    def findById(self, containerId: str):
        print("Container Repository: Finding container")
    
    def update(self, containerId: str):
        print("Container Repository: Updating container")
    
    def remove(self, containerId: str):
        print("Container Repository: Removing container")
