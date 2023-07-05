import sys
import os

import cv2
import json

import retinex

data_path = 'data'
img_list = os.listdir(data_path)

if not os.path.exists(dirname):
	os.mkdir(dirname)

if len(img_list) == 0:
    #print 'Data directory is empty.'
    exit()

with open('config.json', 'r') as f:
    config = json.load(f)

for img_name in img_list:
    if img_name == '.gitkeep':
        continue
    
    img = cv2.imread(os.path.join(data_path, img_name))


   
    img_amsrcr = retinex.automatedMSRCR(
        img,
        config['sigma_list']
    )

 

    shape = img.shape

    dirname = 'retinex_data'


    cv2.imwrite(os.path.join(dirname, '1.jpg'), img_amsrcr)

    
    cv2.waitKey()
