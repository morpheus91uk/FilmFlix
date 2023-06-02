
import tkinter as tk
import tkinter.font as tkFont
from menu import *

class App:
    def __init__(self, root):
        #setting title
        root.title("FilmFlixInterface")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        # This should be the code to update the display label. 
        display_value = tk.StringVar()
        
        # This is the tkinter code for the display.
        display=tk.Label(root, textvariable = display_value)
        display["bg"] = "#fb9f9f"
        ft = tkFont.Font(family='Times', size=10)
        display["font"] = ft
        display["fg"] = "#333333"
        display["justify"] = "center"
        display["text"] = "This is the Display?"
        display.place(x=10, y=20, width = 580, height=260)
        display.pack()
        
        # This is the tkinter code for the entry box.
        entry_box = tk.Entry(root)
        entry_box["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size = 10)
        entry_box["font"] = ft
        entry_box["fg"] = "#333333"
        entry_box["justify"] = "center"
        entry_box["text"] = "Entry"
        entry_box.place(x= 170, y= 320, width = 250, height = 25)
        
        # This is the tkinter code for the submit button
        submit_Btn = tk.Button(root)
        submit_Btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family = "Times", size =10)
        submit_Btn["font"] = ft
        submit_Btn["fg"] = "#000000"
        submit_Btn["justify"] = "center"
        submit_Btn["text"] = "Submit"
        submit_Btn.place(x= 260, y= 380, width = 70, height = 25)
        submit_Btn["command"] = self.submit_Btn_command
        
        # This is the tkinter code for the label above the submit button
        submit_label = tk.Label(root)
        ft = tkFont.Font(family = "Times", size = 10)
        submit_label["font"] = ft
        submit_label["fg"] = "#333333"
        submit_label["justify"] = "center"
        submit_label["text"] = "Enter Commands Below"
        submit_label.place(x= 180, y= 290, width = 225, height = 30)
        
    # This is the function for the submit button
    def submit_Btn_command(self):
        print("command")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    menu_options()
    root.mainloop()
    
