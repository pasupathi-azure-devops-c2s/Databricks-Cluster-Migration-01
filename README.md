Certainly! Below is a professionally formatted version of your README content:

---

# Databricks Cluster Migration

This repository provides the necessary files to automate the migration of Databricks clusters from a workspace in the "West US" region to a workspace in the "West US 2" region. It includes two main components: 

1. **Terraform code** to provision Databricks workspaces in both regions (West US and West US 2) and create a Databricks cluster in the West US region.
2. **Python scripts** to collect cluster details from the West US Databricks workspace and replicate the same cluster configurations in the West US 2 region.

## Pre-requisites

- **Azure Key Vault** to store the Databricks workspace URLs and tokens securely.
- **Terraform** to provision the infrastructure.
- **Python** environment for running the cluster migration scripts.

## Project Structure

- `terraform/` - Contains Terraform configuration files to provision the Databricks workspaces and clusters.
- `python/` - Contains Python scripts for collecting cluster details and replicating them in another region.

## Setup and Configuration

### Terraform Configuration

The Terraform configuration allows you to provision the necessary Databricks workspaces in both the West US and West US 2 regions. Additionally, it provisions a Databricks cluster in the West US region.

#### Terraform Steps

1. **Initialize Terraform**  
   Run the following command to initialize Terraform in your working directory:
   ```bash
   terraform init
   ```

2. **Apply the Terraform configuration**  
   Execute the following command to provision the resources:
   ```bash
   terraform apply --auto-approve
   ```

   This will create the Databricks workspaces and the Databricks cluster in the West US region.

### Python Scripts

Once the Databricks workspaces are provisioned, you can use the Python scripts to gather cluster details from the West US region and replicate them in the West US 2 region.

#### Python Script Steps

1. **Generate Developer Access Tokens**  
   After provisioning the Databricks workspaces in both regions, log in to each workspace using the Launch button on the Databricks UI. 
   - Navigate to **User Settings** and generate a **Personal Access Token** for both the West US and West US 2 workspaces.
   - Store the access tokens and workspace URLs securely (preferably in Azure Key Vault).

2. **Collect Cluster Details from West US**  
   Run the `source_cluster_details_collection.py` script to collect the details of all clusters in the West US region. This script will generate a JSON file containing information such as cluster names, cluster IDs, and other relevant details.

   ```bash
   python source_cluster_details_collection.py
   ```

3. **Modify the JSON File**  
   After collecting the cluster details, open the generated JSON file and extract the cluster IDs. These IDs should be formatted in a list, like so:

   ```json
   ["cluster-id-1", "cluster-id-2", "cluster-id-3"]
   ```

4. **Create Clusters in West US 2**  
   Run the `destination_cluster_creation.py` script, passing the list of cluster IDs from the JSON file as input. This script will replicate the clusters in the West US 2 Databricks workspace.

   ```bash
   python destination_cluster_creation.py --cluster_ids ["cluster-id-1", "cluster-id-2", "cluster-id-3"]
   ```

   This will create the same clusters in the West US 2 region with similar configurations.

## Configuration Details

### Key Vault Configuration

To securely store your Databricks workspace URLs and tokens, make sure to configure an Azure Key Vault. Store the following items in your Key Vault:

- `WEST_US_WORKSPACE_URL` - The URL of the Databricks workspace in the West US region.
- `WEST_US_TOKEN` - The Personal Access Token for the Databricks workspace in the West US region.
- `WEST_US_2_WORKSPACE_URL` - The URL of the Databricks workspace in the West US 2 region.
- `WEST_US_2_TOKEN` - The Personal Access Token for the Databricks workspace in the West US 2 region.

Ensure that the Python scripts can access these values from the Key Vault for seamless operation.

## Additional Notes

- Ensure that you have the necessary permissions to create and manage Databricks resources and access the Key Vault.
- The Terraform code assumes that the Databricks provider is configured correctly in your environment. Make sure to set up the required Azure credentials if necessary.

## Troubleshooting

- If you encounter issues with cluster creation, verify the cluster configurations in the JSON file and ensure that the cluster IDs are correct.
- If Terraform fails to apply the changes, check the logs for any missing or invalid configurations, and make sure your Azure credentials are correctly set up.

---

By following these steps, you should be able to migrate Databricks clusters from one region to another using this automated process.