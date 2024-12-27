import requests
import json
from blob_file_creation import blob_file_creation

# Set your Databricks instance URL and personal access token
DATABRICKS_INSTANCE_URL = "https://<your-databricks-instance>.azuredatabricks.net"  # Replace with your Databricks URL
DATABRICKS_TOKEN = "<your-databricks-token>"  # Replace with your personal access token


def list_workspace_files(path, Databricks_token, databricks_instance_url):
    workspace_path = "/Workspace"  # Starting folder in Databricks Workspace
    headers = {
        "Authorization": f"Bearer {Databricks_token}"
    }

    api_url = f"{databricks_instance_url}/api/2.0/workspace/list"
    params = {
        "path": path  # Specify the path to list
    }

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        files = response.json()
        
        for item in files.get('files', []):
            if item['is_dir']:
                print(f"Directory: {item['path']}")
                list_workspace_files(item['path'])  
            else:
                print(f"File: {item['path']}")
                blob_file_creation(item['path'])
    else:
        print(f"Error: {response.status_code} - {response.text}")

