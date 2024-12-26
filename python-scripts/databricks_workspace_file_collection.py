import requests
import json
from blob_file_creation import blob_file_creation

# Set your Databricks instance URL and personal access token
DATABRICKS_INSTANCE_URL = "https://<your-databricks-instance>.azuredatabricks.net"  # Replace with your Databricks URL
DATABRICKS_TOKEN = "<your-databricks-token>"  # Replace with your personal access token


# Function to recursively list files and folders in Databricks Workspace
def list_workspace_files(path, Databricks_token, databricks_instance_url):

    # Set the workspace path you want to start the search from, e.g., '/Workspace/'
    workspace_path = "/Workspace"  # Starting folder in Databricks Workspace

    # Headers for Databricks REST API authentication
    headers = {
        "Authorization": f"Bearer {Databricks_token}"
    }

    # Databricks API endpoint to list workspace files and directories
    api_url = f"{databricks_instance_url}/api/2.0/workspace/list"
    params = {
        "path": path  # Specify the path to list
    }

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        # Parse the response JSON
        files = response.json()
        
        # Process files and directories
        for item in files.get('files', []):
            if item['is_dir']:
                # If the item is a directory, recursively call the function for this directory
                print(f"Directory: {item['path']}")
                list_workspace_files(item['path'])  # Recurse into subdirectories
            else:
                # If the item is a file, print its path
                print(f"File: {item['path']}")
                blob_file_creation(item['path'])
    else:
        print(f"Error: {response.status_code} - {response.text}")

