import xml.etree.ElementTree as ET
import os

path='/root/Downloads/darknet-master/fire-dataset/validation/images/'

listdir = os.listdir('annotations')
bdpath = 'labels/'

file=open('train.txt','w')

count=0

for i in listdir:
	
	#count=count+1
	#if(count>5):
	#break

	tree = ET.parse('annotations/' + i)
	root = tree.getroot()
	w=float(root[4][0].text)
	h=float(root[4][1].text)

	name= root[1].text
	imgpath = '/content/darknet/firedata/fire-dataset/validation/images/' + name + '\n'
	file.write(imgpath)

	bdfile=open(bdpath + (name.split('.'))[0] + '.txt' ,'w')
	for obj in root.iter('object'):

		xmin = float(obj[4][0].text)
		ymin = float(obj[4][1].text)
		xmax = float(obj[4][2].text)
		ymax = float(obj[4][3].text)

		x = ((xmin + xmax)/2 - 1)/w
		y = ((ymin + ymax)/2 - 1)/h
		width = (xmax - xmin)/w
		height = (ymax - ymin)/h



		txt = '0 ' + str(x) + ' ' + str(y) + ' ' + str(width) + ' ' + str(height) + '\n'

		bdfile.write(txt)

	#print(imgpath)
	#print(txt)

    

    

    

    
