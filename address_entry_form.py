import tkinter as tk 

window = tk.Tk()

window.title('Address Entry Form')

data = ["First Name",'Last Name','Address Line 1','Address Line 2','City','State/Province','Postal Code','Country']
frame_lbl = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frame_lbl.pack()

for i, name in enumerate(data):
    name_entry = name + "_entry"

    name = tk.Label(master=frame_lbl, text=f"{name}:")
    name.grid(row=i, column=0, sticky='e')

    name_entry = tk.Entry(master=frame_lbl, width=50)
    name_entry.grid(row=i, column=1)

frame_btn = tk.Frame()
frame_btn.pack(fill=tk.X, ipadx=5, ipady=5)
btn_submit = tk.Button(master=frame_btn, text="Submit")
btn_clear = tk.Button(master=frame_btn, text="Clear")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
btn_clear.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()

