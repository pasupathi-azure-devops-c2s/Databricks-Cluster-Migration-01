import requests
import zipfile
import os
from io import BytesIO
import json

def list_workspace_folders(workspace_url, workspace_token):
    list_url = f"{workspace_url}/api/2.0/workspace/list"
    headers = {"Authorization": f"Bearer {workspace_token}"}
    folders = []
    params = {"path": "/"}  
    while True:
        response = requests.get(list_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            for file in data.get("files", []):
                if file["is_dir"]:
                    folders.append(file["path"])
            if "next_page" in data:
                params["page_token"] = data["next_page"]
            else:
                break
        else:
            print(f"Error listing folders: {response.text}")
            break
    return folders

def zip_folders_and_notebooks(west_us_workspace_url, west_us_workspace_token, folders):
    zip_buffer = BytesIO()  
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for folder in folders:
            folder_url = f"{west_us_workspace_url}/api/2.0/workspace/list"
            params = {"path": folder}
            headers = {"Authorization": f"Bearer {west_us_workspace_token}"}
            
            response = requests.get(folder_url, headers=headers, params=params)
            
            if response.status_code == 200:
                files_data = response.json()
                for file in files_data.get("files", []):
                    file_path = file["path"]
                    if file["is_dir"]:  
                        continue
                    export_url = f"{west_us_workspace_url}/api/2.0/workspace/export"
                    export_params = {"path": file_path, "format": "SOURCE"}
                    export_response = requests.get(export_url, headers=headers, params=export_params)

                    if export_response.status_code == 200:
                        notebook_content = export_response.text
                        zip_file.writestr(file_path.strip('/'), notebook_content)
                    else:
                        print(f"Failed to export file {file_path}")
            else:
                print(f"Failed to list folder {folder}")
    zip_buffer.seek(0)  
    return zip_buffer

def upload_zip_to_west_us_2(zip_buffer, west_us_2_workspace_url, west_us_2_workspace_token, destination_folder):
    upload_url = f"{west_us_2_workspace_url}/api/2.0/workspace/import"
    headers = {"Authorization": f"Bearer {west_us_2_workspace_token}"}
    files = {
        "file": ("notebooks.zip", zip_buffer, "application/zip")
    }
    params = {
        "path": destination_folder,
        "overwrite": "true",
        "format": "SOURCE"
    }
    
    response = requests.post(upload_url, headers=headers, params=params, files=files)
    if response.status_code == 200:
        print(f"Zip file uploaded successfully to {destination_folder} in West US 2 workspace.")
    else:
        print(f"Failed to upload zip file to {destination_folder} in West US 2: {response.text}")

def unzip_in_west_us_2(zip_path, west_us_2_workspace_url, west_us_2_workspace_token):
    # Unzip the file on the workspace
    unzip_url = f"{west_us_2_workspace_url}/api/2.0/workspace/unzip"
    headers = {"Authorization": f"Bearer {west_us_2_workspace_token}"}
    params = {"path": zip_path}
    response = requests.post(unzip_url, headers=headers, params=params)

    if response.status_code == 200:
        print(f"Unzipped the file {zip_path} in West US 2 workspace successfully.")
    else:
        print(f"Failed to unzip the file {zip_path} in West US 2 workspace: {response.text}")

def migrate_all_folders(west_us_workspace_url, west_us_workspace_token, west_us_2_workspace_url, west_us_2_workspace_token):
    print("Listing all folders in West US workspace...")
    folders_to_migrate = list_workspace_folders(west_us_workspace_url, west_us_workspace_token)

    print("Zipping folders and notebooks...")
    zip_buffer = zip_folders_and_notebooks(west_us_workspace_url, west_us_workspace_token, folders_to_migrate)
    
    destination_folder = "/Workspace/migrated_notebooks"  
    print("Uploading zip file to West US 2 workspace...")
    upload_zip_to_west_us_2(zip_buffer, west_us_2_workspace_url, west_us_2_workspace_token, destination_folder)
    
    print("Unzipping the files in West US 2 workspace...")
    zip_path = f"{destination_folder}/notebooks.zip"
    unzip_in_west_us_2(zip_path, west_us_2_workspace_url, west_us_2_workspace_token)

