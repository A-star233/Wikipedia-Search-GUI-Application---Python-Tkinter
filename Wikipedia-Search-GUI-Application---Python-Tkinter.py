from tkinter import *
from tkinter import messagebox
import wikipedia

class SearchApplication:
    def __init__(self, root):    
        self.root = root   
        self.root.title("Wikipedia Search Engine")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#262626")

        title = Label(self.root, text="Search Application", font=("times new roman", 20, "bold"), bg="white", fg="black")
        title.place(x=0, y=10, height=30, width=1350)

        lbl_search = Label(self.root, text="Search word:", font=("times new roman", 20, "bold"), bg="#262626", fg="white")
        lbl_search.place(x=30, y=55, height=35)

        self.var_search = StringVar()
        self.entry_search = Entry(self.root, textvariable=self.var_search, font=("times new roman", 20), bg="white", fg="black")
        self.entry_search.place(x=180, y=55, height=35, width=200)

        # Buttons
        Button(self.root, text="Search", command=self.searchword, font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=400, y=55, height=35, width=130)
        Button(self.root, text="Clear", command=self.clear, font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=550, y=55, height=35, width=130)
        Button(self.root, text="Enable Edit", command=self.enable, font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=700, y=55, height=35, width=180)
        Button(self.root, text="Disable Edit", command=self.disable, font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=900, y=55, height=35, width=180)

        self.lbl_mode = Label(self.root, text="MODE: ENABLED", font=("times new roman", 15, "bold"), bg="#262626", fg="red")
        self.lbl_mode.place(x=20, y=100)

        # Frame & Text Area with Scroll
        frame1 = Frame(self.root, bd=2, relief=RIDGE)
        frame1.place(x=20, y=130, width=1200, height=550)

        scrolly = Scrollbar(frame1, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_area = Text(frame1, font=("times new roman", 15), yscrollcommand=scrolly.set)
        self.txt_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_area.yview)

    def enable(self):
        self.txt_area.config(state=NORMAL)
        self.lbl_mode.config(text="MODE: ENABLED")

    def disable(self):
        self.txt_area.config(state=DISABLED)
        self.lbl_mode.config(text="MODE: DISABLED")

    def clear(self):
        self.var_search.set("")
        self.txt_area.config(state=NORMAL)
        self.txt_area.delete('1.0', END)
        self.lbl_mode.config(text="MODE: ENABLED")

    def searchword(self):
        word = self.var_search.get()
        if word == "":
            messagebox.showerror("Error", "Search field should not be empty!")
        else:
            try:
                result = wikipedia.summary(word, sentences=5)
                self.txt_area.config(state=NORMAL)
                self.txt_area.delete('1.0', END)
                self.txt_area.insert(END, result)
            except Exception as e:
                messagebox.showerror("Error", f"No result found!\n{e}")

# Run the application
root = Tk()
obj = SearchApplication(root)
root.mainloop()
