resource "azurerm_virtual_network" "databricks-vnet" {
    name = "Databricks-West-US-VNet-01"
    location = azurerm_resource_group.west-us-databricks-rg.location
    resource_group_name = azurerm_resource_group.west-us-databricks-rg.name
    address_space = [ var.vnet-address-space ]
  
}