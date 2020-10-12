# Name: Task1e.py
# Description: Buffers Streams feature class 100, 200, 300, 400, and 500 m

# Import system modules
import arcpy

# Sets arcpy workspace to Data folder
arcpy.env.workspace = "V:/ENV859_PS4/Data"
# Allows an overwrite to the output in the Data file
arcpy.env.overwriteOutput = True

# Sets the input feature to be the streams shapefile path
in_features = "streams.shp"

# Creates for loop to iterate through range 100 to 500
for dist in range(100, 600, 100):
    # Set buffer distance as current iterated # and assigns it a unit
    buffDist = str(dist) + " meters"
    # Allows individual feature class to be named after current buffer number
    out_feature_class = f"V:/ENV859_PS4/scratch/buff_{dist}.shp"
    #  Executes the buffer command so they streams are buffered on both sides
    # with a round end and dissolved as a sinlge feature based on current iteration
    arcpy.Buffer_analysis(in_features, out_feature_class, buffDist,'','','ALL')