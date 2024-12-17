resource "azurerm_resource_group" "west-us-databricks-rg" {
  name     = var.west-us-resource-group-name
  location = "West US"
}

resource "azurerm_databricks_workspace" "databricks-workspace-west-us" {
  name                = var.databricks-workspace-name-west-us
  resource_group_name = azurerm_resource_group.west-us-databricks-rg.name
  location            = azurerm_resource_group.west-us-databricks-rg.location
  sku                 = "standard"

  tags = {
    Environment = "Production"
  }
}

resource "databricks_cluster" "westus-cluster-01" {
  cluster_name = "Sample-Cluster-01"
  spark_version = data.databricks_spark_version.latest_lts.id
  node_type_id = data.databricks_node_type.smallest.id
  autotermination_minutes = 20

  autoscale {
    min_workers = 1
    max_workers = 25
  }
  
}