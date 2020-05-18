Here is information on populating the geometry columns in postgres.

Postgres has functions to populate the geometry type. The most popular geometry types used are point, lines and polygons which we will be using in this project as well. Points represent locations on the surface of the earth(eg: addresses of places) and have a latitude and longitude value associated with it. Lines are your roads, rivers, etc and polygons are boundaries.  There is an important concept called spatial reference when it comes to spatial data which helps describe where features are located in the real world. There are many Spatial references and it is important to provide the correct spatial reference (SRID)when populating the geometry field.  [This documentation](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdevelopers.arcgis.com%2Fdocumentation%2Fcore-concepts%2Fspatial-references%2F&amp;data=02%7C01%7CLetitia.Larry%40microsoft.com%7C1317cc824e1c45dd43e908d7dcbbc010%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637220571269395038&amp;sdata=UFmK5R9aoeGxebeEXGu6UbauF4iiBjYagfIdJuostSU%3D&amp;reserved=0) will help you understand spatial reference. Most times this SRID can be obtained from the metadata of the data source.

To populate point geometry from latitude and longitude, you could use the postgres functions ST\_SetSrid and ST\_MakePoint. Example: if you have columns x, y in your data, you can update your table using a query as such:

UPDATE table SET geometry=ST\_SetSRID(ST\_MakePoint(x, y), 4326);

4326 is the SRID here.

For polygon geometry such as county boundaries, you may need to use a process to bring in the boundaries into postgres and then join the attribute table with the spatial data. The spatial data(shapefiles) can  imported into postgres [using the UI](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fpostgis.net%2Fworkshops%2Fpostgis-intro%2Floading_data.html&amp;data=02%7C01%7CLetitia.Larry%40microsoft.com%7C1317cc824e1c45dd43e908d7dcbbc010%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637220571269395038&amp;sdata=6%2BIdnUaQ0tCbST%2BR9TxhNZ4s1wYiFhJP7iuApYc8Tmg%3D&amp;reserved=0). When you import a shapefile it is important to specify the SRID. Shapefiles for regular administrative boundaries are available from the census website.

To populate the geometry field in postgres, a trigger can be used to calculate the geometry. In the following example a table called &quot;esri\_user\_location&quot; is created. Then a function called build\_geometry is called in the trigger before inserting a row.

**-- Table: public.esri\_user\_location**

-- DROP TABLE public.esri\_user\_location;

CREATE TABLE public.esri\_user\_location

(

    &quot;ID&quot; numeric NOT NULL,

    &quot;Name&quot; character varying(50) COLLATE pg\_catalog.&quot;default&quot;,

    x numeric,

    y numeric,

    geom geometry,

    CONSTRAINT esri\_user\_location\_pkey PRIMARY KEY (&quot;ID&quot;)

)

WITH (

    OIDS = FALSE

)

TABLESPACE pg\_default;

ALTER TABLE public.esri\_user\_location

    OWNER to covida;

**-- Trigger: build\_geometry**

-- DROP TRIGGER build\_geometry ON public.esri\_user\_location;

CREATE TRIGGER build\_geometry

    BEFORE INSERT

    ON public.esri\_user\_location

    FOR EACH ROW

    EXECUTE PROCEDURE public.build\_geometry();

**-- FUNCTION: public.build\_geometry()**

 -- DROP FUNCTION public.build\_geometry();

CREATE FUNCTION public.build\_geometry()

    RETURNS trigger

    LANGUAGE &#39;plpgsql&#39;

    COST 100

    VOLATILE NOT LEAKPROOF

AS $BODY$ BEGIN

NEW.geom = ST\_SetSRID(ST\_MakePoint(NEW.x,NEW.y),4326);

RETURN NEW;

END;

$BODY$;

ALTER FUNCTION public.build\_geometry()

    OWNER TO covida;
