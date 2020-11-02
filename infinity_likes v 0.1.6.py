import time
import webbrowser
import pyautogui
from pynput.keyboard import *

s = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

pause = True
running = True

#  ======== settings ========
enter_key = Key.f2
exit_key = Key.esc
#  ==========================


# functional
def on_press(key):
    """
    enter_key: stop menu, make distance, activate infinity_likes and print result

    exit_key: Stop everything and print result
    """
    global running, pause, infinity_likes_running  # globals

    if key == enter_key:  # activate infinity_likes
        pause = True  # stop menu
        print(s, s, s, s)  # make distance
        infinity_likes_main()  # activate infinity_likes
        print("[Resumed]")  # print result
    elif key == exit_key:  # STOP ALL
        running = False
        infinity_likes_running = False
        print("[Exit]")


# design MENU
def display_controls():
    """
    return: Menu on display
    """
    print("//  ---------------------------------------------------MENU------------------------------------------------")
    print("// - Settings: ")
    print("// - Controls:")
    print("\t F2 = start infinity_likes")
    print("\t Esc = Exit")
    print("-----------------------------------------------------------------------------------------------------------")
    print('Press Shift to start ...')


def main():
    """
    coupe on_press(function) and display_controls(design)
    """
    lis = Listener(on_press=on_press)  # prepare on_press
    lis.start()  # activate on_press
    display_controls()  # activate display_controls
    global pause
    while running:  # while running = true
        if not pause:  # if pause = false
            print(s, s, s)  # Make distance
            infinity_likes_main()
    lis.stop()  # stop on_press


# ================================================INFINITY_LIKES=======================================================

real_amount_of_photo = 10
profiles_name = 'julia_bernada'

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


# make tab
def infinity_likes_display_instagram_search():
    """
    open instagram, open profiles name and click on first photo
    """
    # open instagram and profiles_name
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome"
                                                                     "\Application\chrome.exe"))
    webbrowser.get('Chrome').open('instagram.com/' + profiles_name + '/')

    time.sleep(10)  # make infinity_likes_pause for 10 seconds
    pyautogui.click(344, 742)  # click on the first photo


# infinity_likes function
def infinity_likes_on_press(key):
    """
    resume_key: start infinity_likes
    pause_key: stop infinity_likes
    make_key: make new tab
    restart_key: make distance and restart infinity_likes
    return_key: make distance and activate MENU
    """
    global infinity_likes_running, infinity_likes_pause, running, pause

    if key == resume_key and infinity_likes_pause == True:  # stop pause
        infinity_likes_pause = False
        print("[Resumed]")
    elif key == pause_key and infinity_likes_pause == False:  # make pause
        infinity_likes_pause = True
        print("[Paused]")
    elif key == make_key:  # activate infinity_likes_display_instagram_search
        infinity_likes_display_instagram_search()  # make new tab
        print('[Made_new_tab]')
    elif key == restart_key:  # restart infinity_likes_main
        print(s)  # make distance
        infinity_likes_running = True
        infinity_likes_main()
        print("[Restarted]")
    elif key == return_key:  # return MENU
        print("[Exit]")
        print(s, s, s, s)  # make distance
        pause = True
        main()


# infinity_likes design
def infinity_likes_display_controls():
    """
    return: AutoInstagramClicker on display
    """
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
    """
    coupe infinity_likes_on_press(function) and infinity_likes_display_controls(design)
    """
    lis = Listener(on_press=infinity_likes_on_press)  # prepare infinity_likes_on_press
    lis.start()  # activate infinity_likes_on_press
    amount_of_photo = real_amount_of_photo  # as global
    infinity_likes_display_controls()  # activate infinity_likes_display_controls
    while infinity_likes_running:  # while infinity_likes_running = true
        for i in range(amount_of_photo):  # make cycle
            if not infinity_likes_pause:  # if infinity_likes_pause = false
                pyautogui.doubleClick(493, 454)  # like photo
                pyautogui.click(1170, 425)  # click next photo

                amount_of_photo -= 1
                print('Left Photo: ' + str(amount_of_photo))  # print How much photo leave
                pyautogui.PAUSE = delay  # make pause for delay
    lis.stop()  # stop infinity_likes_on_press


if __name__ == "__main__":
    main()
