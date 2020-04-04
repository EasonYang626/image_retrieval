# -*- coding: utf-8 -*-
from numpy import linalg
from sklearn.metrics.pairwise import cosine_similarity

from extract_cnn_vgg16_keras import VGGNet
import numpy as np
import h5py
import test7


# ap = argparse.ArgumentParser()
# ap.add_argument("-query", required = True,
# 	help = "Path to query which contains image to be queried")
# ap.add_argument("-index", required = True,
# 	help = "Path to index")
# ap.add_argument("-result", required = True,
# 	help = "Path for output retrieved images")
# args = vars(ap.parse_args())
#
#
# # read in indexed images' feature vectors and corresponding image names
# h5f = h5py.File(args["index"],'r')
# # feats = h5f['dataset_1'][:]
# feats = h5f['dataset_1'][:]
# print(feats)
# imgNames = h5f['dataset_2'][:]
# print(imgNames)
# h5f.close()
#
# print("--------------------------------------------------")
# print("               searching starts")
# print("--------------------------------------------------")
#
# # read and show query image
# queryDir = args["query"]
# queryImg = mpimg.imread(queryDir)
# plt.title("Query Image")
# plt.imshow(queryImg)
# plt.show()
#
# # init VGGNet16 model
# model = VGGNet()
#
# # extract query image's feature, compute simlarity score and sort
# queryVec = model.extract_feat(queryDir)
# scores = np.dot(queryVec, feats.T)
# rank_ID = np.argsort(scores)[::-1]
# rank_score = scores[rank_ID]
# #print rank_ID
# #print rank_score
#
#
# # number of top retrieved images to show
# maxres = 3
# imlist = [imgNames[index] for i,index in enumerate(rank_ID[0:maxres])]
# print("top %d images in order are: " %maxres, imlist)
#
# # show top #maxres retrieved result one by one
# for i,im in enumerate(imlist):
#     image = mpimg.imread(args["result"]+"/"+str(im, 'utf-8'))
#     plt.title("search output %d" %(i+1))
#     plt.imshow(image)
#     plt.show()

def query(self,image):
    # 更改查询数据库
    h5f = h5py.File('featureCNN.h5', 'r')
    # h5f = h5py.File('new_feature.h5', 'r')
    feats = h5f['dataset_1'][:]
    # print(feats)
    imgNames = h5f['dataset_2'][:]
    # print(imgNames)
    h5f.close()
    # read and show query image
    #queryDir = args["query"]
    # queryImg = mpimg.imread(image)
    # plt.title("Query Image")
    # plt.imshow(queryImg)
    # plt.show()
    # 更改查询所用模型
    # init VGGNet16 model
    model = VGGNet()
    # model = test7.VGG()
    # extract query image's feature, compute simlarity score and sort
    queryVec = model.extract_feat(image)
    # 余弦相似度算法
    # vec = queryVec.reshape(-1,1)
    # cosscore = []
    # for i in range(10699):
    #       vec1 = feats[i].reshape(-1,1)
    #       cos = cosine_similarity(vec.T,vec1.T)
    #       cosscore.append(cos[0][0])
    Escore = []
    for i in range(10699):
        dist = linalg.norm(queryVec-feats[i])

        Escore.append(dist)
    scores = np.dot(queryVec, feats.T)
    # 欧式距离算法
    # print('查询图片特征向量:')
    # print(queryVec)

    rank_ID = np.argsort(scores)[::-1]
    # rank_ID1 = np.argsort(cosscore)[::-1]
    # rank_ID2 = np.argsort(Escore)[::-1]
    # rank_score = scores[rank_ID]
    # print rank_ID
    # print rank_score
    # number of top retrieved images to show
    maxres = 10
    imlist = [imgNames[index] for i, index in enumerate(rank_ID[0:maxres])]
    print("top %d images in order are: " % maxres, imlist)
    # print(r'E:\graduation\image_retrieval\image_retrieval\database1' + '\\' + imlist[0].decode())
    return imlist
    # show top #maxres retrieved result one by one
    # for i, im in enumerate(imlist):
    #     image = mpimg.imread('database1' + "/" + str(im, 'utf-8'))
    #     plt.title("search output %d" % (i + 1))
    #     plt.imshow(image)
    #     plt.show()


