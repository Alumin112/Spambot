import pyautogui,time
times = 500
word = 'How is my spambot?'
time.sleep(5)
for x in range(times):
    pyautogui.typewrite(word)
    pyautogui.press('enter')