# -*- coding: utf-8 -*-
#小波变换提取特征
from scipy.io import loadmat
import pywt #pywavelets

inputfile = 'C:/Users/Administrator/Desktop/big data/chapter4/demo/data/leleccum.mat' #matlab信号文件

mat = loadmat(inputfile) #mat是python专用格式,需要loadmat加载
signal = mat['leleccum'][0]

coeffs = pywt.wavedec(signal, 'bior3.7', level=5) #bior小波族 print pywt.families，族中小波名称print pywt.wavelist(‘bior’)
#小波变化函数说明 https://www.cnblogs.com/keye/p/7809207.html
