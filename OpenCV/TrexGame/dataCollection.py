import keyboard
import uuid
import time
from PIL import Image
from mss import mss

mon = {"top" : 525, "left" : 685, "width" : 250, "height" : 130}

sct = mss()
i = 0

def recordScreen(record_id, key):
    global i
    i += 1
    print(f"{key} : {i}")
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save(f"./img/{key}_{record_id}_{i}.png")

isExit = False

def exit():
    global isExit
    isExit = True

keyboard.add_hotkey("esc", callback=exit)

record_id = uuid.uuid4()

while True:

    if isExit: break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            recordScreen(record_id, "up")
            time.sleep(0.1)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            recordScreen(record_id, "down")
            time.sleep(0.1)
        elif keyboard.is_pressed("right"):
            recordScreen(record_id, "right")
            time.sleep(0.1)
    except RuntimeError: continue














