from Tkinter import *

def clamp(lo, hi, x):
    return min(max(x, lo), hi)

class MovingFrame:
    all = []
    def MoveWindowStart(self, event):
        self.move_lastx = event.x_root
        self.move_lasty = event.y_root
        self.focus()
    def MoveWindow(self, event):
        self.root.update_idletasks()

        dx = event.x_root - self.move_lastx
        dy = event.y_root - self.move_lasty
        self.move_lastx = event.x_root
        self.move_lasty = event.y_root
        self.x = clamp(0, 640-200, self.x + dx) # should depend on
        self.y = clamp(0, 480-200, self.y + dy) # actual size here
        self.f.place_configure(x=self.x, y=self.y)

    def __init__(self, root, title, x, y,w,h):
        self.root = root

        self.x = x; self.y = y
        self.f = Frame(self.root, bd=1, relief=RAISED)
        self.f.place(x=x, y=y, width=w, height=h)


        self.l = Label(self.f, bd=1, bg="#08246b", fg="white",text=title)
        self.l.pack(fill=X)

        self.l.bind("PCdrag", '<1>', self.MoveWindowStart)
        self.f.bind("PCdrag", '<1>', self.focus)
        self.l.bind("PCdrag", '<B1-Motion>', self.MoveWindow)
        # self.f.bind('<B1-Motion>', self.MoveWindow)
        self.all.append(self)
        self.focus()

    def focus(self, event=None):
        self.f.tkraise()
        for w in self.all:
            if w is self:
                w.l.configure(bg="#08246b", fg="white")
            else:
                w.l.configure(bg="#d9d9d9", fg="black")
if __name__ == "__main__":
    root = Tk()
    root.title("...")
    root.geometry("%dx%d%+d%+d"%(640, 480, 0, 0)) #useful for main window size
    x = MovingFrame(root, "Window 1", 10, 10)

    root.mainloop()