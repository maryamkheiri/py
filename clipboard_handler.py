import clipboard,keyboard
import logging
logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
import time
def gettext():
    time.sleep(0.05)
    memory.append(clipboard.paste())
    print(memory)
    clipboard.copy("")
    flag=False
def settext():
    global flag
    if len(memory)>0:
        if not flag:
            clipboard.copy("")
            clipboard.copy(memory.pop())
            flag=True
        clipboard.copy(memory.pop(0))
    else:
        clipboard.copy("")
if __name__=="__main__":
    memory=[]
    flag=False
    clipboard.copy("")
    keyboard.add_hotkey('ctrl+c',gettext)
    keyboard.add_hotkey('ctrl+v',settext)
    print("monitoring...")
    input()