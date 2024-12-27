from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
import os

# Retrieve environment variables
azure_tenant_id = os.getenv("ARM_TENANT_ID")
azure_client_id = os.getenv("ARM_CLIENT_ID")
azure_client_secret = os.getenv("ARM_CLIENT_SECRET")

key_vault_name = "Databricks-vault-01"

if not all([azure_tenant_id, azure_client_id, azure_client_secret]):
    raise ValueError("One or more environment variables (ARM_TENANT_ID, ARM_CLIENT_ID, ARM_CLIENT_SECRET) are missing.")

azure_credentials = ClientSecretCredential(azure_tenant_id, azure_client_id, azure_client_secret)

key_vault_url = f"https://{key_vault_name}.vault.azure.net/"

client = SecretClient(vault_url=key_vault_url, credential=azure_credentials)

secret_name = "Common-Password"

try:
    retrieved_secret = client.get_secret(secret_name)
    print(f"The secret value is: {retrieved_secret.value}")
except Exception as e:
    print(f"An error occurred: {e}")
