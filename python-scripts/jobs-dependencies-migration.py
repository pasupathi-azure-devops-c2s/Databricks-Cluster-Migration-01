import requests
import json


# West US and West US 2 Workspace Details
west_us_workspace_url = "<West-US-Workspace-URL>"
west_us_workspace_token = "<West-US-Workspace-Developer-Access-Token>"
west_us_2_workspace_url = "<West-US-2-Workspace-URL>"
west_us_2_workspace_token = "<West-US-2-Workspace-Developer-Access-Token>"

def migrate_notebooks():
    notebooks_url = f"{west_us_workspace_url}/api/2.0/workspace/list"
    west_us_header = {"Authorization": f"Bearer {west_us_workspace_token}"}
    notebooks_response = requests.get(notebooks_url, headers=west_us_header)

    if notebooks_response.status_code == 200:
        notebooks_data = notebooks_response.json()

        for notebook in notebooks_data.get("files", []):
            notebook_path = notebook["path"]
   
            export_url = f"{west_us_workspace_url}/api/2.0/workspace/export"
            export_params = {"path": notebook_path, "format": "SOURCE"}
            export_response = requests.get(export_url, headers=west_us_header, params=export_params)

            if export_response.status_code == 200:
                notebook_content = export_response.text
   
                import_url = f"{west_us_2_workspace_url}/api/2.0/workspace/import"
                import_params = {
                    "path": notebook_path,
                    "format": "SOURCE",  # Could be SOURCE or JUPYTER depending on your need
                    "overwrite": "true"
                }
                import_response = requests.post(import_url, headers={"Authorization": f"Bearer {west_us_2_workspace_token}"}, params=import_params, data=notebook_content)

                if import_response.status_code == 200:
                    print(f"Notebook {notebook_path} successfully migrated to West US 2.")
                else:
                    print(f"Failed to import notebook {notebook_path} to West US 2.")
            else:
                print(f"Failed to export notebook {notebook_path} from West US.")
    else:
        print("Failed to retrieve notebooks from West US.")

def migrate_jobs():
    jobs_url = f"{west_us_workspace_url}/api/2.0/jobs/list"
    jobs_response = requests.get(jobs_url, headers={"Authorization": f"Bearer {west_us_workspace_token}"})

    if jobs_response.status_code == 200:
        jobs_data = jobs_response.json()

        for job in jobs_data.get("jobs", []):
            job_id = job["job_id"]
            job_settings_url = f"{west_us_workspace_url}/api/2.0/jobs/get?job_id={job_id}"
            job_settings_response = requests.get(job_settings_url, headers={"Authorization": f"Bearer {west_us_workspace_token}"})

            if job_settings_response.status_code == 200:
                job_settings = job_settings_response.json()
                
                job_payload = {
                    "run_name": job_settings["settings"]["name"],  # Job name
                    "existing_cluster_id": "<West-US-2-Cluster-ID>",  # Use the West US 2 cluster ID
                    "notebook_task": job_settings["settings"].get("notebook_task", {}),
                    "spark_jar_task": job_settings["settings"].get("spark_jar_task", {}),
                    "spark_python_task": job_settings["settings"].get("spark_python_task", {})
                }

                run_job_url = f"{west_us_2_workspace_url}/api/2.0/jobs/runs/submit"
                run_job_response = requests.post(run_job_url, headers={"Authorization": f"Bearer {west_us_2_workspace_token}"}, json=job_payload)

                if run_job_response.status_code == 200:
                    print(f"Job {job_settings['settings']['name']} successfully migrated to West US 2.")
                else:
                    print(f"Failed to submit job {job_settings['settings']['name']} to West US 2.")
            else:
                print(f"Failed to get job {job_id} details from West US.")
    else:
        print("Failed to retrieve jobs from West US.")

migrate_notebooks()
migrate_jobs()
