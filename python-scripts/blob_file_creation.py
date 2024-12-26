from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Azure Storage account URL and SAS token
account_url = "<storage-account-url>"  # Replace with your storage account URL
sas_token = "<blob-sas-token>"

# Combine the account URL and SAS token to create the connection string
connection_string = account_url + sas_token

# Define the container name and blob (file) name
container_name = "<container-name>"  # Replace with your container name
blob_name = "<blob-name>"     # The name of the blob you want to create
file_path = "<file-path>"  # Local path of the file to upload

def blob_file_creation(account_url, sas_token, container_name, blob_name, file_path):

    # Create the BlobServiceClient object using the connection string
    blob_service_client = BlobServiceClient(account_url=account_url, credential=sas_token)

    # Create the container client
    container_client = blob_service_client.get_container_client(container_name)

    # Create the container if it does not exist
    try:
        container_client.create_container()
        print(f"Container '{container_name}' created successfully.")
    except Exception as e:
        print(f"Container already exists or an error occurred: {e}")

    # Create a BlobClient object for the blob
    blob_client = container_client.get_blob_client(blob_name)

    # Upload a local file to the created blob
    try:
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"File '{file_path}' uploaded as blob '{blob_name}' successfully.")
    except Exception as e:
        print(f"Error uploading file: {e}")
