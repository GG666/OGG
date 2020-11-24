import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import time
import pytesseract
import os
from PIL import Image
import pyperclip

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
time.sleep(2)
need = False

def shot(): #screenshot  (Picpick
	pyautogui.keyDown('shift') 
	pyautogui.keyDown('ctrl')
	pyautogui.press('a')
	pyautogui.keyUp('shift')
	pyautogui.keyUp('ctrl')
	time.sleep(5)

	pyautogui.moveTo(1889, 25, duration=0.5) #press exit
	pyautogui.click(1889, 25, button='left', duration=0.1)
	time.sleep(1)

# 12345665454654
def Play():
	pyautogui.moveTo(245, 199, duration=0.5) #create_room
	pyautogui.click(245, 199, button='left', duration=0.1)
	time.sleep(1)

	shot()
	res=con2()
	text=pytesseract.image_to_string(res,lang="chi_tra")
	tt=text.split()
	if(tt[-3]=='字' and tt[-2]=='據'):
		print(tt[-1])
		input=tt[-1][1:5]
		print(input)
		pyperclip.copy(input)
		pyautogui.moveTo(1402, 898, duration=0.5) #input
		pyautogui.click(1402, 898, button='left', duration=0.1)
		# if(len(tt[-1])>4):
			# pyautogui.typewrite(tt[-1][1:5])
			# time.sleep(2)
		# else:
		time.sleep(2)
		pyautogui.keyDown('ctrl') #enter room name
		pyautogui.keyDown('shift') #enter room name
		pyautogui.press('v') #enter room name
		pyautogui.keyUp('shift') #enter room name
		pyautogui.keyUp('ctrl') #enter room name
		# pyautogui.press('enter')
		time.sleep(2)
		pyautogui.moveTo(1744, 1024, duration=0.5) #press sure
		pyautogui.click(1744, 1024, button='left', duration=0.1)
		time.sleep(1)


	pyautogui.moveTo(948, 751, duration=0.5) #one person
	pyautogui.click(948, 751, button='left', duration=0.1)
	time.sleep(1)

	pyautogui.moveTo(594, 887, duration=0.5) #place room name pos
	pyautogui.click(594, 887, button='left', duration=0.1)
	time.sleep(2)

	pyautogui.keyDown('ctrl') #enter room name
	pyautogui.keyDown('shift') #enter room name
	pyautogui.press('v') #enter room name
	pyautogui.keyUp('shift') #enter room name
	pyautogui.keyUp('ctrl') #enter room name
	time.sleep(2)
	pyautogui.keyDown('ctrl') #enter room name
	pyautogui.keyDown('shift') #enter room name
	pyautogui.press('v') #enter room name
	pyautogui.keyUp('shift') #enter room name
	pyautogui.keyUp('ctrl') #enter room name
	time.sleep(2)
	# pyautogui.press('M') #enter room name
	# pyautogui.press('M') #enter room name
	# pyautogui.press('M') #enter room name
	# pyautogui.press('M') #enter room name
	# pyautogui.typewrite(['s','u','3','0','4','4','5','8','7'],0.2)
	# time.sleep(1)

	# pyautogui.press('shift') #enter room name
	# time.sleep(2)
	# pyautogui.press('M') #enter room name
	# pyautogui.press('M') #enter room name
	# pyautogui.press('M') #enter room name
	# pyautogui.press('M') #enter room name
	# pyautogui.press('M') #enter room name
	# pyautogui.typewrite(['1','2','0','0','4','4','5','8','7'],0.2)
	# time.sleep(1)

	pyautogui.moveTo(1744, 1024, duration=0.5) #press sure
	pyautogui.click(1744, 1024, button='left', duration=0.1)
	time.sleep(1)

	pyautogui.moveTo(899, 989, duration=0.5) #press done
	pyautogui.click(899, 989, button='left', duration=0.1)
	time.sleep(1)

	pyautogui.moveTo(256, 218, duration=0.5) #press diff
	pyautogui.click(256, 218, button='left', duration=0.1)
	time.sleep(1)

	pyautogui.moveTo(818, 426, duration=0.5) #select diff
	pyautogui.click(818, 426, button='left', duration=0.1)
	time.sleep(1)

	pyautogui.moveTo(1048, 705, duration=0.5) #select diff done
	pyautogui.click(1048, 705, button='left', duration=0.1)
	time.sleep(1)

	pyautogui.moveTo(1368, 998, duration=0.5) #start game
	pyautogui.click(1368, 998, button='left', duration=0.1)
	time.sleep(45)

	pyautogui.moveTo(899, 989, duration=0.5) #press exit
	pyautogui.click(899, 989, button='left', duration=0.1)
	time.sleep(25)


def Watch():
	global need
	pyautogui.moveTo(1648, 190, duration=0.5) #shop
	pyautogui.click(1648, 190, button='left', duration=0.1)
	time.sleep(1)

	pyautogui.moveTo(1071, 138, duration=0.5) #diamond
	pyautogui.click(1071, 138, button='left', duration=0.1)
	time.sleep(1)

	pyautogui.moveTo(562, 374, duration=0.5) #press first ad
	pyautogui.click(562, 374, button='left', duration=0.1)
	time.sleep(2)

	shot()
	con()
	time.sleep(2)
	Pic_ana()
	time.sleep(2)

	pyautogui.moveTo(562, 374, duration=0.5) #press second ad
	pyautogui.click(562, 374, button='left', duration=0.1)
	time.sleep(2)

	if(need):
		need=False
		shot()
		con()
		time.sleep(2)
		Pic_ana()
		time.sleep(6)

	time.sleep(30)
	pyautogui.moveTo(1790, 105, duration=0.5) #press exit
	pyautogui.click(1790, 105, button='left', duration=0.1)

	time.sleep(5)
	pyautogui.moveTo(1729, 904, duration=0.5) #press exit
	pyautogui.click(1729, 904, button='left', duration=0.1)

def Pic_ana():
	img = cv.imread('TT.png', 0)
	template = cv.imread('0.png', 0)
	h, w = template.shape[:2]  # rows->h, cols->w
	img2 = img.copy()
	method = eval('cv.TM_CCOEFF')
	res = cv.matchTemplate(img, template, method)
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
	top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)

	if(abs(top_left[0]-203)>2 and abs(bottom_right[0]-348)>2):
		print("TT")
		print(top_left[0])
		print(bottom_right[0])
		global need 
		need = True
		for i in range(1,5):
			template = cv.imread(str(i)+'.png', 0)
			h, w = template.shape[:2]  # rows->h, cols->w
			img2 = img.copy()
			method = eval('cv.TM_CCOEFF')
			res = cv.matchTemplate(img, template, method)
			in_val, max_val, min_loc, Max_loc = cv.minMaxLoc(res)
			top_left = Max_loc
			bottom_right = (top_left[0] + w, top_left[1] + h)

			if(top_left[0]+bottom_right[0]>800):
				print(3)
				print(top_left[0])
				print(bottom_right[0])
				pyautogui.moveTo(1107, 617, duration=0.5) #3
				pyautogui.click(1107, 617, button='left', duration=0.1)

			elif(top_left[0]+bottom_right[0]>550):
				print(2)
				print(top_left[0])
				print(bottom_right[0])
				pyautogui.moveTo(996, 630, duration=0.5) #2
				pyautogui.click(996, 630, button='left', duration=0.1)
			
			elif(top_left[0]+bottom_right[0]>300):
				print(1)
				print(top_left[0])
				print(bottom_right[0])
				pyautogui.moveTo(870, 627, duration=0.5) #1
				pyautogui.click(870, 627, button='left', duration=0.1)

			else:
				print(0)
				print(top_left[0])
				print(bottom_right[0])
				pyautogui.moveTo(741, 619, duration=0.5) #0
				pyautogui.click(741, 619, button='left', duration=0.1)
			time.sleep(0.1)
		time.sleep(2)
		# pyautogui.moveTo(1200, 370, duration=0.5) #1
		# pyautogui.click(1200, 370, button='left', duration=0.1)
		time.sleep(2)

	else:
		print("QQ")
		print(top_left[0])
		print(bottom_right[0])



#1566483143161354


def con():
	IMage=Image.open("Image 001.png")
	temp=IMage.convert('L')
	pixels=temp.load()
	for x in range(temp.width):
		for y in range(temp.height):
			if pixels[x,y]<10 or pixels[x,y]>240:
				pixels[x,y]=255
			else:
				pixels[x,y]=0
	temp.save("TT.png")
	os.remove('Image 001.png')
	return temp

def con2():
	IMage=Image.open("Image 001.png")
	temp=IMage.convert('L')
	pixels=temp.load()
	for x in range(temp.width):
		for y in range(temp.height):
			if  pixels[x,y]>100:
				pixels[x,y]=255
			else:
				pixels[x,y]=0
	temp.save("T0.png")
	os.remove('Image 001.png')
	return temp

def main():
	for i in range(2):
		# Pic_ana()
		Play()
		Watch()
		time.sleep(180)
		Watch()
		time.sleep(180)
		Watch()
		time.sleep(180)
		Watch()
		time.sleep(5)

if __name__ == "__main__":
	main()