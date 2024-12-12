resource "azurerm_virtual_network" "databricks-vnet" {
    name = "Databricks-West-US-VNet-01"
    location = azurerm_resource_group.west-us-databricks-rg.location
    resource_group_name = azurerm_resource_group.west-us-databricks-rg.name
    address_space = [ var.vnet-address-space ]
  
}

resource "azurerm_subnet" "databricks-subnet" {
    name = "Databricks-West-US-Subnet-01"
    virtual_network_name = azurerm_virtual_network.databricks-vnet.name
    resource_group_name = azurerm_resource_group.west-us-databricks-rg.name
    address_prefixes = [ var.databricks-subent-cidr ]
  
}

resource "azurerm_network_security_group" "databricks-nsg" {
    name = "Databricks-NSG-West-US"
    resource_group_name = azurerm_resource_group.west-us-databricks-rg.name
    location = azurerm_resource_group.west-us-databricks-rg.location
  
}

resource "azurerm_subnet_network_security_group_association" "subent-nsg-associate" {
    subnet_id = azurerm_subnet.databricks-subnet.id
    network_security_group_id = azurerm_network_security_group.databricks-nsg.id
  
}