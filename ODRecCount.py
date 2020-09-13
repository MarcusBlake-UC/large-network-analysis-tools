# ODNameJoin.py Script

# Purpose:
# Count the number of Origins and Destination records within a set of Feature Class stored within a feature Dataset

# References

# https://pro.arcgis.com/en/pro-app/arcpy/functions/listdatasets.htm"

# Import system modules
import arcpy
import os

# Set the current workspace
ws = arcpy.env.workspace = r"C:\ResearchProjects\HMSUC\Code\OD_DataPrep\Output\OhioZIP4byCounty.gdb"

dslist = arcpy.ListDatasets("*")

for ds in dslist:
    print(ds)

    # Set the local parameters
    #FeatureDataset = os.path.join(ws, ds)

    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        count = arcpy.GetCount_management(fc)
        print(fc, count)