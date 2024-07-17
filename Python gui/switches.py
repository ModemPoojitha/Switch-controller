import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Switch Control")

# Load images
on_image = ImageTk.PhotoImage(Image.open("C:/Users/M Poojitha/Downloads/on.png").resize((100, 100), Image.ANTIALIAS))
off_image = ImageTk.PhotoImage(Image.open("C:/Users/M Poojitha/Downloads/off.png").resize((100, 100), Image.ANTIALIAS))

# Create switches and bulbs
switch_frames = []
bulb_images = []
switch_buttons = []

switches = ["OFF"] * 16

def turn_on(switch_number):
    switches[switch_number-1] = "ON"
    bulb_images[switch_number-1].config(image=on_image)
    switch_buttons[switch_number-1].config(text=" ON ")

def turn_off(switch_number):
    switches[switch_number-1] = "OFF"
    bulb_images[switch_number-1].config(image=off_image)
    switch_buttons[switch_number-1].config(text="OFF")

def toggle_bulb(switch_number):
    if switches[switch_number-1] == "ON":
        turn_off(switch_number)
    else:
        turn_on(switch_number)


operations = {
    "ON": turn_on,
    "OFF": turn_off,
}


for i in range(4):
    for j in range(4):
        switch_frame = tk.Frame(root)
        switch_frame.grid(row=i, column=j*2, padx=5, pady=5)
        switch_label = tk.Label(switch_frame, text="Switch " + str(4*i+j+1))
        switch_label.pack(side=tk.LEFT)
        switch_button = tk.Button(switch_frame, command=lambda switch_number=4*i+j+1: toggle_bulb(switch_number),text="OFF", width=10)
        switch_button.pack(side=tk.LEFT, padx=5)
        bulb_image = tk.Label(root, image=off_image)
        bulb_image.grid(row=i, column=j*2+1, padx=5, pady=5)
        switch_frames.append(switch_frame)
        bulb_images.append(bulb_image)
        switch_buttons.append(switch_button)

root.mainloop()