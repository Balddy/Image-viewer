from tkinter import *


root = Tk()
root.title('learn')
root.iconbitmap('C:/Users/Chemweno/Downloads/pythonicon.png')

my_img1 = ImageTk.photoImage(image.open("image/one.png"))
my_img2 = ImageTk.photoImage(image.open("image/two.png"))

image_list = [my_img1, my_img2]

my_label = Label(image = my_img1)
my_label = grid(row=0, column=0,columnspan=3)

def foward(image_number):
    global my_label
    global button_foward
    global button_back

my_label.grid_forget()
my_label = Label(image=image_list[image_number-1])
button_foward = Button(root, text=">>", command=lambda : foward(image_number + 1))
button_back = Button(root, text="<<", command=lambda: back(image_number -1))

if image_number == 5:
    button_foward = Button(root, text=">>", state=DISABLED)

my_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_foward.grid(row=1,column=2)

button.back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit", command=root.quit)
button_foward = Button(root, text=">>", command=foward)

if image_number == 1 :
    button_back = Button(root, text="<<", state=DISABLED)
    Button_back.grid(row=1, column=0)
    Button_exit.grid(row=1, column=1)
    Button_foward.grid(row=1,column=2)




root.mainloop()
