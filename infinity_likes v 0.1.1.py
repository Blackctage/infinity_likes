import pyautogui

pyautogui.PAUSE = 0.5  # make infinity_likes_pause on 0.5 second from moveTo center to press enter
pyautogui.click(223, 13)  # open google

pyautogui.moveTo(700, 600)  # MoveTo x and y (the center of the Screen)
pyautogui.click(500, 92, duration=7)  # from x, y moveTo Google's search and click it with duration  of 7 seconds
pyautogui.write('instagram.com')  # write instagram.com with MINIMUM_DURATION
pyautogui.PAUSE = 23  # make infinity_likes_pause on 23 seconds after press enter
pyautogui.press('enter')  # press enter immediately

pyautogui.PAUSE = 1  # make infinity_likes_pause on 1 second for writing TEXT
pyautogui.click(609, 137)  # after 20 seconds click on the Instagram's search

pyautogui.write('julia_bernada')  # write TEXT with MINIMUM_DURATION after 1 second
pyautogui.PAUSE = 7  # make infinity_likes_pause on 7 seconds before click on his/her profile
pyautogui.hotkey('enter')  # press enter with infinity_likes_pause 1 second

pyautogui.click(636, 197)  # click on her profile after 5 seconds
pyautogui.PAUSE = 0
pyautogui.click(344, 742)  # click on the first photo after 5 second
x = 10  # amount of photo need to like
for i in range(x):  # make cycle
    pyautogui.moveTo(777, 620, duration=1)  # move Mouse To x and y, now duration like a infinity_likes_pause
    pyautogui.doubleClick(493, 454)  # like photo
    pyautogui.click(1170, 425)  # click next photo

    x -= 1
    print('Left Photo: ' + str(x))  # print How much photo leave

print('Work is ready')  # tell us that work is ready
