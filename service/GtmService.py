
from model.Tag import Tag
from model.Variable import Variable
from model.Trigger import Trigger
from model.Container import Container
from repository.ContainerRepository import ContainerRepository

class GtmContainerService:

    containerRepository:ContainerRepository

    def __init__(self, containerRepository) -> None:
        self.containerRepository = containerRepository
        
    def createContainerWithTags(self, formData: dict) -> bool:

        print("Creating container")
        #instanciate container

        container = Container(formData['website'])
        
        for i in formData:

            if i == "GA4 Standard" and formData[i] == "true":
                ("Client wants GA4 Standard")
                 #add new tag to container
                newTag = Tag("GA4", "Config")
                container.add_tag(newTag)

                #add new trigger to container
                newTrigger = Trigger("Pageview", "All pages")
                container.add_trigger(newTrigger)

                #add new trigger to container
                newVariable = Variable("DataLayer", "ecommerce.event")
                container.add_variable(newVariable)

                #prepares container for publication
                container.publish("1.0")

                #save the created container 
                self.containerRepository.save(container)
            
        return True




        