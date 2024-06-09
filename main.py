import pydirectinput # pyautogui doesnt work
from time import sleep
import keyboard

walking_duration = 0.1
lmb = "n"
rmb = "b"

def holdKey(key, time):
    pydirectinput.keyDown(key)
    sleep(time)
    pydirectinput.keyUp(key)
 
# Zzz... boring
def resolve(combine):
    if combine == "01":
        print("Drop item")
        pydirectinput.press("a")
    elif combine == "02":
        print("Walk forward")
        holdKey("w", walking_duration)
    elif combine == "03":
        print("Open inventory")
        pydirectinput.press("e")
    elif combine == "07":
        print("Walk left")
        holdKey("q", walking_duration)
    elif combine == "08":
        print("Walk backward")
        holdKey("s", walking_duration)
    elif combine == "09":
        print("Walk right")
        holdKey("d", walking_duration)
    elif combine == "04":
        print("Jump")
        pydirectinput.press("space")
    elif combine == "05":
        print("Left Click")
        pydirectinput.press(lmb)
    elif combine == "06":
        print("Right Click")
        pydirectinput.press(rmb)
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
        # pydirectinput doesn't have mouseLeftUp nor mouseLeftDown
        if keyboard.is_pressed(lmb):
            pydirectinput.keyUp(lmb)
        else:
            pydirectinput.keyDown(lmb)
    else:
        print(f"Can't resolve {combine}")

# Useful
pressed = []
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