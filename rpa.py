import webbrowser
import pyautogui as pa
import pyperclip
import time

url = "https://www.google.com"

webbrowser.open(url, new=0, autoraise=True)
pa.moveTo(660, 450, 1)
pyperclip.copy("平泉 観光")
pa.hotkey("ctrl", "v")
pa.hotkey("enter")
time.sleep(3)
screen_shot = pa.screenshot()
screen_shot.save("test.png")
