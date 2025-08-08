from typing import List
from model.Tag import Tag
from model.Trigger import Trigger
from model.Variable import Variable
from model.Version import Version

class Container:
    def __init__(self, name: str):
        self.name = name
        self.tags: List[Tag] = []
        self.triggers: List[Trigger] = []
        self.variables: List[Variable] = []
        self.version: Version
        self.containerId: str

    # tag methods
    def add_tag(self, tag: Tag):
        """Adds a tag to the container's internal list."""
        if self._is_valid_tag(tag):
            self.tags.append(tag)
            print(f"Tag {tag.tag_type} added to container {self.name}.")

    def remove_tag(self, tag_id: str):
        """Remove a tag from the internal list by ID."""
        self.tags = [tag for tag in self.tags if tag.id != tag_id]
        print(f"Tag {tag_id} removed from container {self.name}.")

    # trigger methods
    def add_trigger(self, trigger: Trigger):
        """Adds a trigger to the container's internal list."""
        self.triggers.append(trigger)
        print(f"Trigger {trigger.type} added to container {self.name}.")

    def remove_trigger(self, trigger_id: str):
        """Removes a trigger from the internal list by ID."""
        self.triggers = [trigger for trigger in self.triggers if trigger.id != trigger_id]
        print(f"Trigger {trigger_id} removed from container {self.name}.")


    #variable methods
    def add_variable(self, variable: Variable):
        """Adds a trigger to the container's internal list."""
        self.variables.append(variable)
        print(f"Trigger {variable.type} added to container {self.name}.")

    # container methods
    def getContainerId(self):
        return self.containerId
    
    def publish(self, version: str):
        """
        Prepares the container for publication by creating a new version.
        It does not interact with the API, it only manages the internal state.
        """
        if self._is_valid_for_publication():
            self.version = Version(version=version)
            print(f"Container {self.name} ready for publication. New version created.")
            return True
        print("Erro: Container não pode ser publicado. Falha na validação.")
        return False

    def _is_valid_tag(self, tag: Tag) -> bool:
        """
        Internal tag validation logic (example).
        """
        if not tag.tag_type or not tag.value:
            return False
        return True

    def _is_valid_for_publication(self) -> bool:
        """
        Internal logic to check if the container is in a valid state
        for publishing (example: all tags are valid).
        """
        if not self.tags:
            print("Erro: Containers must have at least one tag.")
            return False
        # Outras validações
        return True
