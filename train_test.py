import xml.etree.ElementTree as ET
import os
import numpy as np
import cv2 

#path='C:\Users\user\Downloads\firedata-master\firedata-master\fire-dataset\train\images'

listdir = os.listdir('annotations')


for i in listdir:
	
	#count=count+1
	#if(count>5):
	#break

	tree = ET.parse('annotations/' + i)
	root = tree.getroot()
	#w=float(root[4][0].text)
	#h=float(root[4][1].text)

	name = root[1].text
	imgopen = r'C:\Users\user\Downloads\firedata-master\firedata-master\fire-dataset\\train\images\\'
	imgsave = r'C:\Users\user\Downloads\firedata-master\firedata-master\fire-dataset\\train\bbimage\\'

	img = cv2.imread(imgopen + name)
	#file.write(imgpath)

	#bdfile=open(bdpath + (name.split('.'))[0] + '.txt' ,'w')
	for obj in root.iter('object'):

		xmin = int(obj[4][0].text)
		ymin = int(obj[4][1].text)
		xmax = int(obj[4][2].text)
		ymax = int(obj[4][3].text)

                cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,0,0),3)
        cv2.imwrite(imgsave + name ,img)

        
    

    

    

    
