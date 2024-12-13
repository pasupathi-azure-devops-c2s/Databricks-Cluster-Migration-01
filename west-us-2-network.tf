resource "azurerm_virtual_network" "westus2-vnet" {
    name = "Databricks-West-US-2-VNet-01"
    resource_group_name = azurerm_resource_group.west-us-2-rg.name
    location = azurerm_resource_group.west-us-2-rg.location
    address_space = [ "10.0.0.0/16" ]
  
}

resource "azurerm_subnet" "westus-2-subnet-1" {
    name = "West-US-2-Subnet-1"
    resource_group_name = azurerm_resource_group.west-us-2-rg.name
    virtual_network_name = azurerm_virtual_network.westus2-vnet.name
    address_prefixes = [ "10.0.0.0/24" ]
  
}

resource "azurerm_network_security_group" "west-us-2-nsg" {
    name = "West-US-2-NSG-01"
    resource_group_name = azurerm_resource_group.west-us-2-rg.name
    location = azurerm_resource_group.west-us-2-rg.location
  
}

resource "azurerm_subnet_network_security_group_association" "west-us-2-network-associate" {
    subnet_id = azurerm_subnet.westus-2-subnet-1.id
    network_security_group_id = azurerm_network_security_group.west-us-2-nsg.id
  
}