import json
import requests
import time

# West US Workspace and Cluster details (Source Workspace and Cluster Details)
west_us_workspace_url = "<West-US-Workspace-URL>"
west_us_workspace_token = "<West-US-Workspace-Developer-Access-Token>"
west_us_cluster_id = "<Databricks-Cluster-ID>"

# West US 2 Workspace details (Destination Workspace details)
west_us_2_workspace_url = "<West-US-2-Workspace-URL>"
west_us_2_workspace_token = "<West-US-2-Workspace-Developer-Access-Token>"

# Cluster details URL for West US Workspace
west_us_cluster_url = f"{west_us_workspace_url}/api/2.0/clusters/get"

west_us_header = {
    "Authorization": f"Bearer {west_us_workspace_token}"
}

# Get cluster details from the West US workspace
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

    # Create the cluster in the West US 2 workspace
    west_us_2_header = {
        "Authorization": f"Bearer {west_us_2_workspace_token}",
        "Content-Type": "application/json"
    }

    create_cluster_url = f"{west_us_2_workspace_url}/api/2.0/clusters/create"
    create_response = requests.post(create_cluster_url, headers=west_us_2_header, json=cluster_config)

    if create_response.status_code == 200:
        print("Cluster created successfully in West US 2 workspace!")

        # Wait for the cluster to be running before installing libraries or running jobs
        cluster_id = create_response.json().get("cluster_id")

        # Wait for the cluster to be in a running state
        while True:
            cluster_status_url = f"{west_us_2_workspace_url}/api/2.0/clusters/get?cluster_id={cluster_id}"
            cluster_status_response = requests.get(cluster_status_url, headers=west_us_2_header)

            if cluster_status_response.status_code == 200:
                cluster_status_data = cluster_status_response.json()
                state = cluster_status_data.get("state")

                if state == "RUNNING":
                    print("Cluster is running.")
                    break
                else:
                    print(f"Cluster is in {state} state. Waiting for it to be running...")
            else:
                print(f"Failed to fetch cluster status: {cluster_status_response.text}")
                break

            time.sleep(30)  # Wait for 30 seconds before checking again

        # Step 1: Install libraries on the cluster
        install_libraries_url = f"{west_us_2_workspace_url}/api/2.0/libraries/install"
        libraries = [
            {
                "pypi": {
                    "package": "pandas",
                    "repo": "https://pypi.org/simple/"
                }
            },
            {
                "pypi": {
                    "package": "numpy",
                    "repo": "https://pypi.org/simple/"
                }
            }
            # Add more libraries as required
        ]

        install_libraries_payload = {
            "cluster_id": cluster_id,
            "libraries": libraries
        }

        install_libraries_response = requests.post(install_libraries_url, headers=west_us_2_header, json=install_libraries_payload)

        if install_libraries_response.status_code == 200:
            print("Libraries installed successfully.")
        else:
            print(f"Failed to install libraries: {install_libraries_response.text}")

        # Step 2: Run jobs on the cluster
        job_payload = {
            "run_name": "Example Job",
            "existing_cluster_id": cluster_id,
            "notebook_task": {
                "notebook_path": "/Users/<your_username>/example_notebook"  # Replace with your notebook path
            }
        }

        run_job_url = f"{west_us_2_workspace_url}/api/2.0/jobs/runs/submit"
        run_job_response = requests.post(run_job_url, headers=west_us_2_header, json=job_payload)

        if run_job_response.status_code == 200:
            print("Job submitted successfully.")
        else:
            print(f"Failed to submit job: {run_job_response.text}")

    else:
        print(f"Failed to create cluster in West US 2: {create_response.text}")
else:
    print(f"Failed to fetch cluster details from West US workspace: {west_us_response.text}")
