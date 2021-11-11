#Libraries

import random
import time
import keyboard as keyboard_input
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

#Keyboard and mouse

keyboard = KeyboardController()
mouse = MouseController()

#Letter

vowels = ['', 'a', 'e', 'i', 'o', 'u']
consonants = ['', 'n', 'r', 't', 'l', 'c', 'b']

#Mouse Position

add_tab = [1081, 16]
search_bar = [609, 382]
close_tab = [1039, 18]
#Countdown before start

time.sleep(10)

#Function


def search():
    # Variable with how many time the bot search
    how_many_search = 0
    while True:
        #Generate word

        word = [consonants[random.randint(1, 6)], vowels[random.randint(1, 5)], consonants[random.randint(1, 6)], consonants[random.randint(1, 6)], vowels[random.randint(1, 5)], vowels[random.randint(1, 5)]]
        wordstr = ' '.join([str(elem) for elem in word])
        wordstr.replace(' ', '', 5)
        #Search

        mouse.position = (add_tab[0], add_tab[1])
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.position = (search_bar[0], search_bar[1])
        time.sleep(2)
        mouse.press(Button.left)
        mouse.release(Button.left)
        keyboard.type(wordstr)
        for space in range(5):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        mouse.position = (close_tab[0], close_tab[1])
        time.sleep(3)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1)
        how_many_search = how_many_search + 1
        print(how_many_search)


search()
while True:
    if keyboard_input.is_pressed('a'):
        quit()
