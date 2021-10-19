from tkinter import *
from DeskJamsKit import *
from PIL import Image, ImageTk

class Control(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, DrumsPage, SynthPage, bassPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(Frame, DeskJamKit):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Start Page", font=("Verdana", 12))
        label.pack(pady=10, padx=10)
        image = Image.open("images/DJSet.png")
        image = image.resize((700, 410), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
        photo = ImageTk.PhotoImage(image)
        label = Label(self, image=photo)
        label.img = photo
        label.pack()


        button1 = Button(self, text="Quit", fg="blue",
                         command=self.client_exit)
        button1.place(x=0,y=0)

        button1.config(fg="red")

        button = Button(self, text="Drums Page",
                           command=lambda: controller.show_frame(DrumsPage))
        button.place(x=300, y=100)

        button2 = Button(self, text="Synth Page",
                            command=lambda: controller.show_frame(SynthPage))
        button2.place(x=300, y=400)

        button3 = Button(self, text="Bass Page",
                            command=lambda:controller.show_frame(bassPage))
        button3.place(x=300, y=250)



class DrumsPage(Frame, DeskJamKit):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Drums Page", font=("Verdana", 12))
        label.pack(pady=10, padx=10)

        image = Image.open("images/drums.gif")
        image = image.resize((700, 410), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
        self.pic = ImageTk.PhotoImage(image)
        photo = ImageTk.PhotoImage(image)
        label = Label(self, image=photo)
        label.img = photo  # this line is not always needed, but include it anyway to prevent bugs
        label.pack()

        button1 = Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.place(x=0,y=0)

        kickbutton = Button(self, text="Kick",
                            command=self.play_kick)
        kickbutton.place(x=350, y=340)

        snarebutton = Button(self, text="Snare",
                             command=self.play_snare)
        snarebutton.place(x=450, y=250)

        hatbutton = Button(self, text="Hat",
                           command=self.play_hat)
        hatbutton.place(x=490, y=190)

        ridebutton = Button(self, text="Ride",
                            command=self.play_ride)
        ridebutton.place(x=190, y=100)

        clapbutton = Button(self, text="Clap",
                            command=self.play_clap)
        clapbutton.place(x=220, y=250)



class SynthPage(Frame, DeskJamKit):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Bass Page", font=("Verdana", 12))
        label.pack(pady=10, padx=10)

        image = Image.open("images/Synth.gif")
        image = image.resize((700, 410), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
        self.pic = ImageTk.PhotoImage(image)
        photo = ImageTk.PhotoImage(image)
        label = Label(self, image=photo)
        label.img = photo  # this line is not always needed, but include it anyway to prevent bugs
        label.pack()

        button1 = Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()

        walkIt = Button(self, text="Migos",
                        command=self.play_walkIt)
        walkIt.place(x=300, y=240)

        rockstar = Button(self, text="Post Malone",
                        command=self.play_rockstar)
        rockstar.place(x=150, y=240)

        bell = Button(self, text="Bell",
                      command=self.play_bell)
        bell.place(x=450, y=240)

class bassPage(Frame, DeskJamKit):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Guitar Page", font=("Verdana", 12))
        label.pack(pady=10, padx=10)

        image = Image.open("images/soundWave.gif")
        image = image.resize((700, 410), Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(image)
        photo = ImageTk.PhotoImage(image)
        label = Label(self, image=photo)
        label.img = photo  # this line is not always needed, but include it anyway to prevent bugs
        label.pack()

        button1 = Button(self, text="Back to Home",
                         command=lambda: controller.show_frame(HomePage))
        button1.place(x=0, y=0)

        gyalchester = Button(self, text="Gyalchester",
                        command=self.play_Gyalchester)
        gyalchester.place(x=300, y=240)

        gucci = Button(self, text="Gucci",
                            command=self.play_gucci)
        gucci.place(x=150, y=240)

        suge = Button(self, text="Suge",
                            command=self.play_suge)
        suge.place(x=450, y=240)

app = Control()
app.geometry("700x482")


if __name__ == '__main__':
    app.mainloop()
