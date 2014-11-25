#encoding: utf-8

import os
import sys
import pandas as pd
import numpy as np

'''
@Note This is used to combine csvs into one.
@Author Jonny Wan
@E-mail beikehua@j1.com
@date 2014-09-10
@Version 0.1
'''

#############
# this is used to write csvs into one. result is d:\\test_0910.csv

listfile=os.listdir('D:\\recom2.0\\Pearson')
for i in listfile:
	# print i  #,'\n'
	tempfolder = 'D:\\recom2.0\\Pearson'+ '\\'+ i
	# print tempfolder
	child_fold_list = os.listdir(tempfolder)
	# print child_fold_list
	for j in child_fold_list:
		filedir =  tempfolder + '\\' +j
		temp_data = pd.read_csv(filedir)
		n = len(temp_data)
		print filedir,n
		temp_data.to_csv('d:\\test_0911.csv',mode = 'ab+',header=False)



#############
# this is used to write csvs into one. result is d:\\test_0910_2.csv
'''
listfile=os.listdir('D:\\recom2.0\\result')
for i in listfile:
	print i  #,'\n'
	tempfolder = 'D:\\recom2.0\\result'+ '\\'+ i
	# print tempfolder
	# child_fold_list = os.listdir(tempfolder)
	# # print child_fold_list
	# for j in child_fold_list:
	# 	filedir =  tempfolder + '\\' +j
	# 	print filedir
	
	temp_data = pd.read_csv(tempfolder)
	temp_data.to_csv('d:\\test_0910_2.csv',mode = 'ab+',header=False)
'''

