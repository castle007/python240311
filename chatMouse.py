import tkinter as tk
import pyautogui

def change_mouse_size(size):
    pyautogui.FAILSAFE = False  
    pyautogui.mouseInfo()  
    pyautogui.FAILSAFE = True  
    
    for i in range(1, pyautogui.mouseInfo()['count'] + 1):
        pyautogui._sizeDataForMouseButton(i, size, size)

def set_mouse_size():
    selected_size = size_var.get()
    if selected_size == "대":
        change_mouse_size(10)
    elif selected_size == "중":
        change_mouse_size(5)
    elif selected_size == "소":
        change_mouse_size(2)

root = tk.Tk()
root.title("마우스 크기 변경")

size_var = tk.StringVar(root)
size_var.set("대")

size_label = tk.Label(root, text="마우스 크기 선택:")
size_label.pack()

size_option = tk.OptionMenu(root, size_var, "대", "중", "소")
size_option.pack()

set_button = tk.Button(root, text="설정", command=set_mouse_size)
set_button.pack()

root.mainloop()
