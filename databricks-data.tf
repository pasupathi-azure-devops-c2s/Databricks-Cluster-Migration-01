data "databricks_node_type" "smallest" {
  depends_on = [ azurerm_databricks_workspace.databricks-workspace-west-us, azurerm_databricks_workspace.west-us-2-workspace ]
  local_disk = true
}

data "databricks_spark_version" "latest_lts" {
  depends_on = [ azurerm_databricks_workspace.databricks-workspace-west-us, azurerm_databricks_workspace.west-us-2-workspace ]
  long_term_support = true
}