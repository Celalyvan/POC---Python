from entry_device import EntryDevice

class Mouse(EntryDevice):
    mouse_counter = 0

    def __init__(self, brand, entry_type):
        Mouse.mouse_counter += 1
        self._id_mouse = Mouse.mouse_counter
        super().__init__(brand, entry_type)

    def __str__(self):
        return f'Id {self._id_mouse}, brand: {self._brand}, entry: {self._entry_type}'


mouse1 = Mouse('hp', 'USB')
print(mouse1)
mouse2 = Mouse('acer', 'BT')
print(mouse2)