import colordescriptor
import argparse
import glob
import cv2

#Contsruct the argumen parser and parse the arguments
import graydescriptor

ap = argparse.ArgumentParser()
ap.add_argument("-dataset", required = True,
                 help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

#initialize the color descriptor
# cd = colordescriptor.ColorDescriptor((8, 12, 3))
# cd = colordescriptor.ColorDescriptor((8, 4, 4))
cd = graydescriptor.GrayDescriptor(256)
#open the output index file for writing
output = open(args["index"], "w")

#use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    #extract the image ID from the image path and load the image itself
    imageID = imagePath[imagePath.rfind("/")+ 1:]
    image = cv2.imread(imagePath)

    #describe the image
    features = cd.describe(image)

    #write the features to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))
    print("extracting feature from image %s "%imageID )
output.close
                        
