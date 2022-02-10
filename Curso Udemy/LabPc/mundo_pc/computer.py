from keboard import Keyboard
from Screen import Screen



class Computer:
    computer_counter = 0

    def __init__(self, name, screen, keyboard, mouse):
        Computer.computer_counter += 1
        self._id_computer = Computer.computer_counter
        self._name = name
        self._screen = screen
        self._keyboard = keyboard
        self._mouse = mouse


    def  __str__(self):
        return f'''
        {self._name}: {self._id_computer}
        Screen: {self._screen}
        Keyboard: {self._keyboard}
        Mouse: {self._mouse}'''


if __name__ == '__main__':
    keboard1= Keyboard('k1', 'USB')
    # mouse1 = Mouse('M1', 'wireless')
    screen1= Screen('s1',23)


