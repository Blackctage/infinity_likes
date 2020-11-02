import time
import webbrowser
import pyautogui
from pynput.keyboard import *

amount_of_photo = 10
profiles_name = 'julia_bernada'

infinity_likes_pause = True
infinity_likes_running = True

#  ======== settings ========
delay = 1.5  # in seconds
resume_key = Key.shift
pause_key = Key.space
exit_key = Key.esc
#  ==========================

# open instagram and profiles_name
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome"
                                                                 "\Application\chrome.exe"))
webbrowser.get('Chrome').open('instagram.com/' + profiles_name + '/')

time.sleep(10)  # make infinity_likes_pause for 10 seconds
pyautogui.click(344, 742)  # click on the first photo


def on_press(key):
    global infinity_likes_running, infinity_likes_pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker by 4B")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t Shift   = Resume")
    print("\t Space = Pause")
    print("\t Esc = Exit")
    print("-----------------------------------------------------")
    print('Press Space to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()
    global amount_of_photo
    display_controls()
    while infinity_likes_running:
        for i in range(amount_of_photo):  # make cycle
            if not infinity_likes_pause:

                pyautogui.doubleClick(493, 454)  # like photo
                pyautogui.PAUSE = 0
                pyautogui.click(1170, 425)  # click next photo

                amount_of_photo -= 1
                print('Left Photo: ' + str(amount_of_photo))  # print How much photo leave
                pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()