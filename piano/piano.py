try:
    from Tkinter import Tk, Frame, BOTH, Label, PhotoImage
except ImportError:
    from tkinter import Tk, Frame, BOTH, Label, PhotoImage
from pygame import mixer

def label_pressed(event):
    #changes the graphical interface whenever a label is pressed
    if len(event.widget.name) == 2:
        img = 'pictures/white_key_pressed.gif'
    elif len(event.widget.name) == 3:
        img = 'pictures/black_key_pressed.gif'
    key_img = PhotoImage(file=img)
    event.widget.configure(image=key_img)
    event.widget.image = key_img

def label_released(event):
    #changes the graphical interface whenever a label is released
    if len(event.widget.name) == 2:
        img = 'pictures/white_key.gif'
    elif len(event.widget.name) == 3:
        img = 'pictures/black_key.gif'
    key_img = PhotoImage(file=img)
    event.widget.configure(image=key_img)
    event.widget.image = key_img


def find_label(name, array):
    for x in range(len(array)):

        if name == array[x][1]:

            return array[x][2]

def key_pressed(event):
    #changes the graphical interface whenever a key is pressed
    note = KEYS_TO_NOTES.get(event.char, None)
    if note:
        mixer.init()
        wave_obj = mixer.Sound('sounds/' + note + '.wav')
        wave_obj.play()
        print(note)
        if len(note) == 2:
            img = 'pictures/white_key_pressed.gif'
        else:
            img = 'pictures/black_key_pressed.gif'
        key_img = PhotoImage(file=img)
        find_label(note, event.widget.keys).configure(image=key_img)
        find_label(note, event.widget.keys).image = key_img

def key_released(event):
    #changes the graphical interface whenever a key is released
    note = KEYS_TO_NOTES.get(event.char, None)
    if note:
        if len(note) == 2:
            img = 'pictures/white_key.gif'
        else:
            img = 'pictures/black_key.gif'
        key_img = PhotoImage(file=img)
        find_label(note, event.widget.keys).configure(image=key_img)
        find_label(note, event.widget.keys).image = key_img

def button_pressed(event):
    #plays sound during an event (i.e. key/label is pressed)
    mixer.init()
    wave_obj=mixer.Sound('sounds/' + event.widget.name + '.wav')
    wave_obj.play()
    print(event.widget.name)

KEYS_TO_NOTES = {
    'z': 'C2',
    'x': 'D2',
    'c': 'E2',
    'v': 'F2',
    'b': 'G2',
    'n': 'A2',
    'm': 'B2',

    's': 'Db2',
    'd': 'Eb2',
    'g': 'Gb2',
    'h': 'Ab2',
    'j': 'Bb2',

    '\t': 'C3',
    'q': 'D3',
    'w': 'E3',
    'e': 'F3',
    'r': 'G3',
    't': 'A3',
    'y': 'B3',
    'u': 'C4',
    'i': 'D4',
    'o': 'E4',
    'p': 'F4',
    '[': 'G4',
    ']': 'A4',
    '\\': 'B4',

    '`': 'Db3',
    '1': 'Eb3',
    '3': 'Gb3',
    '4': 'Ab3',
    '5': 'Bb3',
    '7': 'Db4',
    '8': 'Eb4',
    '0': 'Gb4',
    '-': 'Ab4',
    '=': 'Bb4',
}

class Piano(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent, background='SkyBlue3')

        self.parent = parent


        self.init_user_interface()

    def init_user_interface(self):
        self.create_mapping()

        keys = [   #provides locations of keys on the GUI
    [0, 'C2'],
    [35, 'Db2'],
    [50, 'D2'],
    [85, 'Eb2'],
    [100, 'E2'],
    [150, 'F2'],
    [185, 'Gb2'],
    [200, 'G2'],
    [235, 'Ab2'],
    [250, 'A2'],
    [285, 'Bb2'],
    [300, 'B2'],
    [350, 'C3'],
    [385, 'Db3'],
    [400, 'D3'],
    [435, 'Eb3'],
    [450, 'E3'],
    [500, 'F3'],
    [535, 'Gb3'],
    [550, 'G3'],
    [585, 'Ab3'],
    [600, 'A3'],
    [635, 'Bb3'],
    [650, 'B3'],
    [700, 'C4'],
    [735, 'Db4'],
    [750, 'D4'],
    [785, 'Eb4'],
    [800, 'E4'],
    [850, 'F4'],
    [885, 'Gb4'],
    [900, 'G4'],
    [935, 'Ab4'],
    [950, 'A4'],
    [985, 'Bb4'],
    [1000, 'B4']

]

        for key in keys:
            if len(key[1]) == 2:
                img = 'pictures/white_key.gif'
                key.append(self.create_key(img, key))

        for key in keys:
            if len(key[1]) > 2:
                img = 'pictures/black_key.gif'
                key.append(self.create_key(img, key))

        self.parent.title('The Piano')

        w = 1050
        h = 624
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        #Centers the GUI in the middle of the screen
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.parent.keys = keys
        self.parent.bind('<KeyPress>', key_pressed)
        self.parent.bind('<KeyRelease>', key_released)


        self.pack(fill=BOTH, expand=1)

    def create_key(self, img, key):
        key_image = PhotoImage(file=img)
        label = Label(self, image=key_image, bd=0)
        label.image = key_image
        label.place(x=key[0], y=424)
        label.name = key[1]
        label.bind('<Button-1>', button_pressed)
        label.bind('<ButtonRelease-1>', label_released)
        return label

    def create_mapping(self):
        #adds the key mapping image on the GUI
        path_to_mapping ='pictures/mapping.gif'
        mapping_image = PhotoImage(file=path_to_mapping)
        label = Label(self, image = mapping_image, bd=0)
        label.image = mapping_image
        label.place(x=0, y=0)
        return label


def main():
    root = Tk()
    app = Piano(root)
    app.mainloop()

if __name__ == '__main__':
    main()
