from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
import os

# Retrieve environment variables
azure_tenant_id = os.getenv("ARM_TENANT_ID")
azure_client_id = os.getenv("ARM_CLIENT_ID")
azure_client_secret = os.getenv("ARM_CLIENT_SECRET")

# Check if the environment variables are correctly set
if not all([azure_tenant_id, azure_client_id, azure_client_secret]):
    raise ValueError("One or more environment variables (ARM_TENANT_ID, ARM_CLIENT_ID, ARM_CLIENT_SECRET) are missing.")

# Use ClientSecretCredential to authenticate with Azure
azure_credentials = ClientSecretCredential(azure_tenant_id, azure_client_id, azure_client_secret)

# Define Key Vault URL
key_vault_url = "https://Cloud-Secret-vault-02.vault.azure.net/"

# Initialize the SecretClient
client = SecretClient(vault_url=key_vault_url, credential=azure_credentials)

# Specify the name of the secret you want to retrieve
secret_name = "VM-Password"

try:
    # Get the secret from the Key Vault
    retrieved_secret = client.get_secret(secret_name)
    print(f"The secret value is: {retrieved_secret.value}")
except Exception as e:
    print(f"An error occurred: {e}")
