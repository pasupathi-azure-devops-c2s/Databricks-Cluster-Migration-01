resource "azurerm_resource_group" "west-us-2-rg" {
    name = var.west-us-2-resource-group-name
    location = "westus2"
  
}

resource "azurerm_databricks_workspace" "west-us-2-workspace" {
    name = var.databricks-workspace-name-west-us-2
    location = azurerm_resource_group.west-us-2-rg.location
    resource_group_name = azurerm_resource_group.west-us-2-rg.name
    sku = "Standard"
  
}