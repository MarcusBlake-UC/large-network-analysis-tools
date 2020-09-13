# Name: CreateFeatureDataset.py
# Description: Create a feature dataset using a spatial reference object

# Import system modules
import arcpy

# Set local variables
out_dataset_path = r"C:\ResearchProjects\HMSUC\Code\OD_DataPrep\Output\OhioZIP4byCounty.gdb"
out_dataset_name = "POI_PHDR_4269"

# Creating a spatial reference object
#sr = arcpy.SpatialReference(r"C:\ResearchProjects\HMSUC\Code\OD_DataPrep\Output\OhioZIP4byCounty.gdb\OH_PHDR_446110_39001")
# This fails with "RuntimeError: ERROR 999999: Something unexpected caused the tool to fail.
# Contact Esri Technical Support (http://esriurl.com/support) to Report a Bug,
# and refer to the error help for potential solutions or workarounds.
# Class not registered"


# String below is representation for the
# Geographic Coordinate system "WGS 1984" (factory code=4326)
#wkt = "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',\
#        SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],AUTHORITY['EPSG',4269]]"
#sr = arcpy.SpatialReference()
#sr.loadFromString(wkt)

sr = arcpy.SpatialReference(4269)


print(sr.GCSName, sr.GCSCode)

# Execute CreateFeaturedataset
#try:
arcpy.CreateFeatureDataset_management(out_dataset_path, out_dataset_name, sr)
#except:
#    print('The dataset name probably already exists')