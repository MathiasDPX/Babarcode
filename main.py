import pydirectinput # pyautogui doesnt work
from time import sleep
import keyboard

walking_duration = 0.1
lmb = "n"
rmb = "b"

stats = {}

def holdKey(key, time):
    pydirectinput.keyDown(key)
    sleep(time)
    pydirectinput.keyUp(key)

def increment(key:str, value:int):
    try:
        stats[key] += value
    except KeyError:
        stats[key] = value

# Zzz... boring
def resolve(combine):
    if combine == "01":
        increment('Drop', 1)
        pydirectinput.press("q")
    elif combine == "02":
        increment("Forward", 1)
        holdKey("w", walking_duration)
    elif combine == "03":
        increment("Inventory", 1)
        pydirectinput.press("e")
    elif combine == "07":
        increment("Left", 1)
        holdKey("a", walking_duration)
    elif combine == "08":
        increment("Backward", 1)
        holdKey("s", walking_duration)
    elif combine == "09":
        increment("Right", 1)
        holdKey("d", walking_duration)
    elif combine == "04":
        increment("Jump", 1)
        pydirectinput.press("space")
    elif combine == "05":
        increment("LMB", 1)
        pydirectinput.press(lmb)
    elif combine == "06":
        increment("RMB", 1)
        pydirectinput.press(rmb)
    elif combine == "10":
        increment("Ctrl", 1)
        pydirectinput.press("ctrl")
    elif combine == "11":
        increment("Shift", 1)
        pydirectinput.press("shift")
    elif combine == "13":
        increment("Esc", 1)
        pydirectinput.press("esc")
    elif combine == "12":
        # pydirectinput doesn't have mouseLeftUp nor mouseLeftDown
        if keyboard.is_pressed(lmb):
            increment("Long LMB", 1)
            pydirectinput.keyUp(lmb)
        else:
            pydirectinput.keyDown(lmb)
    elif combine == "14": # Eat
        increment("Eat", 1)
        holdKey(rmb, 1.61)
    elif combine == "15":
        # pydirectinput doesn't have mouseLeftUp nor mouseLeftDown
        if keyboard.is_pressed(lmb):
            increment("Long RMB", 1)
            pydirectinput.keyUp(rmb)
        else:
            pydirectinput.keyDown(rmb)
    else:
        print(f"Can't resolve {combine}")

# Useful
pressed = []
try:
    while True:
        key = keyboard.read_event()
        
        if key.event_type != keyboard.KEY_DOWN:
            continue

        # so you can type in chat
        if key.name.isnumeric():
            pressed.append(key.name)

        # Enter or any terminator
        if key.name == "enter":
            combine = "".join(pressed)
            resolve(combine)
            pressed = []
except KeyboardInterrupt:
    print("--STATS:")
    for stat, value in stats.items():
        print(f"{stat}: {value}")
    exit()