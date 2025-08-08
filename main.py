from service.GtmService import GtmContainerService
from repository.ContainerRepository import ContainerRepository

formData = {
    "website": "myfavcont.com",
    "GA4 Standard": "true",
    "GA4 E-commerce":"false",
    "websLINE": "false"
}

def main():
    gtmRepo = ContainerRepository()
    gtmService = GtmContainerService(gtmRepo)
    gtmService.createContainerWithTags(formData)


main()