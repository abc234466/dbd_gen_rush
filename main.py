from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


image_folder = "images/"

window = Tk()
window.geometry("1200x800")
window.title("Dead by Dayligh generator rush")

canvas = Canvas(window, height=800, width=1200)
background = ImageTk.PhotoImage(Image.open("{}{}".format(image_folder, "background.jpg")))



canvas.create_image(0, 0, anchor=NW, image=background)

# NOTE: Just test draw a oval with canvas
canvas.create_oval(400, 400, 470, 470, outline="white", width=1)


skills_pngs = [
    "iconPerks_HuntressLullaby.png",
    "iconPerks_unnervingPresence.png",
    "iconPerks_ruin.png",
]

tkImages = []


# btm = Checkbutton(
#     canvas,
#     text='unnerving_presence',
#     image=unnerving_presence,
#     highlightbackground='yellow',
#     borderwidth=0,
#     takefocus=0,
#     bg='grey'
# )


def killer_perks(widget, perks):
    tk_images =perks_preconfig(perks)
    render_perks(widget, tk_images)


def perks_preconfig(perks):
    tk_images = []

    for skill in perks:
        image = "{}{}".format(image_folder, skill)
        img = Image.open(image)
        img = img.resize((70, 70))
        img = ImageTk.PhotoImage(img)
        tk_images.append(img)

    return tk_images


def render_perks(widget, images):
    frame = Frame(canvas)
    for idx, img in enumerate(images):
        label = Label(frame, image=img)
        label.image=img # keep reference to avoid garbage collection
        btm = Button(label, image=img)
        btm.pack()
        label.grid(row=0, column=idx)
    canvas.create_window(1000, 700, window=frame)


canvas.pack()
# btm.configure(activebackground = "#33B5E5", relief = FLAT)
# canvas.create_image(0, 0, anchor=NW, image=unnerving_presence)


killer_perks(canvas, skills_pngs)
window.mainloop()
