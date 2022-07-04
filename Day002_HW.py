# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xml.dom.minidom

# 存取檔案
doc = xml.dom.minidom.parse("./sample.xml")

# 存取我們的資訊
print(doc.getElementsByTagName("Title")[0].firstChild.nodeValue)

# 用迴圈存取我們的資訊
chapters = doc.getElementsByTagName("Chapter")
for chapter in chapters:
    print (chapter.getAttribute('name'), chapter.firstChild.nodeValue)

import xml.etree.ElementTree as ET 

# 存取檔案
tree = ET.parse('./sample.xml') 
root = tree.getroot()

# 存取我們的資訊
print(root[0].text)

# 用迴圈存取我們的資訊
chapters = root[2]
for chapter in chapters:
    print (chapter.attrib['name'], chapter.text)

import xmltodict

# 存取檔案

with open('./sample.xml') as fd:
    doc = dict(xmltodict.parse(fd.read()))

# 存取我們的資訊
print(doc['CUPOY']['Title'])

# 用迴圈存取我們的資訊
chapters = doc['CUPOY']['Chapters']['Chapter']
for chapter in chapters:
    print (chapter['@name'], chapter['#text'])

# 下載檔案
import urllib.request
import zipfile

res = "http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"
urllib.request.urlretrieve(res, "./data/example.zip")
f = zipfile.ZipFile('./data/example.zip')
f.extractall('./data')

import zipfile
f = zipfile.ZipFile('./data/example.zip')
f.extractall('./data')

import os, sys

# 打开文件
dirs = os.listdir( './data' )

# 输出所有文件和文件夹
for file in dirs:
    print(file)

# 讀檔案
with open("./data/64_72hr_CH.xml", "r") as fh:
    xml = fh.read()
print(xml)

# 解析檔案內容
import xmltodict
d = dict(xmltodict.parse(xml))
print(d)

# 取出 datasetDescription
datasetDescription = d['cwbopendata']['dataset']['datasetInfo']['datasetDescription']
print(datasetDescription)

import pandas as pd
datasetlocations = pd.DataFrame(d['cwbopendata']['dataset']['locations']['location'])
datasetlocations['T']=datasetlocations['weatherElement'].str[0]
df = pd.DataFrame()
for inx in datasetlocations.index:
    for i in datasetlocations.iloc[inx]['T']['time']:
        i['item']=datasetlocations.at[inx, 'locationName']
        df = df.append(pd.DataFrame(i))
df.drop(['measures'], axis=0, inplace=True)
print(df)