terraform {
  required_providers {
    databricks = {
      source = "databricks/databricks"
      version = "0.3.7"  # Specify the version
    }
  }
}
provider "azurerm"{
    features{}
}