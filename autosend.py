import pyautogui
import time

words = input()                 # Your word
wait = 1                        # Time between execution program
do = 1                          # Time between repeating words    
message = 10                    # How menny messages
upper = ()                     # By defaul non letters will cange; # (1) all tetters uppercase # (2) all letters lowercase

def wordss(words):
    
    if upper == 1:
        pyautogui.typewrite(words.upper())
    elif upper == 2:
        pyautogui.typewrite(words.lower())
    else:
        pyautogui.typewrite(words)
    return words

time.sleep(wait)

while message >= 0:
    time.sleep(do)
    wordss(words)
    time.sleep(do)
    pyautogui.press('enter')
    message -= 1

