import tkinter as tk
from random import randrange

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Guess The Word")

        self.textBox1 = tk.Entry(self)
        self.textBox2 = tk.Entry(self)

        
        def word():
            global word_R,word_A,h,db
            word_list = ["wolf","cat","dog"]
            rand = randrange(3)
            word_R = word_list[rand]
            word_A=""
            db=0
            h=len(word_R)
            for i in range(h):
                word_A+="?"
            self.textBox2.delete(0,tk.END)
            self.textBox2.insert(0,word_A)

        def summary():
             global word_R,word_A,h,db
             guess = self.textBox1.get()
             guess = guess.lower()
             prev = word_A
             word_A = ""
             for i in range(h):
                     if guess[0]==word_R[i]:
                         word_A+=guess[0]
                         db+=1
                     else:
                         word_A+=prev[i]

             self.textBox2.delete(0,tk.END)
             self.textBox2.insert(0,word_A)
             self.textBox1.delete(0,tk.END)
             if db == h: #don't enter the same guessed letter again if you've guessed it well
                self.textBox1.insert(0,"You've won!")


        self.button1 = tk.Button(self,text="New word",command=word)
        self.button2 = tk.Button(self, text="Next letter",command=summary)
        self.button3 = tk.Button(self, text="Exit", command=self.destroy)
        self.label1 = tk.Label(self, text="Guessed letter: ")
        self.label2 = tk.Label(self, text="The word: ")
        

        self.button1.grid(row=3,column=1)
        self.button2.grid(row=3,column=2)
        self.button3.grid(row=3,column=3)
        self.label1.grid(row=1,column=1,sticky="E")
        self.label2.grid(row=2,column=1,sticky="E")
        self.textBox1.grid(row=1,column=2)
        self.textBox2.grid(row=2,column=2)

        for i in range(4):
            self.columnconfigure(i,pad=10)
            self.rowconfigure(i,pad=5)


if __name__=="__main__":
    window = App()
    window.mainloop()
