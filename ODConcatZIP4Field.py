# ODConcatZIP4Field.py Script

# Purpose:
# Concatenate the ZIP and PLUS4 Fields in each of the Ohio County Origins feature classes

# References
# https://pro.arcgis.com/en/pro-app/tool-reference/environment-settings/current-workspace.htm

# https://pro.arcgis.com/en/pro-app/tool-reference/data-management/add-field.htm

# https://pro.arcgis.com/en/pro-app/arcpy/functions/listfields.htm

# https://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field-examples.htm

# https://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field.htm

# Import system modules
import arcpy
import os

# Set the current workspace and single data set
ws = arcpy.env.workspace = r"D:\ArcGISProjects\ODCMTesting\OCDMOhioData.gdb"
ds = 'OhioCountyZIP4PnP_ESPG102723'

# Iterate over Datasets
#for ds in arcpy.ListDatasets("*","FEATURE"):
#    print(ds)

# For every feature class in the data set
for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
    count = arcpy.GetCount_management(fc)
    print(fc, count)

    # Make a list of field names from the ListFields object. Name is one of many attributes of the object
    FieldNameList = []
    for field in arcpy.ListFields(fc):
        FieldNameList.append(field.name)

    if "ZIPPLUS4" not in FieldNameList:
        arcpy.AddField_management(fc, "ZIPPLUS4", "TEXT", field_length="9")
    Else: \
        arcpy.CalculateField_management(fc, "ZIPPLUS4", 'str(!ZIP!) + str(!PLUS4!)', "PYTHON3")

    # {}{}.format(str(!ZIP!), str(!PLUS4!)) alternative?
    # str() to force casting to string
