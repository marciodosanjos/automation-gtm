from domain.Account import Account
from infra.AccountRepository import AccountRepository

class AccountService:
    def __init__(self, account_repository: AccountRepository):
        """
        Initializes the service with a repository for account data.
        """
        self.account_repository = account_repository

    def create_account(self, name: str) -> Account:
        """
        Orchestrates the creation of a new GTM account.
        """
        # 1. Create the Account domain object.
        new_account = Account(name=name)

        # 2. Use the repository to persist the object.
        # The repository will make the API call and update the 'new_account'
        # object with the account_id and path returned by the API.
        self.account_repository.save(new_account)
        
        print(f"Service: New account '{new_account.name}' created with ID {new_account.account_id}")

        return new_account

    def get_account_by_path(self, account_path: str) -> Account:
        """
        Fetches an existing account by its path.
        """
        # The service delegates the fetching logic to the repository.
        account = self.account_repository.findById(account_path)
        
        if not account:
            raise ValueError(f"Account with path '{account_path}' not found.")
            
        return account

    def update_account(self, account: Account, new_name: str):
        """
        Orchestrates the update of an existing account.
        This method includes a simple business rule.
        """
        # Business logic: a name must be provided to update the account.
        if not new_name:
            raise ValueError("A new name must be provided to update the account.")

        # Update the domain object's state in memory.
        account.name = new_name

        # Delegate the persistence of the updated object to the repository.
        self.account_repository.update(account)
        
        print(f"Service: Account '{account.name}' updated successfully.")

    def delete_account(self, account: Account):
        """
        Deletes an account from the GTM API.
        """
        # Delegate the deletion to the repository.
        if not account.path:
            raise ValueError("Cannot delete account: path is missing.")
            
        self.account_repository.remove(account.path)
        
        print(f"Service: Account '{account.name}' deleted successfully.")