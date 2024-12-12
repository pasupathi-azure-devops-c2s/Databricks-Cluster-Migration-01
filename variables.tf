variable "databricks-cluster-name" {
    type = string
    description = "Provide the Given Databricks Cluster Name: "
}

variable "west-us-resource-group-name" {
    type = string
    description = "Provide the Given Resource Group Name: "
  
}

variable "west-us-2-resource-group-name" {
    type = string
    description = "Provide the Given Resource Group Name: "
  
}

variable "vnet-address-space" {
    type = string
    description = "Provide the VNET Address Space: "
  
}

variable "storage-account-name" {
    type = string
    description = "Provide the Storage Account Name: "
  
}

variable "blob-contianer-name" {
    type = string
    description = "Provide the Storage Blob Container Name: "
  
}

variable "databricks-workspace-name-west-us" {
    type = string
    description = "Provide the Databricks Workspace Name for West US Region: "
  
}

variable "databricks-workspace-name-west-us-2" {
    type = string
    description = "Provide the Databricks Workspace Name for West US 2 Region: "
  
}
variable "databricks-subent-cidr" {
    type = string
    description = "Provide the Given Subnet 1 CIDR Range: "
  
}