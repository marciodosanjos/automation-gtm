from typing import List, Dict, Any, Optional
from domain.Container import Container

class Account:
    def __init__(self,
                 name: str,
                 account_id: Optional[str] = None,
                 path: Optional[str] = None):
        
        # Atributos que correspondem aos campos da API
        self.name = name
        self.account_id = account_id
        self.path = path  # O caminho completo para o recurso na API

        # A lista de contêineres gerenciados por esta conta
        self.containers: List[Container] = []

    def add_container(self, container: Container):
        """Adiciona um contêiner à lista interna da conta."""
        if container.account_id is None:
            container.account_id = self.account_id
        self.containers.append(container)

    def remove_container(self, container_id: str):
        """Remove um contêiner da lista por ID."""
        self.containers = [c for c in self.containers if c.container_id != container_id]

    def to_api_format(self) -> Dict[str, Any]:
        """
        Converte o objeto Conta para o formato de dicionário da API.
        A API do GTM espera um formato simples para a criação de contas.
        """
        api_data = {
            "name": self.name
        }
        return api_data

    @classmethod
    def from_api_format(cls, api_data: Dict[str, Any]):
        """
        Cria uma nova instância de Conta a partir de um dicionário retornado pela API.
        """
        instance = cls(
            name=api_data.get("name", ""),
            account_id=api_data.get("accountId"),
            path=api_data.get("path")
        )
        # Observação: a API não retorna a lista de containers diretamente.
        # Eles teriam que ser buscados separadamente pelo repositório.
        return instance