from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from jobs_dependencies_migration import migrate_jobs


def blob_file_creation(account_url, sas_token, container_name, blob_name, file_path):

    connection_string = account_url + sas_token

    print("Storage Account Connection URL: ", connection_string)

    blob_service_client = BlobServiceClient(account_url=account_url, credential=sas_token)
    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.create_container()
        print(f"Container '{container_name}' created successfully.")
    except Exception as e:
        print(f"Container already exists or an error occurred: {e}")
    blob_client = container_client.get_blob_client(blob_name)

    try:
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"File '{file_path}' uploaded as blob '{blob_name}' successfully.")
    except Exception as e:
        print(f"Error uploading file: {e}")


