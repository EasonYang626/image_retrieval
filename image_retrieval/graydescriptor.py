import numpy as np
import cv2


class GrayDescriptor:
    def __init__(self, bins):
        # Store the number of bins of the 3D Histogram
        self.bins = bins

    def describe(self, image):
        # Convert the image to the HSV color space and initialize
        # the feautures used to quantify the image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        features = []
        hist = cv2.calcHist(image,[0],None,[256],[0,256])
        hist = cv2.normalize(hist, hist).flatten()
        features.extend(hist)
        # return the feature vector
        return features
        # Grab the dimensions and compute the center of the image
        # (h, w) = image.shape[:2]
        # (cX, cY) = (int(w * 0.5), int(h * 0.5))
        #
        # # Divide the image into four segments (top-left, top-right,
        # # bottom-right, bottom-left)
        # segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),
        #             (0, cX, cY, h)]
        #
        # # Construct an elliptical mask representing the center of the image
        # (axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
        # ellipMask = np.zeros(image.shape[:2], dtype="uint8")
        # cv2.ellipse(ellipMask, (int(cX), int(cY)), (int(axesX), int(axesY)), 0, 0, 360, 255, -1)
        #
        # # Loop over the segments
        # for (startX, endX, startY, endY) in segments:
        #     # Construct a mask for each corner of the image, subtracting
        #     # the elliptical center from it
        #     cornerMask = np.zeros(image.shape[:2], dtype="uint8")
        #     cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
        #     cornerMask = cv2.subtract(cornerMask, ellipMask)
        #
        #     # extract a color histogram from the image, then update the
        #     # feature vector
        #
        #     hist = self.histogram(image, cornerMask)
        #     features.extend(hist)
        #
        # # extract a color histogram from the elliptical region and update
        # # the feature vector
        # hist = self.histogram(image, ellipMask)
        # features.extend(hist)
        # # return the feature vector
        # return features

    # def histogram(self, image, mask):
    #     # Extract a 3D color histogram from the masked region of the image, using
    #     # the supplied number of bins per channel, then normalize the histogram
    #     hist = cv2.calcHist([image], mask, self.bins,256,[0,255])
    #     hist = cv2.normalize(hist, hist).flatten()
    #     return hist




