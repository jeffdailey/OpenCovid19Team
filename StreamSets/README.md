Using Streamsets For Covid-19 Analytics

Assets
Azure Databricks ARM Template
Azure CLI deployment
Streamsets Pipelines



# Connect to Azure Gov via CLI
az cloud set --name AzureUSGovernment
az login -u youruser@covidtaskforce.onmicrosoft.us -p changeit123!

# Create Streamsets Resource Group
az group create --name $resourceGroup --location "USGov Virginia"

# Create a deployment from Streamsets ARM template via CLI
az group deployment create --resource-group streamsets --template-file azure/deployments/template.json
