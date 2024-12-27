import json
import requests
import time
from databricks_workspace_file_collection import list_workspace_files


# West US Workspace and Cluster details (Source Workspace and Cluster Details)
west_us_workspace_url = "<West-US-Workspace-URL>"
west_us_workspace_token = "<West-US-Workspace-Developer-Access-Token>"
west_us_cluster_id = "<Databricks-Cluster-ID>"



# West US 2 Workspace details (Destination Workspace details)
west_us_2_workspace_url = "<West-US-2-Workspace-URL>"
west_us_2_workspace_token = "<West-US-2-Workspace-Developer-Access-Token>"


west_us_cluster_url = f"{west_us_workspace_url}/api/2.0/clusters/get"
workspace_path = "/Workspace"

account_url = "<storage-account-url>" 
sas_token = "<blob-sas-token>"



container_name = "<container-name>"  
blob_name = "<blob-name>"     
file_path = "<file-path>"  


west_us_header = {
    "Authorization": f"Bearer {west_us_workspace_token}"
}

west_us_response = requests.get(west_us_cluster_url, headers=west_us_header, json={"cluster_id": west_us_cluster_id})

if west_us_response.status_code == 200:
    cluster_data = west_us_response.json()
    cluster_config = {
        "cluster_name": cluster_data.get("cluster_name"),
        "spark_version": cluster_data.get("spark_version"),
        "node_type_id": cluster_data.get("node_type_id"),
        "num_workers": cluster_data.get("num_workers"),
        "autotermination_minutes": cluster_data.get("autotermination_minutes"),
        "driver_node_type_id": cluster_data.get("driver_node_type_id"),
        "enable_elastic_disk": cluster_data.get("enable_elastic_disk"),
        "autoscale": cluster_data.get("autoscale")
    }

    west_us_2_header = {
        "Authorization": f"Bearer {west_us_2_workspace_token}",
        "Content-Type": "application/json"
    }

    create_cluster_url = f"{west_us_2_workspace_url}/api/2.0/clusters/create"

    create_response = requests.post(create_cluster_url, headers=west_us_2_header, json=cluster_config)

    if create_response.status_code == 200:
        print("Cluster created successfully in West US 2 workspace!")
        list_workspace_files(workspace_path, west_us_2_workspace_url, west_us_2_workspace_token, account_url, sas_token, container_name, blob_name)
    else:
        print(f"Failed to create cluster in West US 2: {create_response.text}")
else:
    print(f"Failed to fetch cluster details from West US workspace: {west_us_response.text}")