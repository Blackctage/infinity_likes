import time
import webbrowser
import pyautogui
from pynput.keyboard import *

profiles_name = 'julia_bernada'
pause = True
running = True

#  ======== settings ========
enter_key = Key.f2
exit_key = Key.esc


#  ==========================


def on_press(key):
    global running, pause, infinity_likes_running

    if key == enter_key:
        pause = True
        print(s, s, s, s, s, s)
        infinity_likes_main()
        print("[Resumed]")
    elif key == exit_key:
        running = False
        infinity_likes_running = False
        print("[Exit]")


def display_controls():
    print("//  ---------------------------------------------------MENU------------------------------------------------")
    print("// - Settings: ")
    print("// - Controls:")
    print("\t F2 = start infinity_likes")
    print("\t Esc = Exit")
    print("-----------------------------------------------------------------------------------------------------------")
    print('Press Shift to start ...')


s = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'


def main():
    lis = Listener(on_press=on_press)
    lis.start()
    display_controls()
    global pause
    while running:
        if not pause:
            print(s, s, s)
            infinity_likes_main()
    lis.stop()


# ================================================INFINITY_LIKES=======================================================

real_amount_of_photo = 10

infinity_likes_pause = True
infinity_likes_running = True

#  ======== settings ========
delay = 0.5  # in seconds
resume_key = Key.space
pause_key = Key.space
make_key = Key.enter
restart_key = Key.shift
return_key = Key.tab


#  ==========================


def infinity_likes_display_instagram_search():
    # open instagram and profiles_name
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome"
                                                                     "\Application\chrome.exe"))
    webbrowser.get('Chrome').open('instagram.com/' + profiles_name + '/')

    time.sleep(10)  # make infinity_likes_pause for 10 seconds
    pyautogui.click(344, 742)  # click on the first photo


def infinity_likes_on_press(key):
    global infinity_likes_running, infinity_likes_pause, running, pause

    if key == resume_key and infinity_likes_pause == True:
        infinity_likes_pause = False
        print("[Resumed]")
    elif key == pause_key and infinity_likes_pause == False:
        infinity_likes_pause = True
        print("[Paused]")
    elif key == make_key:
        infinity_likes_display_instagram_search()
        print('[Made_new_tab]')
    elif key == restart_key:
        print(s)
        infinity_likes_running = True
        infinity_likes_main()
        print("[Restarted]")
    elif key == return_key:
        print("[Exit]")
        print(s, s, s, s)
        pause = True
        main()


def infinity_likes_display_controls():
    print("-------------------------------------------AutoInstagramClicker---------------------------------------")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print('\t Space = Resume')
    print("\t Space = Pause")
    print("\t Enter = Make new tab")
    print("\t Shift = Restart")
    print("\t Tab = Return to MainMenu           ")
    print("------------------------------------------------------------------------------------------------------")
    print('Press Space to start ...')


def infinity_likes_main():
    lis = Listener(on_press=infinity_likes_on_press)
    lis.start()
    amount_of_photo = real_amount_of_photo
    infinity_likes_display_controls()
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

