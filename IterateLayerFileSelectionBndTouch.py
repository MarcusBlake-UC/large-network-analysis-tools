########################################################################################################################
#    Program: IterateLayerFileSelectionBndTouch.py                                                                     #
#    Program Description: Iterate through each Ohio Counties selecting POIs within                                     #
#                                                                                                                      #
#    Author: Marcus.Blake@canberra.edu.au                                                                              #
#    Date: 23/08/2020                                                                                                  #
#                                                                                                                      #
#    References                                                                                                        #
#    https://pro.arcgis.com/en/pro-app/tool-reference/data-management/project.htm                                      #
#    https://pro.arcgis.com/en/pro-app/tool-reference/data-management/make-feature-layer.htm                           #
#    https://pro.arcgis.com/en/pro-app/tool-reference/data-management/select-layer-by-location.htm                     #
#    https://pro.arcgis.com/en/pro-app/tool-reference/data-management/make-feature-layer.htm                           #
#    https://pro.arcgis.com/en/pro-app/tool-reference/conversion/feature-class-to-geodatabase.htm                      #
#                                                                                                                      #
#                                                                                                                      #
#                                                                                                                      #


# This is an arcpy Python script that iterates through OH ZIP4 code points saving each County

if __name__ == '__main__':

    # Imports
    import arcpy
    import os
    # Set env settings
    arcpy.env.workspace = r"C:\ResearchProjects\HMSUC\Code\OD_DataPrep\Output\OhioZIP4byCounty.gdb"
    arcpy.env.overwriteOutput = True

    # input and output GDB locations on AGeoHL Workstation

    #ptsLoc = r'C:\ResearchProjects\HMSUC\Data\Ohio\DataSources\SafeGraph\core_poi_ohio.gdb\core_poi_ohio_naic_722511_full_service_restaurants'
    ptsLoc = r'C:\ResearchProjects\HMSUC\Data\Ohio\DataSources\SafeGraph\core_poi_ohio.gdb\core_poi_2_county_naic_446110'
    polysLoc = r'C:\ResearchProjects\HMSUC\Data\USA\US Census\TIGER\tlgdb_2019_a_39_oh\tlgdb_2019_a_39_oh.gdb\County'
    outputLoc = r'C:\ResearchProjects\HMSUC\Code\OD_DataPrep\Output\OhioZIP4byCounty.gdb\POI_PHDR_4269'

    # Create Feature Layers for the POIs and Counties for use downstream
    arcpy.MakeFeatureLayer_management(ptsLoc,'poi_fl')
    arcpy.MakeFeatureLayer_management(polysLoc,'counties_fl')

    # Create A Description Object for the feature layer & output some info
    desc = arcpy.Describe('poi_fl')
    print("Name:      " + desc.nameString)
    # Find out if the layer represents a feature class
    if desc.dataElement.dataType == "FeatureClass":
        print("Feature class:      " + desc.dataElement.catalogPath)
        #print("Feature class Type: " + desc.featureClass.featureType)
    else:
        print("Not a regular feature class")

    # Create a list of county names to iterate through Lists for testing, Dict for production

    # List of one test county
    #Counties = ['39049']

    # Ohio TestArea list
    #Counties = ['39049', '39045']

    # Full Ohio Dictionary  County Name: County FID Code
    CountiesDict =  {
        "Adams County": 39001,
        "Allen County": 39003,
        "Ashland County": 39005,
        "Ashtabula County": 39007,
        "Athens County": 39009,
        "Auglaize County": 39011,
        "Belmont County": 39013,
        "Brown County": 39015,
        "Butler County": 39017,
        "Carroll County": 39019,
        "Champaign County": 39021,
        "Clark County": 39023,
        "Clermont County": 39025,
        "Clinton County": 39027,
        "Columbiana County": 39029,
        "Coshocton County": 39031,
        "Crawford County": 39033,
        "Cuyahoga County": 39035,
        "Darke County": 39037,
        "Defiance County": 39039,
        "Delaware County": 39041,
        "Erie County": 39043,
        "Fairfield County": 39045,
        "Fayette County": 39047,
        "Franklin County": 39049,
        "Fulton County": 39051,
        "Gallia County": 39053,
        "Geauga County": 39055,
        "Greene County": 39057,
        "Guernsey County": 39059,
        "Hamilton County": 39061,
        "Hancock County": 39063,
        "Hardin County": 39065,
        "Harrison County": 39067,
        "Henry County": 39069,
        "Highland County": 39071,
        "Hocking County": 39073,
        "Holmes County": 39075,
        "Huron County": 39077,
        "Jackson County": 39079,
        "Jefferson County": 39081,
        "Knox County": 39083,
        "Lake County": 39085,
        "Lawrence County": 39087,
        "Licking County": 39089,
        "Logan County": 39091,
        "Lorain County": 39093,
        "Lucas County": 39095,
        "Madison County": 39097,
        "Mahoning County": 39099,
        "Marion County": 39101,
        "Medina County": 39103,
        "Meigs County": 39105,
        "Mercer County": 39107,
        "Miami County": 39109,
        "Monroe County": 39111,
        "Montgomery County": 39113,
        "Morgan County": 39115,
        "Morrow County": 39117,
        "Muskingum County": 39119,
        "Noble County": 39121,
        "Ottawa County": 39123,
        "Paulding County": 39125,
        "Perry County": 39127,
        "Pickaway County": 39129,
        "Pike County": 39131,
        "Portage County": 39133,
        "Preble County": 39135,
        "Putnam County": 39137,
        "Richland County": 39139,
        "Ross County": 39141,
        "Sandusky County": 39143,
        "Scioto County": 39145,
        "Seneca County": 39147,
        "Shelby County": 39149,
        "Stark County": 39151,
        "Summit County": 39153,
        "Trumbull County": 39155,
        "Tuscarawas County": 39157,
        "Union County": 39159,
        "Van Wert County": 39161,
        "Vinton County": 39163,
        "Warren County": 39165,
        "Washington County": 39167,
        "Wayne County": 39169,
        "Williams County": 39171,
        "Wood County": 39173,
        "Wyandot County": 39175
        }

    # MAIN Iteration to create selections, feature layers, and GDB outputs

    for x in CountiesDict.values():
        print(x)
        # Create the polygon feature layer for each single County
        arcpy.MakeFeatureLayer_management(polysLoc, 'OH_County_{}'.format(x), "GEOID = '{}'".format(x))
        desc = arcpy.Describe('OH_County_{}'.format(x))
        print("Name:      " + desc.nameString)
        print("Feature class:      " + desc.dataElement.catalogPath)
        print(arcpy.GetCount_management('OH_County_{}'.format(x)))

        # Create a Selection of Counties that touch the input County and add to the selection
        # The Select Layer By Location tool allows the Input Feature Layer to be the same the layer specified in the
        # Selecting Features parameter. A useful application of this behavior is to select adjacent, connected,
        # or nearby features within a layer. Different Relationship options can be used to
        # generate the desired analysis or result.
        # counties_fl the set to select from....OH_County_{} the polygon to measure the boundar touches from.
        arcpy.MakeFeatureLayer_management(arcpy.SelectLayerByLocation_management('counties_fl', 'BOUNDARY_TOUCHES', 'OH_County_{}'.format(x), '', 'NEW_SELECTION'), 'OH_County_{}_BT'.format(x))

        # Select points (poi) WITHIN all the polygons (Counties).
        arcpy.SelectLayerByLocation_management('poi_fl', 'WITHIN', 'OH_County_{}_BT'.format(x))

        # Make a new Feature Layer based on the selection
        fl = arcpy.MakeFeatureLayer_management('poi_fl', 'TEMP_446110_{}'.format(x))
        fl_out_path = os.path.join(outputLoc, 'OH_PHDR_446110_{}'.format(x))
        fl_out = arcpy.MakeFeatureLayer_management('poi_fl', fl_out_path)

        # Reproject Feature Layer
        sr = arcpy.SpatialReference(4269)
        arcpy.Project_management(fl, fl_out, sr)

        # Write selection out to a GDB
        arcpy.FeatureClassToGeodatabase_conversion('OH_PHDR_446110_{}'.format(x), outputLoc)

