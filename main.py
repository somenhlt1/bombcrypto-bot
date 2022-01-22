from pyautogui import *
from time import localtime, strftime
import pyautogui
import time

import random
import yaml

import win32gui


# Time format for logging.
time_format = strftime("%a, %d %b %Y %I:%M %p:", localtime())

game = win32gui.FindWindowEx(0, 0, None, '1234')
metamask = win32gui.FindWindowEx(0, 0, None, 'MetaMask Notification')

if __name__ == '__main__':
    stream = open("config.yaml", 'r')
    c = yaml.safe_load(stream)


def deployHeroes():
    deployedHero = 0
    dragTime = 0
    # Check heroes icon and click it
    hero_icon = pyautogui.locateOnScreen(
        './targets/hero-icon.png', confidence=0.9, region=(0, 0, 1056, 1077))
    if hero_icon == None:
        return False
    while hero_icon != None:
        click(game, int(hero_icon.left + hero_icon.width / 2),
              int(hero_icon.top + hero_icon.height / 2))
        time.sleep(1)
        hero_icon = pyautogui.locateOnScreen(
            './targets/hero-icon.png', confidence=0.9)

    while 1:

        check = pyautogui.locateAllOnScreen(
            './targets/green.png', confidence=0.9)

        if check != None:

            for pos in check:
                click(game, int(150 + pos.left + pos.width / 2),
                      int(pos.top + pos.height / 2))
                click(game, int(150 + pos.left + pos.width / 2),
                      int(pos.top + pos.height / 2))
                deployedHero += 1
                time.sleep(1)

            if dragTime >= 4 or deployedHero >= 5:
                #print(strftime("%a, %d %b %Y %I:%M %p:", localtime()) + "Exceeded draging times.")
                break
            check = None

            result = pyautogui.locateOnScreen(
                './targets/drag.png', confidence=0.8, region=(0, 0, 1056, 1077))
            if result != None:
                drag(int(result.left + result.width / 2),
                     int(result.top + result.height / 2))
                dragTime += 1
                time.sleep(3)

    logger(strftime("%a, %d %b %Y %I:%M %p:", localtime()) +
           "Deloyed hero count: " + str(deployedHero))
    time.sleep(2)
    exit = pyautogui.locateOnScreen('./targets/x.png', confidence=0.9)
    if exit == None:
        return False
    while exit != None:
        click(game, int(exit.left + exit.width / 2),
              int(exit.top + exit.height / 2))
        time.sleep(2)
        startwork()
        exit = pyautogui.locateOnScreen(
            './targets/x.png', confidence=0.9, region=(0, 0, 1056, 1077))
    logger(strftime("%a, %d %b %Y %I:%M %p:", localtime()) +
           "Done to deploy hero to work")

    return True


def deployAllHeroes():
    # Check heroes icon and click it
    hero_icon = pyautogui.locateOnScreen(
        './targets/hero-icon.png', confidence=0.9, region=(0, 0, 1056, 1077))
    if hero_icon == None:
        return False
    while hero_icon != None:
        click(game, int(hero_icon.left + hero_icon.width / 2),
              int(hero_icon.top + hero_icon.height / 2))
        time.sleep(1)
        hero_icon = pyautogui.locateOnScreen(
            './targets/hero-icon.png', confidence=0.9)

    check = pyautogui.locateOnScreen(
        './targets/all.jpg', confidence=0.95)
    if check == None:
        return False
    click(game, int(check.left + check.width / 2),
          int(check.top + check.height / 2))
    time.sleep(2)

    exit = pyautogui.locateOnScreen('./targets/x.png', confidence=0.9)
    if exit == None:
        return False
    while exit != None:
        click(game, int(exit.left + exit.width / 2),
              int(exit.top + exit.height / 2))
        time.sleep(2)
        startwork()
        exit = pyautogui.locateOnScreen(
            './targets/x.png', confidence=0.9, region=(0, 0, 1056, 1077))

    logger(strftime("%a, %d %b %Y %I:%M %p:", localtime()) +
           "Done to deploy hero to work")
    return True


def click(hwnd, x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    # lParam =  win32api.MAKELONG(x,y)
    # win32gui.PostMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
    # win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
    # win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)


def drag(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.dragTo(x, y-160, 1, button='left')

# def deployHeroes():
# 	deployedHero = 0
# 	dragTime = 0
# 	#Check heroes icon and click it
# 	hero_icon = pyautogui.locateOnScreen('./targets/hero-icon.png',confidence=0.9,region=(0,0,1056,1077))
# 	while hero_icon != None:
# 		click(int(hero_icon.left + hero_icon.width / 2),int(hero_icon.top + hero_icon.height / 2))
# 		time.sleep(1)
# 		hero_icon = pyautogui.locateOnScreen('./targets/hero-icon.png',confidence=0.9,region=(0,0,1056,1077))

# 	while deployedHero < c["heroes"]:
# 		check = pyautogui.locateOnScreen('./targets/go-work.png',confidence=0.9,region=(0,0,1056,1077))
# 		if check != None:
# 			click(int( check.left + check.width / 2),int(check.top + check.height / 2))
# 			click(int( check.left + check.width / 2),int(check.top + check.height / 2))
# 			deployedHero += 1
# 			time.sleep(1)
# 		else:
# 			if dragTime >= 3:
# 				#print(strftime("%a, %d %b %Y %I:%M %p:", localtime()) + "Exceeded draging times.")
# 				break
# 			result = pyautogui.locateOnScreen('./targets/drag.png',confidence=0.8,region=(0,0,1056,1077))
# 			if result != None:
# 				drag(int(result.left + result.width / 2),int(result.top + result.height / 2))
# 				dragTime += 1
# 				time.sleep(2)
# 			else:
# 				#print(strftime("%a, %d %b %Y %I:%M %p:", localtime()) + "I can't drag anymore"  )
# 				break
# 	logger(strftime("%a, %d %b %Y %I:%M %p:", localtime()) + "Deloyed hero count: " + str(deployedHero))
# 	time.sleep(2)
# 	exit = pyautogui.locateOnScreen('./targets/x.png',confidence=0.9,region=(0,0,1056,1077))
# 	while exit !=None:
# 		click(int(exit.left + exit.width / 2),int(exit.top + exit.height / 2))
# 		time.sleep(2)
# 		startwork()
# 		exit = pyautogui.locateOnScreen('./targets/x.png',confidence=0.9,region=(0,0,1056,1077))
# 	if pyautogui.locateOnScreen('./targets/hero-icon.png',confidence=0.9,region=(0,0,1056,1077)) != None:
# 		deployHeroes()
# 	logger(strftime("%a, %d %b %Y %I:%M %p:", localtime()) + "Done to deploy hero to work")


def startwork():
    work = pyautogui.locateOnScreen(
        './targets/treasure-hunt-icon.png', confidence=0.9, region=(0, 0, 1056, 1077))
    while work != None:
        click(game, int(work.left + work.width / 2),
              int(work.top + work.height / 2))
        time.sleep(2)
        work = pyautogui.locateOnScreen(
            './targets/treasure-hunt-icon.png', confidence=0.9, region=(0, 0, 1056, 1077))


def goback():
    result = False
    check = pyautogui.locateOnScreen('./targets/back.png', confidence=0.8)
    start = time.time()
    while check != None:
        result = False
        click(game, int(check.left + check.width / 2),
              int(check.top + check.height / 2))
        time.sleep(1)
        result = True
        check = pyautogui.locateOnScreen('./targets/back.png', confidence=0.8)
        has_timeouted = time.time() - start
        if has_timeouted >= 10:
            result = False
            break
    return result


def restart():
    logger(strftime("%a, %d %b %Y %I:%M %p:",
           localtime()) + "Restarting the game...")
    meta = pyautogui.locateOnScreen('./targets/metamask.png', confidence=0.8)
    while meta != None:
        pyautogui.click(int(meta.left + meta.width / 2),
                        int(meta.top + meta.height / 2))
        sleep(0.5)
        cancel = pyautogui.locateOnScreen(
            './targets/cancel.png', confidence=0.8)
        if cancel != None:
            pyautogui.click(int(cancel.left + cancel.width / 2),
                            int(cancel.top + cancel.height / 2))
            sleep(1)
        meta = pyautogui.locateOnScreen(
            './targets/metamask.png', confidence=0.8)

    check = pyautogui.locateOnScreen('./targets/reload.png', confidence=0.8)
    click(game, int(check.left + check.width / 2),
          int(check.top + check.height / 2))
    time.sleep(5)
    return True


def connect():
    check = pyautogui.locateOnScreen(
        './targets/connect-wallet.png', confidence=0.8)

    while check != None:
        click(game, int(check.left + check.width / 2),
              int(check.top + check.height / 2))
        time.sleep(5)
        wallet = pyautogui.locateOnScreen(
            './targets/select-wallet-2.png', confidence=0.8)
        if wallet != None:
            pyautogui.click(int(wallet.left + wallet.width / 2),
                            int(wallet.top + wallet.height / 2))
            time.sleep(2)
        else:
            logger("Connected failed")
            return False
        check = pyautogui.locateOnScreen(
            './targets/connect-wallet.png', confidence=0.8)
    return True


def reconnect():
    while 1:
        if restart() == True:
            if connect() == True:
                break


def checkNewMap():

    check = pyautogui.locateOnScreen('./targets/new-map.png', confidence=0.8)
    while check != None:
        click(game, int(check.left + check.width / 2),
              int(check.top + check.height / 2))
        time.sleep(1)
        logger(strftime("%a, %d %b %Y %I:%M %p:",
               localtime()) + "New Map Clicked")
        check = pyautogui.locateOnScreen(
            './targets/new-map.png', confidence=0.8)


def logger(message):
    print(message)
    logger_file = open("./logs/logger.log", "a", encoding='utf-8')
    logger_file.write(message + '\n')
    logger_file.close()


def main():
    timeout = c["timeout"]
    timeout_refresh = c["timeout_refresh"]
    logger("[----------------------------------------------------------------------------------------]")
    reconnect()
    time.sleep(10)
    deployAllHeroes()
    start = time.time()
    start_refresh = time.time()
    while 1:
        checkNewMap()
        time.sleep(2)
        has_time_out = time.time() - start
        if has_time_out > timeout:
            logger(strftime("%a, %d %b %Y %I:%M %p:", localtime()) +
                   "Starting to deploy hero to work")
            if goback() == False:
                logger(strftime("%a, %d %b %Y %I:%M %p:", localtime()) +
                       "Error: goback() error trying to reconnect.")
                reconnect()
                time.sleep(10)
            while 1:
                if deployAllHeroes() == True:
                    break
            start = time.time()
            start_refresh = time.time()

        has_time_out = time.time() - start_refresh
        if has_time_out > timeout_refresh:
            logger(strftime("%a, %d %b %Y %I:%M %p:", localtime()) +
                   "Relocating heroes position.")
            if goback() == False:
                logger(strftime("%a, %d %b %Y %I:%M %p:", localtime()) +
                       "Error: goback() error trying to reconnect.")
                reconnect()
                time.sleep(10)
            startwork()
            start_refresh = time.time()
        # get a random time from base + random time
        timeout_refresh = c["timeout_refresh"] + random.randrange(0, 100, 5)
        time.sleep(60)


main()
