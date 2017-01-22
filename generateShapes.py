from Tkinter import * 
import random
import time

def click():
    radius = 0
    size = sizeVar.get()
    shape = shapeVar.get()
    if size == "small":
        ran1 = 10
        ran2 = 30
    elif size == "medium":
        ran1 = 30
        ran2 = 50
    else:
        ran1 = 50
        ran2 = 70

    circleNum = random.randint(1,25)

    for i in range(0, circleNum):
        d = random.randint(ran1,ran2)

        colour = colourVar.get()
        if colour == rColour:
            colour = randColour()
        else:
            colour = colour
        x = random.randint(0, 300)
        y = random.randint(0, 400)
        if shape == "circle":
            circle = cv.create_oval(x, y, x+d, y+d, fill = colour)
        elif shape == "square":
            square = cv.create_rectangle(x, y, x+d, y+d, fill = colour)
        else:
            triangle = cv.create_polygon(x, y, x+d, y, x+(d/2), y-d, fill = colour, outline = "black")

        time.sleep(0.05)
        cv.update()

def randColour():
    colour = "#"
    for i in range(0, 6):
        colour = colour + random.choice("ABCDEF0123456789")
    return colour

def clickDraw(event):
    x = event.x
    y = event.y
    d = 20
    cv.create_oval(x, y, x+d, y+d, fill = "blue")
    cv.update()

def clear():
    cv.delete("all")

#generate the holding structures
root = Tk()

mainframe = Frame(root, bg = "white")

colourFrame = LabelFrame(mainframe, text = "Choose a colour for shapes", font = ("Calibri", 14))
sizeFrame = LabelFrame(mainframe, text = "Choose a size for shapes", font = ("Calibri", 14))
shapeFrame = LabelFrame(mainframe, text = "Choose a shape to draw", font = ("Calibri", 14))

#create the widgets
cv = Canvas(mainframe, width = 300, height = 400, bg = "white")
title = Label(mainframe, text = "Random Shape Generator", font = ("Calibri", 20), bg = "white", fg = "purple")

colourVar = StringVar()

whiteRadio = Radiobutton(colourFrame, text = "White", variable = colourVar, value = "white")
yellowRadio = Radiobutton(colourFrame, text = "Yellow", variable = colourVar, value = "yellow")
blueRadio = Radiobutton(colourFrame, text = "Blue", variable = colourVar, value = "blue")
greenRadio= Radiobutton(colourFrame, text = "Green", variable = colourVar, value = "green")
redRadio = Radiobutton(colourFrame, text = "Red", variable = colourVar, value = "red")
purpleRadio = Radiobutton(colourFrame, text = "Purple", variable = colourVar, value = "purple")
rColour = randColour()
randomRadio = Radiobutton(colourFrame, text = "Random", variable = colourVar, value = rColour)
colourVar.set("white")

sizeVar = StringVar()

smallRadio = Radiobutton(sizeFrame, text = "Small", variable = sizeVar, value = "small")
mediumRadio = Radiobutton(sizeFrame, text = "Medium", variable = sizeVar, value = "medium")
bigRadio = Radiobutton(sizeFrame, text = "Large", variable = sizeVar, value = "big")
sizeVar.set("small")

shapeVar = StringVar()

cirRadio = Radiobutton(shapeFrame, text = "Circle", variable = shapeVar, value = "circle")
squRadio = Radiobutton(shapeFrame, text = "Square", variable = shapeVar, value = "square")
triRadio = Radiobutton(shapeFrame, text = "Triangle", variable = shapeVar, value = "triangle")
shapeVar.set("circle")

drawButton = Button(mainframe, text = "Draw Shapes", command = click, font = ("Calibri", 14), bg = "lightblue")
clearButton = Button(mainframe, text = "Clear", command = clear, font = ("Calibri", 14), bg = "lightblue")

#root.bind("<Button-1>", clickDraw)

#gridding
mainframe.grid()
title.grid(row=0, column=0, columnspan=3)
colourFrame.grid(row=1, column=0, pady=15, padx=10)
sizeFrame.grid(row=2, column=0, pady=15, padx=10)
shapeFrame.grid(row=3, column=0, pady=15)

whiteRadio.grid(row=0, sticky=W)
yellowRadio.grid(sticky=W)
blueRadio.grid(sticky=W)
greenRadio.grid(sticky=W)
redRadio.grid(sticky=W)
purpleRadio.grid(sticky=W)
randomRadio.grid(sticky=W)

smallRadio.grid(row=0, sticky=W)
mediumRadio.grid(sticky=W)
bigRadio.grid(sticky=W)

cirRadio.grid(row=0, sticky=W)
squRadio.grid(sticky=W)
triRadio.grid(sticky=W)

drawButton.grid(row=3, column=1, pady = 15)
clearButton.grid(row=3, column=2, pady=15)

cv.grid(row=1, column=1, rowspan=2, columnspan=2, padx=10, pady=15)

root.mainloop()

