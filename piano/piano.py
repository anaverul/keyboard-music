try:
    from Tkinter import Tk, Frame, BOTH, Label, PhotoImage
except ImportError:
    from tkinter import Tk, Frame, BOTH, Label, PhotoImage

import simpleaudio as sa

import time as t

from _thread import start_new_thread

# importing this to reference BACKSPACE key
from selenium.webdriver.common.keys import Keys

start = t.time()

file = open('songs/song.txt', 'w')
file.close()

recording = False
def label_pressed(event):
    if len(event.widget.name) == 2:
        img = 'pictures/white_key_pressed.gif'
    elif len(event.widget.name) == 3:
        img = 'pictures/black_key_pressed.gif'
    elif event.widget.name == 'red_button':
        img = 'pictures/red_button_pressed.gif'
    else:
        img = 'pictures/green_button_pressed.gif'
    key_img = PhotoImage(file=img)
    event.widget.configure(image=key_img)
    event.widget.image = key_img

def label_released(event):
    if len(event.widget.name) == 2:
        img = 'pictures/white_key.gif'
    elif len(event.widget.name) == 3:
        img = 'pictures/black_key.gif'
    elif event.widget.name == 'red_button':
        img = 'pictures/red_button.gif'
    else:
        img = 'pictures/green_button.gif'
    key_img = PhotoImage(file=img)
    event.widget.configure(image=key_img)
    event.widget.image = key_img

def play(file_name):
    song_file = open(file_name, 'r')
    print("Playback Started")
    first_line = song_file.readline().split()
    note = first_line[0]
    time_scale = float(first_line[1])
    for line in song_file:
        wave_obj = sa.WaveObject.from_wave_file('sounds/' + note + '.wav')
        wave_obj.play()
        line_elements = line.split()
        note = line_elements[0]
        time = float(line_elements[1])
        t.sleep(time - time_scale)
        time_scale = time
    wave_obj = sa.WaveObject.from_wave_file('sounds/' + note + '.wav')
    wave_obj.play()
    print("Playback Stopped")

# def play_back(event):
#     if event.char == '1':
#         start_new_thread(play, ('songs/1.txt',))
#     elif event.char == '2':
#         start_new_thread(play, ('songs/2.txt',))
#     else:
#         label_pressed(event)

#         start_new_thread(play, ('songs/song.txt',))

def record_on_off(event):
    global recording
    recording = not recording
    print('Recording: ', recording)
    if recording:
        label_pressed(event)
    else:
        label_released(event)

def record(file_name, note):
    song_file = open(file_name, 'a')
    end = t.time()
    time = end - start
    song_file.write(note + ' ' + str(time))
    song_file.write('\n')

def find_label(name, array):
    for x in range(len(array)):

        if name == array[x][1]:

            return array[x][2]

def key_pressed(event):
    note = KEYS_TO_NOTES.get(event.char, None)
    if note:
        wave_obj = sa.WaveObject.from_wave_file('sounds/' + note + '.wav')
        wave_obj.play()
        print(note)
        if recording:
            record('songs/song.txt', note)
        if len(note) == 2:
            img = 'pictures/white_key_pressed.gif'
        else:
            img = 'pictures/black_key_pressed.gif'
        key_img = PhotoImage(file=img)
        find_label(note, event.widget.keys).configure(image=key_img)
        find_label(note, event.widget.keys).image = key_img

def key_released(event):
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
    wave_obj = sa.WaveObject.from_wave_file('sounds/' + event.widget.name + '.wav')
    wave_obj.play()
    print(event.widget.name)
    if recording:
        record('songs/song.txt', event.widget.name)
    label_pressed(event)

KEYS_TO_NOTES = {
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
    '1': 'Db3',
    '2': 'Eb3',
    '4': 'Gb3',
    '5': 'Ab3',
    '6': 'Bb3',
    '8': 'Db4',
    '9': 'Eb4',
    '-': 'Gb4',
    '=': 'Ab4',
    Keys.BACKSPACE : 'Ab4', 
    Keys.BACK_SPACE : 'Ab4',
    Keys.DELETE : 'Ab4',
    'Keys.BACKSPACE' : 'Ab4',
    'Keys.BACK_SPACE' : 'Ab4',
    'Keys.DELETE' : 'Ab4',
}

# Keys.BACKSPACE : 'Ab4'
#2 Eb3
#6 Bb3
#9 Eb4

class Piano(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent, background='SkyBlue3')

        self.parent = parent


        self.init_user_interface()

    def init_user_interface(self):

        keys = [
            [0, 'C3'],
            [35, 'Cb3'],
            [50, 'D3'],
            [85, 'Db3'],
            [100, 'E3'],
            [150, 'F3'],
            [185, 'Fb3'],
            [200, 'G3'],
            [235, 'Gb3'],
            [250, 'A3'],
            [285, 'Ab3'],
            [300, 'B3'],
            [350, 'C4'],
            [385, 'Cb4'],
            [400, 'D4'],
            [435, 'Db4'],
            [450, 'E4'],
            [500, 'F4'],
            [535, 'Fb4'],
            [550, 'G4'],
            [585, 'Gb4'],
            [600, 'A4'],
            [635, 'Ab4'],
            [650, 'B4'] 
        ]

        for key in keys:
            if len(key[1]) == 2:
                img = 'pictures/white_key.gif'
                key.append(self.create_key(img, key))

        for key in keys:
            if len(key[1]) > 2:
                img = 'pictures/black_key.gif'
                key.append(self.create_key(img, key))

        img = PhotoImage(file='pictures/red_button.gif')
        record_button = Label(self, image=img, bd=0)
        record_button.image = img
        record_button.place(x=700, y=0)
        record_button.name = 'red_button'
        record_button.bind('<Button-1>', record_on_off)

        img = PhotoImage(file='pictures/green_button.gif')
        play_button = Label(self, image=img, bd=0)
        play_button.image = img
        play_button.place(x=700, y=50)
        play_button.name = 'green_button'
        # play_button.bind('<Button-1>', play_back)
        play_button.bind('<ButtonRelease-1>', label_released)

        self.parent.title('The Piano')

        w = 750
        h = 200
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.parent.keys = keys
        self.parent.bind('<KeyPress>', key_pressed)
        self.parent.bind('<KeyRelease>', key_released)

        # self.parent.bind('1', play_back)
        # self.parent.bind('2', play_back)

        self.pack(fill=BOTH, expand=1)

    def create_key(self, img, key):
        key_image = PhotoImage(file=img)
        label = Label(self, image=key_image, bd=0)
        label.image = key_image
        label.place(x=key[0], y=0)
        label.name = key[1]
        label.bind('<Button-1>', button_pressed)
        label.bind('<ButtonRelease-1>', label_released)
        return label

def main():
    root = Tk()
    app = Piano(root)
    app.mainloop()

if __name__ == '__main__':
    main()
