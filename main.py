import pydirectinput
from time import sleep
import keyboard

pressed = []

def holdKey(key, time):
    pydirectinput.keyDown(key)
    sleep(time)
    pydirectinput.keyUp(key)

def resolve(combine):
    if combine == "01":
        print("Drop item")
        pydirectinput.press("a")
    elif combine == "02":
        print("Walk forward")
        holdKey("w", 0.1)
    elif combine == "03":
        print("Open inventory")
        pydirectinput.press("e")
    elif combine == "07":
        print("Walk left")
        holdKey("q", 0.1)
    elif combine == "08":
        print("Walk backward")
        holdKey("s", 0.1)
    elif combine == "09":
        print("Walk right")
        holdKey("d", 0.1)
    elif combine == "04":
        print("Jump")
        pydirectinput.press("space")
    elif combine == "05":
        print("Left Click")
        pydirectinput.press("n")
    elif combine == "06":
        print("Right Click")
        pydirectinput.rightClick()
    elif combine == "10":
        print("Sprint")
        pydirectinput.press("ctrl")
    elif combine == "11":
        print("Sneak")
        pydirectinput.press("shift")
    elif combine == "13":
        print("Esc")
        pydirectinput.press("esc")
    elif combine == "12":
        if keyboard.is_pressed("n"):
            pydirectinput.keyUp("n")
        else:
            pydirectinput.keyDown("n")
    else:
        print(f"Can't resolve {combine}")

while True:
    key = keyboard.read_event()
    
    if key.event_type != keyboard.KEY_DOWN:
        continue

    if key.name.isnumeric():
        pressed.append(key.name)

    if key.name == "enter":
        combine = "".join(pressed)
        resolve(combine)
        pressed = []