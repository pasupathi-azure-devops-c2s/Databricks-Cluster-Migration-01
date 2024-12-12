resource "azurerm_resource_group" "west-us-databricks-rg" {
    name = var.west-us-resource-group-name
    location = "West US"
  
}


resource "azurerm_databricks_workspace" "databricks-workspace-west-us" {
    name = var.databricks-workspace-name-west-us
    resource_group_name = azurerm_resource_group.west-us-databricks-rg.name
    location = azurerm_resource_group.west-us-databricks-rg.location
    sku = "Standard"

    network_security_group_rules_required = azurerm_network_security_group.databricks-nsg.id

    tags = {
      Environment = "Production"
    }
  
}


