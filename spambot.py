import pyautogui,time
time.sleep(5)
f = open('conjuring.txt','r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')