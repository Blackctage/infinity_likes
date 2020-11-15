import pynput.keyboard as keyboard
import webbrowser
import pyautogui
import time


class GameObject:
    pass


class Menu(GameObject):
    def __init__(self):
        self.distanation = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

        self.pause = True
        self.running = True

        self.enter_key = keyboard.Key.f2
        self.exit_key = keyboard.Key.esc

    # functional
    def on_press(self, key):
        """
        enter_key: stop menu, make distance, activate infinity_likes and print result

        exit_key: Stop everything and print result
        """
        if key == self.enter_key:  # activate infinity_likes
            self.pause = True  # stop menu
            print(self.distanation, self.distanation, self.distanation, self.distanation)  # make distance
            Infinity_main().infinity_likes_main()  # activate infinity_likes
            print("[Resumed]")  # print result
        elif key == self.exit_key:  # STOP ALL
            self.running = False
            Infinity().infinity_likes_running = True
            print("[Exit]")

    # design MENU
    def display_controls(self):
        """
        return: Menu on display
        """
        print("//  -------------------------------------------------MENU----------------------------------------------")
        print("// - Settings: ")
        print("// - Controls:")
        print("\t F2 = start infinity_likes")
        print("\t Esc = Exit")
        print("-------------------------------------------------------------------------------------------------------")
        print('Press Shift to start ...')


class Main(Menu):
    def main(self):
        """
        coupe on_press(function) and display_controls(design)
        """
        lis = keyboard.Listener(on_press=self.on_press)  # prepare on_press
        lis.start()  # activate on_press
        self.display_controls()  # activate display_controls
        while self.running:  # while running = true
            if not self.pause:  # if pause = false
                print(self.distanation, self.distanation, self.distanation)  # Make distance
                Infinity_main().infinity_likes_main()
        lis.stop()  # stop on_press


class Infinity(Main):
    def __init__(self):
        super().__init__()
        self.infinity_likes_pause = True
        self.infinity_likes_running = True
        self.real_amount_of_photo = 10
        self.profiles_name = 'julia_bernada'

        self.delay = 0.5  # in second
        self.resume_key = keyboard.Key.space
        self.pause_key = keyboard.Key.space
        self.make_key = keyboard.Key.enter
        self.restart_key = keyboard.Key.shift
        self.return_key = keyboard.Key.tab

    # make tab
    def instagram_search(self):
        """
        open instagram, open profiles name and click on first photo
        """
        # open instagram and profiles_name
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome"
                                                                         "\Application\chrome.exe"))
        webbrowser.get('Chrome').open('instagram.com/' + self.profiles_name + '/')

        time.sleep(10)  # make infinity_likes_pause for 10 seconds
        pyautogui.click(344, 742)  # click on the first photo

    # infinity_likes function
    def infinity_likes_on_press(self, key):
        """
        resume_key: start infinity_likes
        pause_key: stop infinity_likes
        make_key: make new tab
        restart_key: make distance and restart infinity_likes
        return_key: make distance and activate MENU
        """
        if key == self.resume_key and self.infinity_likes_pause == True:  # stop pause
            print("[Resumed]")
            self.infinity_likes_pause = False
        elif key == self.pause_key and self.infinity_likes_pause == False:  # make pause
            print("[Paused]")
            self.infinity_likes_pause = True
        elif key == self.make_key:  # activate infinity_likes_display_instagram_search
            self.instagram_search()  # make new tab
            print('[Made_new_tab]')
        elif key == self.restart_key:  # restart infinity_likes_main
            print(self.distanation, self.distanation, self.distanation)  # make distance
            self.infinity_likes_running = True
            Infinity_main().infinity_likes_main()
            print("[Restarted]")
        elif key == self.return_key:  # return MENU
            print("[Exit]")
            print(self.distanation, self.distanation, self.distanation, self.distanation, )  # make distance
            self.pause = True
            self.main()

    # infinity_likes design
    def infinity_likes_display_controls(self):
        """
        return: AutoInstagramClicker on display
        """
        print("-------------------------------------------AutoInstagramClicker---------------------------------------")
        print("// - Settings: ")
        print("\t delay = " + str(self.delay) + ' sec' + '\n')
        print("// - Controls:")
        print('\t Space = Resume')
        print("\t Space = Pause")
        print("\t Enter = Make new tab")
        print("\t Shift = Restart")
        print("\t Tab = Return to MainMenu           ")
        print("------------------------------------------------------------------------------------------------------")
        print('Press Space to start ...')


class Infinity_main(Infinity):
    def infinity_likes_main(self):
        """
        coupe infinity_likes_on_press(function) and infinity_likes_display_controls(design)
        """
        lis = keyboard.Listener(on_press=self.infinity_likes_on_press)  # prepare infinity_likes_on_press
        lis.start()  # activate infinity_likes_on_press
        amount_of_photo = self.real_amount_of_photo  # as global
        self.infinity_likes_display_controls()  # activate infinity_likes_display_controls
        while self.infinity_likes_running:  # while infinity_likes_running = true
            for i in range(amount_of_photo):  # make cycle
                if not self.infinity_likes_pause:  # if infinity_likes_pause = false
                    pyautogui.doubleClick(493, 454)  # like photo
                    pyautogui.click(1170, 425)  # click next photo

                    amount_of_photo -= 1
                    print('Left Photo: ' + str(amount_of_photo))  # print How much photo leave
                    pyautogui.PAUSE = self.delay  # make pause for delay
        lis.stop()  # stop infinity_likes_on_press


if __name__ == "__main__":
    Main().main()
