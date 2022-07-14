#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:19:50 2022

@author: jklkj
"""

import requests
import os
from bs4 import BeautifulSoup
from PIL import Image
import io

url = 'https://www.ptt.cc/bbs/Beauty/M.1574854555.A.E5C.html'
resp = requests.get(url, cookies={'over18': '1'})
soup = BeautifulSoup(resp.text)

output_dir = 'downloads'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image_tags = soup.find(id='main-content').findChildren('a', recursive=False)

for img_tag in image_tags:
    if 'imgur' not in img_tag['href']:
        continue
    Img_Name = img_tag['href'].split('/')[-1]
    img_url = 'https://i.imgur.com/{}'.format(Img_Name)
    with requests.get(img_url) as r:
        img = Image.open(io.BytesIO(r.content))
        img_save = '{img_dir}/{img_id}'.format(img_dir=output_dir, img_id=Img_Name)
        img.save(img_save)

