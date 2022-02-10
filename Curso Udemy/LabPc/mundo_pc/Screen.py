class Screen:

    screen_counter = 0

    def __init__(self, brand, size):
        Screen.screen_counter +=1
        self._id_screen = Screen.screen_counter
        self._brand = brand
        self._size = size

    def __str__(self):
        return f'Id {self._id_screen}, brand: {self._brand}, entry: {self._size}'


if __name__ =='__main__':
    screen1 = Screen('lg', 21)
    print(screen1)
    screen1 = Screen('acer', 27)
    print(screen1)
    