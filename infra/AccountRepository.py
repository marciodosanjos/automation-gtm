from domain.Account import Account
from infra.GtmApiClient import GtmApiClient

class AccountRepository:
    def __init__(self, api_client: GtmApiClient):
        """
        Initializes the repository with a GtmApiClient instance.
        """
        self.api_client = api_client

    def save(self, account: Account) -> None:
        """
        Saves a new Account by calling the GTM API's account creation method.
        The repository is responsible for updating the Account object with
        the ID and path returned by the API.
        """
        # The GTM API requires a simple object for account creation
        account_data = self._to_api_format(account)
        
        # The API call is delegated to the GtmApiClient
        api_response = self.api_client.create_account(account_data)

        # Update the domain object with the new information from the API
        account.account_id = api_response.get("accountId")
        account.path = api_response.get("path")
        
        print(f"Account '{account.name}' created in API with ID: {account.account_id} and path: {account.path}")

    def findById(self, account_path: str) -> Account:
        """
        Finds an Account by its full path and returns it as a domain object.
        """
        # The API call is delegated to the GtmApiClient
        api_response = self.api_client.get_account(account_path)

        # Convert the API response (dict) to a domain object
        account = self._from_api_format(api_response)
        
        print(f"Account '{account.name}' found from API.")
        return account

    def update(self, account: Account) -> None:
        """
        Updates an existing Account in the GTM API.
        The repository uses the path stored in the Account object.
        """
        if not account.path:
            raise ValueError("Cannot update account: path is missing.")
            
        account_data = self._to_api_format(account)
        self.api_client.update_account(account.path, account_data)
        
        print(f"Account '{account.name}' updated in API successfully.")

    def remove(self, account_path: str) -> None:
        """
        Removes an Account from the GTM API.
        """
        self.api_client.delete_account(account_path)
        print(f"Account at path '{account_path}' removed from API.")

    def _to_api_format(self, account: Account) -> dict:
        """
        Internal utility to convert the Account domain object to an API-friendly dictionary.
        """
        return {
            "name": account.name
        }

    def _from_api_format(self, api_data: dict) -> Account:
        """
        Internal utility to convert an API response dictionary to an Account domain object.
        """
        return Account(
            name=api_data.get("name", ""),
            account_id=api_data.get("accountId"),
            path=api_data.get("path")
        )