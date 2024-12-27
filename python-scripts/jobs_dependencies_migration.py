import requests
import json



def migrate_jobs(west_us_workspace_url, west_us_workspace_token, west_us_2_workspace_url, west_us_2_workspace_token):
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

migrate_jobs()
