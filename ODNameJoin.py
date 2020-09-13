# ODNameJoin.py Script

# Purpose:
# For the Origins
# Create a Full 9 digit ZIP4 code from separate fields in the Origin ZIP4 feature class attribute table
# Add this to the OD Matrix via joining on the OIDs
# For the Destinations add the SafeGraph ID via joining on the OIDs

# Import system modules
import arcpy

# Set the current workspace
arcpy.env.workspace = "c:/data/data.gdb"

# Set the local parameters
inFeatures = "zion_park"
joinField = "zonecode"
joinTable = "zion_zoning"
fieldList = ["land_use", "land_cover"]

# Join two feature classes by the zonecode field and only carry
# over the land use and land cover fields
arcpy.JoinField_management(inFeatures, joinField, joinTable, joinField,
                           fieldList)