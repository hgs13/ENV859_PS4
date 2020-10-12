# Name: Task1b.py
# Description: Buffers Streams feature class 1000 m and allows script to be 
# overwritten

# Import system modules
import arcpy

# Sets arcpy workspace to Data folder
arcpy.env.workspace = "V:/ENV859_PS4/Data"
# Allows an overwrite to the output in the Data file
arcpy.env.overwriteOutput = True

# Set local variables
# Sets the input feature to be the streams shapefile path
in_features = "streams.shp"
# Sets the output path for the StrmBuff1km.shp
out_feature_class = "V:/ENV859_PS4/scratch/StrmBuff1km.shp"
# Creates variable for buffer distance
buffDist = "1000 meters"

# Executes the buffer command so they streams are buffered on both sides
# with a round end and dissolved as a sinlge feature
arcpy.Buffer_analysis(in_features, out_feature_class, buffDist,'','','ALL')



