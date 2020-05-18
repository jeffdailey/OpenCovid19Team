
**Web GIS**

Web GIS is a pattern or architectural approach for implementing a modern GIS powered by web services to manage COVID-19 pandemic in a community. Web GIS may be implemented in on your own infrastructure (using ArcGIS Enterprise). Web GIS reduces the need to create custom applications, provides a platform for integrating GIS with other business systems, and enables cross-organizational collaboration. It allows organizations to properly manage all their geographic knowledge. At the heart of Web GIS is a map-centric content management system.

Web GIS represents an opportunity to take the powerful tools leveraged by GIS practitioners and scale many of the capabilities in a simplified form out to the majority of the organization thus empowering staff to access data, perform analysis, visualize patterns, ask new questions, and see what others cannot. The Web GIS approach introduces many advantages over the traditional desktop environment such as increased number of users, better cross-platform capabilities, lower cost per user, ease of use, diverse applications, and a user-based experience. Many of the capabilities provided under this modern approach are introduced throughout this document along with technology requirements and reference resources.

A critical component of a Web GIS to be introduced is **identity**. Identity has become a key role within ArcGIS Enterprise just as identity has persisted throughout other key Enterprise systems. The use of identity is not unique to Esri&#39;s Location Platform. Identity has become a method to quickly and simply ensure the proper data, applications, editing environments, and information products are delivered to the intended users. Identity allows an organization to recognize the roles of staff within the organization, associate each role with access to data, apps, and tools as well as provide a user experience tailored to each identity.

Your identity (User Type) associates you with ArcGIS privileges no matter your location. Log in to any app, on any device, at any time, and have access to all the maps, apps, data, and analysis associated with your organizational role. Note: access is based on the assigned User Type. This identity model is similar to how identity functions across other familiar solutions such as Exchange, Salesforce, SharePoint, and SAP.

It is recommended to leverage the organization&#39;s existing identity store through integration of Active Directory (AD) for on-premise ArcGIS Portal deployment(s) and for ArcGIS Online via Enterprise Logins, which leverage Active Directory Federation Services (AD FS), a SAML 2.0 identity provider. Note: within ArcGIS Enterprise, Web GIS On-Premise, provides unlimited viewer type user roles (formerly known as level 1 named users).

**[ArcGIS](#TOC) Enterprise**

ArcGIS Enterprise, at a minimum, consists of a base deployment. This base deployment is the core of the Enterprise, and consists of two web adaptors, a Portal, a hosting server, and the relational data store. This base deployment provides the organization with a content management system, web maps, application creation and hosting, powerful but simplified analytical capabilities and much more. The data store is designed to provide output for analysis stored as simple web services without the overhead of more complex services requiring a map service. Web maps are the primary interface that allow users to discover data and build out maps that consist of web enabled data within the organization as well as Living Atlas content, if enabled. These web maps may be converted into Applications, Story Maps, and Operational Dashboards.

ArcGIS Enterprise is designed to scale horizontally as well as vertically with each server technology designated into functional roles that become federated into the base deployment to provide additional capabilities. If enterprise geodatabase data needs to be accessed within ArcGIS Enterprise a map server role should be considered to support these referenced data sources.

Portals: The **Portal** component organizes users and connects them with the appropriate content and capabilities based on their role and privileges within the platform. The portal uses a person&#39;s identity to deliver the right content to the right person at the right time. ArcGIS Enterprise (on your own infrastructure solution) and ArcGIS Online (a Software as a Service, cloud‐based solution) are both considered portals. These portals provide access control, content management, and a sharing model that enables users to share information products across the organization. Data that is intended to be shared with the public will be shared to a group that has collaboration configured. This will automate a copy of the data to ArcGIS Online.

ArcGIS Enterprise: [_Link_](http://www.esri.com/en/arcgis/products/arcgis-enterprise/overview)

![](RackMultipart20200513-4-1r756kj_html_e470e9a2b3a8779a.gif)

Product Page: [_Link_](http://www.esri.com/software/arcgis/arcgisserver/extensions/portal-for-arcgis)

Hardware Requirements: [_Link_](http://server.arcgis.com/en/portal/latest/administer/windows/portal-for-arcgis-system-requirements.htm#ESRI_SECTION1_80B50BEEF1CF42A99D8C164DAA51A3CE)

Federating ArcGIS Server: [_Link_](http://server.arcgis.com/en/portal/latest/administer/windows/federate-an-arcgis-server-site-with-your-portal.htm)

Ports used by Portal: [_Link_](http://server.arcgis.com/en/portal/latest/administer/windows/ports-used-by-portal-for-arcgis.htm)

Import a Certificate: [_Link_](http://server.arcgis.com/en/portal/latest/administer/windows/import-a-certificate-into-the-portal.htm)

Domain Certificates: [_Link_](http://server.arcgis.com/en/portal/latest/administer/windows/enable-https-on-your-web-server-portal-.htm)

Configuring AD FS: [_Link_](https://doc.arcgis.com/en/arcgis-online/reference/configure-adfs.htm)

**ArcGIS Enterprise on Microsoft Azure**

One of the three methods can be used to deploy ArcGIS Enterprise on Azure

1. [Esri Images in Azure Marketplace.](https://enterprise.arcgis.com/en/server/latest/cloud/azure/esri-images-on-azure-marketplace.htm)
2. [ArcGIS Azure ARM Template](https://github.com/Esri/arcgis-azure-templates)
3. [CloudBuilder – A custom UI to deploy ArcGIS in Azure](https://enterprise.arcgis.com/en/server/latest/cloud/azure/what-is-arcgis-server-cloud-builder-for-microsoft-azure.htm)

**Use Cases:**

Location information is critical to decision-making associated with large outbreaks.

Both the who and the when of disease are relative to and often dependent on the where. Geographic information science, systems, software (collectively known as GIS) and methods are one of the tools epidemiologists use in defining and evaluating the where.

The health-care community has long used maps to understand the spread of disease—initially in 1694 to communicate quarantine areas for bubonic plague and most famously in 1854, when Dr. John Snow connected location and illness with his history-making map of a London cholera outbreak. From disease atlases of the early 20th century to more recent web mapping of Ebola and Zika infections, health-care professionals have considered mapping—more recently done using GIS—a critical tool in tracking and combating contagion.

For example, GIS is critical to answering many infectious disease-related questions including the following:

- Where are current cases in the community; and where will the virus likely spread?
- Do we have schools in socially vulnerable areas?
- Which neighborhoods are distant from a testing site?
- Do we have communities or specific population demographics that are at greater risk?
- Which facilities and staff are in harm&#39;s way?
- What does surveillance data on the number of hospitalizations and deaths suggest regarding the following?
- Distribution of hospital supplies and hospital beds on a regional or statewide basis
- How quickly local and regional hospital resources are being depleted

While most public health organizations recognize the importance of location, location- based information is not always collected in routine public health practice. With the widespread implementation of electronic health records, the intrinsic value of a patient&#39;s address for public health reportable conditions should be recognized and preserved. Accurate geographic information should be embedded as part of any international, federal, state, or local health information system solution.

**Following are several examples of situations that highlight the need for location intelligence:**

- A disease outbreak has rapidly progressed to widespread status in a community, and public health officials can no longer hope to contain the outbreak through contact tracing and quarantine. A series of community-level interventions must now be evaluated and implemented to contain the outbreak. Location-based information can be used to support multiple, specific community interventions and activities. Common and helpful GIS applications include mapping and data collection apps to track cases, spread, vulnerable populations and places, and hospital capacity; dashboards for real-time situational awareness; and web apps for keeping the public informed. Health officials may overlay outbreak data with other location-based information such as public gathering places, schools, health facilities and services, and transportation centers. GIS supports possible interventions such as

- Sharing situational awareness to monitor and evaluate impact.
- Canceling public events, meetings, and gatherings.
- Closing schools, public places, and office buildings.
- Restricting use of public transportation systems.
- Identifying potential group quarantine and isolation facilities.
- Enforcing community or personal quarantines.

- International airline passengers are screened by public health officials at a large urban airport and asked to complete a standardized health status questionnaire and submit to temperature checks for fever. Passengers are asked to state both origin and destination addresses. Subsequently, a disease cluster is reported in another country, and public health officials need to identify how many people have traveled from or recently visited that same location. Using GIS, public health officials are able to apply the information collected in the questionnaire in their estimate of exposures and to prioritize investigations. A digital solution to capture the questionnaire data, including a standardized method to geographically reference each passenger&#39;s place of origin and travel destination, will save the public health community valuable time in understanding the transmission dynamics and potentially containing the outbreak.

- A patient seen in a hospital emergency room is tested for coronavirus, but the test ends up being a false negative. Days later, when the lab test results are confirmed to be positive, the public health agency is notified to investigate, only to discover that the patient&#39;s address is not valid, has been mistakenly recorded, or does not exist—and vital time is lost in locating the patient. GIS technology provides a mechanism for validating the address against an existing address database at the time it is recorded. GIS gives the ability to rapidly capture standardized and geocoded addresses for confirmed cases, suspected cases, and case contacts during the critical early phase of the pandemic period, providing essential support for attempts to slow the spread of disease throughout the community.

- The COVID-19 Modeling toolbox provides CHIME Model v1.1.2 and COVID-19Surge (CDC) tools for ArcGIS Pro 2.3 and later to assist hospitals, cities and regions with intervention and resource planning during the COVID-19 pandemic. Version 4 of the toolbox **introduces the new COVID-19Surge (CDC) tool**. &quot;[Understanding what it takes to flatten the curve](https://www.esri.com/arcgis-blog/products/arcgis-pro/analytics/understanding-what-it-takes-to-flatten-the-curve/)&quot; provides more insight to use the tools.

