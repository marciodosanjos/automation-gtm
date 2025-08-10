from domain.Tag import Tag
from domain.Variable import Variable
from domain.Trigger import Trigger
from domain.Container import Container
from infra.ContainerRepository import ContainerRepository
from services.AccountService import AccountService # Novo serviço para contas
from typing import Dict, Any

class ContainerService:

    def __init__(self, accountService: AccountService, containerRepository: ContainerRepository) -> None:
        """
        Inicializa o serviço com o AccountService e o ContainerRepository.
        """
        self.accountService = accountService
        self.containerRepository = containerRepository

    def createContainerWithComponents(self, account_path: str, formData: Dict[str, Any]) -> Container:
        """
        Orquestra a criação de um novo contêiner GTM com seus componentes.
        Ele delega a responsabilidade de buscar a conta para o AccountService.
        """
        print(f"Service: Buscando conta para criar o contêiner no caminho '{account_path}'.")

        # 1. Delega a responsabilidade de buscar a conta para o AccountService
        account = self.accountService.get_account_by_path(account_path)
        
        if not account:
            raise ValueError(f"Conta no caminho '{account_path}' não encontrada. Não é possível criar o contêiner.")

        # 2. Instancia os objetos de domínio (Container, Tags, etc.).
        tag = Tag(formData['tag_name'], formData['tag_type'])
        trigger = Trigger(formData['trigger_name'], formData['trigger_type'])
        variable = Variable(formData['variable_name'], formData['variable_type'])

        # O container é instanciado com o account_id para que o repositório saiba onde salvá-lo
        container = Container(name=formData['container_name'])
        container.add_tag(tag)
        container.add_trigger(trigger)
        container.add_variable(variable)

        # 3. Usa o ContainerRepository para persistir o novo contêiner.
        self.containerRepository.save(container, account.account_id or "")
        
        print(f"Service: Contêiner '{container.name}' criado e persistido com sucesso.")
        return container
    
    
    def get_container(self, account_path: str) -> Container:
        """
        Fetches an existing account by its path.
        """
        # The service delegates the fetching logic to the repository.
        account = self.containerRepository.findById(account_path)
        
        if not account:
            raise ValueError(f"Account with path '{account_path}' not found.")
            
        return account
    

    def update_container(self, account_path: str, container: Container) -> Container:

        container = self.get_container(account_path)

        if container:
            self.containerRepository.update(container)

            return container
        

        