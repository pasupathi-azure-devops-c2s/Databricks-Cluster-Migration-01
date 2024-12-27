import requests
import json

workspace_url = "<West-US-Workspace-URL>"
token = "<West-US-Workspace-Developer-Access-Token>"

headers = {
    "Authorization": f"Bearer {token}"
}

url = f"{workspace_url}/api/2.0/clusters/list"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    clusters = response.json().get("clusters", [])
    for cluster in clusters:
        print(f"Cluster Name: {cluster['cluster_name']}, Cluster ID: {cluster['cluster_id']}")

    with open('cluster-details.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)

else:
    print(f"Error: {response.status_code}, {response.text}")
