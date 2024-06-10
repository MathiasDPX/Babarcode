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
 
# Zzz... boring
def resolve(combine):
    if combine == "01":
        stats['Left'] += 1
        pydirectinput.press("a")
    elif combine == "02":
        stats['Forward'] += 1
        holdKey("w", walking_duration)
    elif combine == "03":
        stats['Inventory'] += 1
        pydirectinput.press("e")
    elif combine == "07":
        stats['Right'] += 1
        holdKey("q", walking_duration)
    elif combine == "08":
        stats['Backward'] += 1
        holdKey("s", walking_duration)
    elif combine == "09":
        stats['Right'] += 1
        holdKey("d", walking_duration)
    elif combine == "04":
        stats['Jump'] += 1
        pydirectinput.press("space")
    elif combine == "05":
        stats['LMB'] += 1
        pydirectinput.press(lmb)
    elif combine == "06":
        stats['RMB'] += 1
        pydirectinput.press(rmb)
    elif combine == "10":
        stats['Ctrl'] += 1
        pydirectinput.press("ctrl")
    elif combine == "11":
        stats['Shift'] += 1
        pydirectinput.press("shift")
    elif combine == "13":
        stats['Escape'] += 1
        pydirectinput.press("esc")
    elif combine == "12":
        # pydirectinput doesn't have mouseLeftUp nor mouseLeftDown
        if keyboard.is_pressed(lmb):
            stats['Long LMB'] += 1
            pydirectinput.keyUp(lmb)
        else:
            pydirectinput.keyDown(lmb)
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
    for stat, value in stats.items():
        print(f"{stat}: {value}")
    exit()