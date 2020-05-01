# Using Databricks For Covid-19 Analytics

## Databricks enables a wide range of analytics use cases for Covid-19.


## Assets

Azure Databricks ARM Template

Sample Notebooks Covering

*   Comparing IHME
*   Comparing 3 Day New Covid-19 Cases
*   Loading US Census and New York Times Covid Cases


## Setup
The ARM template can be used to provision a Databricks workspace. The parameters provided to the template are
*   Workspace Name
*   Virtual Network To Use

After the workspace is deployed either using the UI or the databricks cli the sample notebooks can be used to create and populate a set of base tables

## Use Cases

One use case is comparing IMHE models to actual data. The figure below is the IHME predictions made on April 1st compared with the reported deaths to April 18th.Using this view shows the initial model over predicted the number of deaths.

The next figure is the IHME predictions as of April 12th. In this model the predictions are accurate in the beginning but begin to under predict the number of deaths.
