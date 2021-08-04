from tkinter import *
import backend
from tkinter import filedialog as fd
C_driv = ""

def btn_search():
    print("Button Clicked")
    backend.search(C_driv)

def btn_start():
    print("start")
    backend.start(entry0.get().upper(), entry8.get(), entry9.get() ,entry1.get(),
                   entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get())


window = Tk()

window.geometry("747x542")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 542,
    width = 747,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"./images/background.png")
background = canvas.create_image(
    373.5, 76.5,
    image=background_img)

entry0_img = PhotoImage(file = f"./images/img_textBox0.png")
entry0_bg = canvas.create_image(
    409.0, 182.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 244, y = 170,
    width = 330,
    height = 23)

entry1_img = PhotoImage(file = f"./images/img_textBox1.png")
entry1_bg = canvas.create_image(
    409.0, 277.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 244, y = 265,
    width = 330,
    height = 23)

entry2_img = PhotoImage(file = f"./images/img_textBox2.png")
entry2_bg = canvas.create_image(
    409.0, 309.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry2.place(
    x = 244, y = 297,
    width = 330,
    height = 23)

entry3_img = PhotoImage(file = f"./images/img_textBox3.png")
entry3_bg = canvas.create_image(
    409.0, 339.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry3.place(
    x = 244, y = 327,
    width = 330,
    height = 23)

entry4_img = PhotoImage(file = f"./images/img_textBox4.png")
entry4_bg = canvas.create_image(
    409.0, 369.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry4.place(
    x = 244, y = 357,
    width = 330,
    height = 23)

entry5_img = PhotoImage(file = f"./images/img_textBox5.png")
entry5_bg = canvas.create_image(
    409.0, 400.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry5.place(
    x = 244, y = 388,
    width = 330,
    height = 23)

entry6_img = PhotoImage(file = f"./images/img_textBox6.png")
entry6_bg = canvas.create_image(
    409.0, 431.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry6.place(
    x = 244, y = 419,
    width = 330,
    height = 23)

entry7_img = PhotoImage(file = f"./images/img_textBox7.png")
entry7_bg = canvas.create_image(
    409.0, 463.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry7.place(
    x = 244, y = 451,
    width = 330,
    height = 23)

entry8_img = PhotoImage(file = f"./images/img_textBox8.png")
entry8_bg = canvas.create_image(
    409.0, 213.5,
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry8.place(
    x = 244, y = 201,
    width = 330,
    height = 23)

entry9_img = PhotoImage(file = f"./images/img_textBox9.png")
entry9_bg = canvas.create_image(
    409.0, 245.5,
    image = entry9_img)

entry9 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry9.place(
    x = 244, y = 233,
    width = 330,
    height = 23)

canvas.create_text(
    374.0, 56.5,
    text = "PALACE BOT",
    fill = "#000000",
    font = ("Roboto-Black", int(60.0)))

canvas.create_text(
    153.5, 180.5,
    text = "Item",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    153.0, 399.5,
    text = "City",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    153.0, 431.5,
    text = "Post Code",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    153.5, 212.5,
    text = "Size",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    153.5, 242.5,
    text = "E-mail",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    153.0, 275.5,
    text = "First name",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    153.0, 307.5,
    text = "Last name",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    153.0, 337.5,
    text = "Address",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    153.0, 367.5,
    text = "Apartment",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

canvas.create_text(
    153.0, 463.5,
    text = "Phone",
    fill = "#000000",
    font = ("Roboto-Bold", int(25.0)))

img0 = PhotoImage(file = f"./images/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_search,
    relief = "flat")

b0.place(
    x = 638, y = 166,
    width = 78,
    height = 32)

img1 = PhotoImage(file = f"./images/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_start,
    relief = "flat")

b1.place(
    x = 638, y = 219,
    width = 78,
    height = 32)

# img2 = PhotoImage(file = f"./images/img2.png")
# b2 = Button(
#     image = img2,
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = btn_reset,
#     relief = "flat")

# b2.place(
#     x = 638, y = 268,
#     width = 78,
#     height = 32)
C_driv = fd.askopenfilename()
window.resizable(False, False)
window.mainloop()
