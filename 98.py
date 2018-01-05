import tkinter as tk

window = tk.Tk()
window.wm_title("Text Saving App")
window.bind('<Return>', lambda e: add_line())


def add_line():
    global entry_list
    entry = text_input.get()
    entry_list.append(entry)
    e1.delete(0, tk.END)


def save_changes():
    if text_input.get():
        add_line()
    global entry_list
    file = open('ex_98.txt', 'a+')
    for entry in entry_list:
        file.writelines(entry + '\n')
    entry_list = []
    file.close()


def save_and_close():
    save_changes()
    window.quit()


entry_list = []

text_input = tk.StringVar()
e1 = tk.Entry(window, textvariable=text_input)
e1.grid(column=0, row=0)

b1 = tk.Button(window, text='Add Line', command=add_line)
b1.grid(column=1, row=0)

b2 = tk.Button(window, text='Save Changes', command=save_changes)
b2.grid(column=2, row=0)

b3 = tk.Button(window, text='Save and Close', command=save_and_close)
b3.grid(column=3, row=0)

window.mainloop()
