from tkinter import *
# membuat jendela dasar
window = Tk()
window.geometry("312x323")
window.title("Calcualtor")


def btn_click(item):
 
    global expression
 
    expression = expression + str(item)
 
    input_text.set(expression)

# Fungsi 'btn_clear' mengosongkan bidang input
def btn_clear():
 
    global expression
 
    expression = ""
 
    input_text.set("")

# Fungsi 'btn_delete' menghapus satu angka
def btn_delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)
 
# 'btn_equal' menghitung ekspresi yang ada di bidang input
 
def btn_equal():
 
    global expression
 
    result = str(eval(expression)) # Fungsi 'eval' mengevaluasi ekspresi string secara langsung
 
    # anda juga dapat mengimplementasikan fungsi Anda sendiri untuk mengevaluasi ekspresi alih-alih fungsi 'eval'
 
    input_text.set(result)
 
    expression = ""
 
expression = ""
input_text = StringVar()
 
# membuat bingkai untuk kolom input
 
input_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
 
input_frame.pack(side = TOP)
 
# kolom input
 
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
 
input_field.grid(row = 0, column = 0)
 
input_field.pack(ipady = 10) #menambah ketinggian kolom input
 
# membuat 'Frame' lain untuk tombol di bawah 'input_frame'
 
btns_frame = Frame(window, width = 312, height = 272.5, bg = "white")
 
btns_frame.pack()
 
# baris pertama
 
aclear = Button(btns_frame, text = "AC", fg = "black", width = 21, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear())
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/"))

clear = Button(btns_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_delete())
 
# baris kedua
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7))
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8))
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9))
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*"))
 
# baris ketiga
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4))
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5))
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6))
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-"))
 
# baris keempat
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1))
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2))
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3))
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+"))
 
# baris kelima
 
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0))
 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("."))
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal())

# baris pertama 
aclear.grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)

divide.grid(row = 0, column = 3, padx = 1, pady = 1)

clear.grid(row = 0, column = 2, padx = 1, pady = 1)

# baris kedua
seven.grid(row = 1, column = 0, padx = 1, pady = 1)

eight.grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine.grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)

# baris ketiga
four.grid(row = 2, column = 0, padx = 1, pady = 1)
 
five.grid(row = 2, column = 1, padx = 1, pady = 1)
 
six.grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus.grid(row = 2, column = 3, padx = 1, pady = 1)

# baris keempat
one.grid(row = 3, column = 0, padx = 1, pady = 1)
 
two.grid(row = 3, column = 1, padx = 1, pady = 1)
 
three.grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus.grid(row = 3, column = 3, padx = 1, pady = 1)

# baris kelima
zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point.grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals.grid(row = 4, column = 3, padx = 1, pady = 1)

window.mainloop()