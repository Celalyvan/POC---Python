from entry_device import EntryDevice

class Keyboard(EntryDevice):

    keyboard_counter = 0

    def __init__(self, brand, entry_type):
        Keyboard.keyboard_counter += 1
        self._id_keyboard = Keyboard.keyboard_counter
        super().__init__(brand, entry_type)


    def __str__(self):
        return f'id: {self._id_keyboard}, brand: {self._brand}, entry: {self._entry_type}'


keyboard = Keyboard('genius', 'USB')
print(keyword1)
keyboard2 = Keyboard('hp', 'wireless')
print(keyword2)
