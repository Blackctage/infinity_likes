import pyautogui
import webbrowser

webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome"
                                                                 "\Application\chrome.exe"))
webbrowser.get('Chrome').open('instagram.com')

pyautogui.PAUSE = 1  # make infinity_likes_pause on 1 second for writing TEXT
pyautogui.click(609, 137, duration=20)  # after 20 seconds click on the Instagram's search

pyautogui.write('k_bernada')  # write TEXT with MINIMUM_DURATION after 1 second
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
