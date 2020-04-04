import colordescriptor
import graydescriptor
import searcher
import argparse
import cv2

# ap = argparse.ArgumentParser()
# ap.add_argument("-index", required = True,
# 	help = "Path to where the computed index will be stored")
# ap.add_argument("-query", required = True,
# 	help = "Path to the query image")
# ap.add_argument("-result-path", required = True,
# 	help = "Path to the result path")
# args = vars(ap.parse_args())

def search(self,image):

    # cd = colordescriptor.ColorDescriptor((8, 12, 3))
    cd = colordescriptor.ColorDescriptor((8, 4, 4))

    #load the query image and describe it
    query = cv2.imread(image)
    features = cd.describe(query)
    print("query image features extracted")
    #perform the search
    # s = searcher.Searcher("color_index.csv")
    s = searcher.Searcher("color_index_2.csv")
    results = s.search(features)
    print("search finished")
    """for (result, idd) in results:
        cv2.imshow("Result", result)
        cv2.waitKey(0)"""
    return  results
    #display the query
    # cv2.imshow("Query", query)
    # cv2.waitKey(0)
    #
    #loop over the results

    # for (score, resultID) in results:
    #     #print "ResultID ", resultID
    #     #result = cv2.imread(args["result_path"] + "/" + resultID)
    #     result = cv2.imread(resultID)
    #     print(result)
