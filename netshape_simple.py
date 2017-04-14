#!/usr/bin/env python
import sys
sys.path.insert(0,'/home/ecoluo/caffe/python')
import caffe
#import cv2
import numpy as np

net = caffe.Net('/home/ecoluo/caffe/examples/tinyimagenet_luot/process/self_longversion/trainself_val.prototxt', caffe.TRAIN)

print "\nnet.inputs =", net.inputs
print "\ndir(net.blobs) =", dir(net.blobs)
print "\ndir(net.params) =", dir(net.params)
print "\nconv shape = ", net.blobs['conv1'].data.shape
#print "\nconv shape = ", net.blobs['relu1'].data.shape
print "\npool1 shape = ", net.blobs['pool1'].data.shape
print "\nconv shape = ", net.blobs['conv2'].data.shape
#print "\nconv shape = ", net.blobs['relu2'].data.shape
print "\nconv shape = ", net.blobs['conv3'].data.shape
#print "\nconv shape = ", net.blobs['relu3'].data.shape
print "\nconv shape = ", net.blobs['conv4'].data.shape
#print "\nconv shape = ", net.blobs['relu4'].data.shape
print "\npool2 shape = ", net.blobs['pool2'].data.shape
print "\nconv shape = ", net.blobs['conv5'].data.shape
#print "\nconv shape = ", net.blobs['relu5'].data.shape
print "\npool3 shape = ", net.blobs['pool3'].data.shape
print "\nconv shape = ", net.blobs['conv6'].data.shape
#print "\nconv shape = ", net.blobs['relu6'].data.shape
print "\nconv shape = ", net.blobs['conv7'].data.shape
#print "\nconv shape = ", net.blobs['relu7'].data.shape
#print "\nconv shape = ", net.blobs['drop1'].data.shape
print "\nconv shape = ", net.blobs['fc1'].data.shape
#print "\nconv shape = ", net.blobs['relu7'].data.shape
#print "\nconv shape = ", net.blobs['drop2'].data.shape
print "\nconv shape = ", net.blobs['fc2'].data.shape
#print "\nconv shape = ", net.blobs['relu8'].data.shape
print "\nconv shape = ", net.blobs['loss'].data.shape




#https://prateekvjoshi.com/2016/02/09/deep-learning-with-caffe-in-python-part-ii-interacting-with-a-model/
