# Name: Task1d.py
# Description: Allows and saves user input in output feature class 

# Import system modules
import arcpy

# Sets arcpy workspace to Data folder
arcpy.env.workspace = "V:/ENV859_PS4/Data"
# Allows an overwrite to the output in the Data file
arcpy.env.overwriteOutput = True

# Set local variables
# Sets the input feature to be the streams shapefile path
in_features = "streams.shp"
# Sets the user generated output feature class
out_feature_class = "V:/ENV859_PS4/scratch/buff_" + arcpy.GetParameterAsText(0) + "m.shp"
# Creates variable for user input buffer distance
distance = arcpy.GetParameterAsText(0) + " meters"

# Executes the buffer command so they streams are buffered on both sides
# with a round end and dissolved as a sinlge feature
arcpy.Buffer_analysis(in_features, out_feature_class, distance,'','','ALL')




