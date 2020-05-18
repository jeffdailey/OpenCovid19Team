# Using Databricks For Covid-19 Analytics

## Databricks enables a wide range of analytics use cases for Covid-19.


## Assets

Azure Databricks ARM Template

Sample Notebooks Covering

*   Comparing IHME Models
*   Comparing 3 Day New Covid-19 Cases
*   Loading US Census and New York Times Covid Cases


## Setup
The ARM template can be used to provision a Databricks workspace. The parameters provided to the template are
*   Workspace Name
*   Virtual Network (Either VNET Injection Or Have ARM Create VNET)
*   Storage Account For ADLS Gen2
*   Azure Active Directory Service Principal (SP)

### Storage Account & Service Principal
Create a Storage Account and ADLS Gen2 Filesystem. Hierarchical namespace needs to be enabled and hot is the recommended performance tier.
The SP needs to have Storage Blob Contributor role to the Storage Account. Full documentation can be found at https://docs.databricks.com/data/data-sources/azure/azure-datalake-gen2.html

### ARM Deployment
Sample Command To Deploy Workspace

az group deployment create --name deploy_databricks --subscription <SUBSCRIPTION ID> --resource-group <EXISTING RG> --template-file azuredeploy.json --parameters nsgName="<nsg to create>" vnetName="<VNET to create>" workspaceName="<workspace name>" privateSubnetName="<subnet to create>" publicSubnetName="<subnet to create>" location="<Azure Region To Deploy In>"

After the workspace is deployed either using the UI or the databricks cli the sample notebooks can be used to create and populate a set of base tables

### Creating Tables
There are a few tables that need to be created. The tables are Delta tables and relay on Azure Data Lake Storage Gen2 (ADLS). 

### Schedule Jobs
In the main folder where all the notebooks were imported there is a Data Loads folder. Inside there is a NYTimes notebook. This nootebook should be scheduled to run everyday around noon to update the NY Times Covid Data

## Use Cases

One use case is comparing IMHE models to actual data. The figure below is the IHME predictions made on April 1st compared with the reported deaths to April 18th.Using this view shows the initial model over predicted the number of deaths.

The next figure is the IHME predictions as of April 12th. In this model the predictions are accurate in the beginning but begin to under predict the number of deaths.
