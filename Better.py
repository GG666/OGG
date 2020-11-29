import pytesseract
import pyautogui
import time
import pyperclip

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
pyautogui.FAILSAFE=False

def shot( Left, Top, Width, Height):
	im=pyautogui.screenshot(region=( Left, Top, Width, Height))
	return im

def move_and_click(x,y,delay):
	pyautogui.moveTo(x, y, duration=0.5)
	pyautogui.click(x, y, button='left', duration=0.1)
	time.sleep(delay)

def Play():
	exit=False
	move_and_click(245,199,2) #create room
	press_location0=pyautogui.locateOnScreen('verify.png',region=(1300,800,200,100), confidence=0.8)
	if(press_location0!=None):
		im=pyautogui.screenshot(region=(1427,800,100,50))
		text=pytesseract.image_to_string(im)
		a123 = text.split()
		# print(a123)
		pyperclip.copy(a123[0])
		move_and_click(1400,900,2) #enter verify code
		# print(type(text))
		# print(pyperclip.paste(text))
		# time.sleep(2)
		pyautogui.keyDown('ctrl')
		pyautogui.keyDown('shift')
		pyautogui.press('v')
		pyautogui.keyUp('shift')
		pyautogui.keyUp('ctrl')
		time.sleep(2)
		move_and_click(1744,1024,2) #press sure
		pyperclip.copy('GVJ53DL79M')


	move_and_click(948,751,1) #one person
	move_and_click(594,887,3)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('shift')
	pyautogui.press('v')
	pyautogui.keyUp('shift')
	pyautogui.keyUp('ctrl')
	move_and_click(1744,1024,2) #press sure
	move_and_click(899,989,2) #press done
	move_and_click(256,218,2) #press diff
	move_and_click(818,426,2) #select diff
	move_and_click(1048,705,2) #select done
	move_and_click(1368,998,30) #press start
	count=0
	while(exit==False):
		time.sleep(1)
		press_location=pyautogui.locateOnScreen('exit.png',region=(810,900,250,100), confidence=0.9,grayscale=True)
		if(press_location!=None):
			exit=True
			break
		else:
			count=count+1
			if(count>30):
				exit()
	move_and_click(899,989,5) #press exit

def Watch():
	shop=False
	count=0
	while(shop==False):
		time.sleep(1)
		press_location=pyautogui.locateOnScreen('shop.png',region=(1500,120,300,200), confidence=0.9,grayscale=True)
		if(press_location!=None):
			shop=True
			break
		else:
			count=count+1
			if(count>30):
				exit()

	move_and_click(1648,190,2) #press shop
	move_and_click(1071,138,1) #press diamond
	move_and_click(562,374,1) #press ad 1

	image=shot(690,550,500,150)
	for i in range(1,5):
		press_location=pyautogui.locateOnScreen('temp'+str(i)+'.png',region=(600,450, 700, 400), confidence=0.9,grayscale=True)
		if(press_location==None):
			break
		else:
			# print(i)
			# print(press_location)
			temp=pyautogui.center(press_location)
			move_and_click(temp[0],temp[1],0.2)
	time.sleep(10)

	move_and_click(562,374,2)#press ad 2
	image=shot(690,550,500,150)
	for i in range(1,5):
		press_location=pyautogui.locateOnScreen('temp'+str(i)+'.png',region=(600,450, 700, 400), confidence=0.9,grayscale=True)
		if(press_location==None):
			break
		else:
			# print(i)
			# print(press_location)
			temp=pyautogui.center(press_location)
			move_and_click(temp[0],temp[1],0.2)
	time.sleep(40)

	pyautogui.keyDown('ctrl') #leave
	pyautogui.keyDown('shift')
	pyautogui.press('2')
	pyautogui.keyUp('shift')
	pyautogui.keyUp('ctrl')
	time.sleep(10)

	move_and_click(1729,904,2) #exit

def save():
	move_and_click(1625,940,10)
	move_and_click(1050,682,10)
	move_and_click(1226,357,10)

def close():
	move_and_click(1823,31,30)
	move_and_click(1008,584,15)

def Restart():
	Max=False
	count=0
	move_and_click(1919,1079,2)
	move_and_click(1659,696,0.1)
	pyautogui.doubleClick()
	time.sleep(10)
	while(Max==False):
		time.sleep(1)
		press_location=pyautogui.locateOnScreen('Max_button.png',region=(1100,60,400,100), confidence=0.9,grayscale=True)
		if(press_location!=None):
			temp=pyautogui.center(press_location)
			move_and_click(temp[0],temp[1],10)
			Max=True
			break
		else:
			count=count+1
			if(count>30):
				exit()
	time.sleep(100)
	move_and_click(933,792,5)


def main():
	pyperclip.copy('DHVHGJI12')
	for i in range(11):
		Restart()
		j=0
		if(i<2):
			j=4
		elif(i<6):
			j=8
		else:
			j=2
		for k in range(j):
			time.sleep(5)
			Play()
			Watch()
			time.sleep(155)
			Watch()
			time.sleep(5)
			print(i)
			print("iteration----------")
			print(k)
		save()
		close()
		time.sleep(10)

if __name__ == "__main__":
	main()
