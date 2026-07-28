import tkinter as tks
import tkinter.font as tfont

window = tks.Tk()
window.title("Honey singh munariya")
window.minsize(width = 400, height= 1000)
custome_font = tfont.Font(family = "Times New Roman", size =15, weight= 'bold')
labl = tks.Label(text = "Honey", font=custome_font)
labl.pack()

labl["text"] = "Hii my name is Honey singh munariya"
labl.config(text = 'Honey is my second name...')

window.mainloop()

