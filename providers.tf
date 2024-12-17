terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"  # Adjust this version as needed
    }
    databricks = {
            source = "databrickslabs/databricks"
            version = "0.3.1"
        }
  }

  required_version = ">= 1.0"
}


provider "azurerm" {
  features {}
}

provider "databricks" {
    azure_workspace_resource_id  = azurerm_databricks_workspace.databricks-workspace-west-us.id
}