# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#def select_pt_in_poly(pts, poly):
    # Selects points within a polygon

#def save_selection(selection):
    # Saves a selected set of Features to an output location specified in main



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Imports
    import arcpy as apy

    apy.env.overwriteOutput = True

    # input and output GDB locations
    ptsLoc = r'C:\ResearchProjects\HMSUC\Data\Ohio\DataSources\Precisely\ZIP4\Z4_Centroids_12007\GDB\OH_ZIP4.gdb\ESPG4326\OH_ZIP4_ESPG4326'
    polysLoc = r'C:\ResearchProjects\HMSUC\Data\USA\US Census\TIGER\tlgdb_2019_a_39_oh\tlgdb_2019_a_39_oh.gdb\County'
    outputLoc = r'C:\ResearchProjects\HMSUC\Code\OD_DataPrep\Output\OhioZIP4byCounty.gdb\OhioCountyZIP4PnPSelection'

    # Create the points feature layer
    apy.MakeFeatureLayer_management(ptsLoc,'points_fl')
    #apy.MakeFeatureLayer_management(polysLoc,'OH_Counties')

    # Create A Description Object for the feature layer & output some info
    desc = apy.Describe('points_fl')
    print("Name:      " + desc.nameString)
    # Find out if the layer represents a feature class
    if desc.dataElement.dataType == "FeatureClass":
        print("Feature class:      " + desc.dataElement.catalogPath)
        #print("Feature class Type: " + desc.featureClass.featureType)
    else:
        print("Not a regular feature class")

# Create a list of county names to iterate through


# List of one test county
    #Counties = ['39049']

    # Ohio TestArea list
    #Counties = ['39049', '39045']

# Full Ohio List
    CountiesDict = {
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
    # for x in Counties:
    for x in CountiesDict.values():
        # Create the polygon feature layer to use in the selection
        apy.MakeFeatureLayer_management(polysLoc, 'OH_{}'.format(x), "GEOID = '{}'".format(x))

        # Create a Description object to create some metadata to print
        desc = apy.Describe('OH_{}'.format(x))
        print("Name:      " + desc.nameString)
        print("Feature class:      " + desc.dataElement.catalogPath)

        # Select points (ZIP4) WITHIN polygons (Counties)
        apy.SelectLayerByLocation_management('points_fl', 'WITHIN', 'OH_{}'.format(x))

        # Make a new Feature Layer based on the selection
        apy.MakeFeatureLayer_management('points_fl', 'OH_ZIP4_{}'.format(x))

        # Write selection out to a GDB
        apy.FeatureClassToGeodatabase_conversion('OH_ZIP4_{}'.format(x), outputLoc)


