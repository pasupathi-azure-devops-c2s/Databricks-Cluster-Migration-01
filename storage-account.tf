/*resource "azurerm_storage_account" "databricks-storage-account" {
    name = var.storage-account-name
    resource_group_name = azurerm_resource_group.west-us-databricks-rg.name
    location = azurerm_resource_group.west-us-databricks-rg.location
    account_tier = "Standard"
    account_replication_type = "GRS"
  
}

resource "azurerm_storage_container" "databricks-blob" {
    name = var.blob-contianer-name
    storage_account_id = azurerm_storage_account.databricks-storage-account.id
    container_access_type = "private"
  
}
*/