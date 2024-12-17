import requests
import json

# Replace with your Databricks workspace URL and your generated token
workspace_url = "<West-US-Workspace-URL>"
token = "<West-US-Workspace-Developer-Access-Token>"

# Set up the headers for authentication
headers = {
    "Authorization": f"Bearer {token}"
}

# Define the API endpoint to list clusters
url = f"{workspace_url}/api/2.0/clusters/list"

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    clusters = response.json().get("clusters", [])
    for cluster in clusters:
        print(f"Cluster Name: {cluster['cluster_name']}, Cluster ID: {cluster['cluster_id']}")

    # Save the response JSON to a file
    with open('cluster-details.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)

else:
    print(f"Error: {response.status_code}, {response.text}")
