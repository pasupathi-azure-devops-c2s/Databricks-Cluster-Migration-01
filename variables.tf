variable "west-us-resource-group-name" {
  type        = string
  description = "Provide the Given Resource Group Name: "
  default     = "Databricks-Cluster-West-us-Pasupathikumar"
}

variable "west-us-2-resource-group-name" {
  type        = string
  description = "Provide the Given Resource Group Name: "
  default     = "Databricks-Cluster-West-us-2-Pasupathikumar"
}

variable "vnet-address-space" {
  type        = string
  description = "Provide the VNET Address Space: "
  default     = "10.0.0.0/16"
}

variable "storage-account-name" {
  type        = string
  description = "Provide the Storage Account Name: "
  default     = "databricks01sa"
}

variable "blob-container-name" {
  type        = string
  description = "Provide the Storage Blob Container Name: "
  default     = "databricks-container"
}

variable "databricks-workspace-name-west-us" {
  type        = string
  description = "Provide the Databricks Workspace Name for West US Region: "
  default     = "Databricks-workspace-west-us-01"
}

variable "databricks-workspace-name-west-us-2" {
  type        = string
  description = "Provide the Databricks Workspace Name for West US 2 Region: "
  default     = "databricks-workspace-west-us-2"
}

variable "databricks-subnet-cidr" {
  type        = string
  description = "Provide the Given Subnet 1 CIDR Range: "
  default     = "10.0.0.0/24"
}