import pyautogui
import webbrowser
import time

amount_of_photo = 10
profiles_name = 'julia_bernada'

# open instagram and profiles_name
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome"
                                                                 "\Application\chrome.exe"))
webbrowser.get('Chrome').open('instagram.com/' + profiles_name + '/')

time.sleep(10)  # make infinity_likes_pause for 10 seconds
pyautogui.click(344, 742)  # click on the first photo

for i in range(amount_of_photo):  # make cycle
    pyautogui.moveTo(777, 620, duration=1)  # move Mouse To x and y, now duration like a infinity_likes_pause
    pyautogui.doubleClick(493, 454)  # like photo
    pyautogui.click(1170, 425)  # click next photo

    amount_of_photo -= 1
    print('Left Photo: ' + str(amount_of_photo))  # print How much photo leave

print('Work is ready')  # tell us that work is ready
