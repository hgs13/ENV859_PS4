# Name: Task2.py
# Description: Selects roads by class type

# Import system modules
import arcpy

# Sets arcpy workspace to Data folder
arcpy.env.workspace = "V:/ENV859_PS4/Data"
# Allows an overwrite to the output in the Data file
arcpy.env.overwriteOutput = True

# Creates a string variable containing path to Roads.shp
in_roads = "Roads.shp"

# Creates a multi-value string variable
in_roads_multi = ('0;201;203')
#in_roads_multi = 

# Splits the road class types into a list
in_roads_list = in_roads_multi.split(';')

#in_features = "majorrds.shp"
#out_feature_class = "V:/ArcPyDemo1/scratch/majorrdsClass4.shp"

where_clause = '"CLASS" = \'4\''


# Creates for loop to iterate through and selects by road type 

    # Set buffer distance as current iterated # and assigns it a unit
#class = str(in_roads_list)
    # Allows individual feature class to be named after current buffer number
out_feature_class = "V:/ENV859_PS4/scratch/roads_class.shp"
arcpy.Select_analysis(in_roads_list, out_feature_class, where_clause)
