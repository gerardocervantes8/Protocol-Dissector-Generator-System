# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 22:05:42 2018

@author: revil0mg
"""

#TODO: Add Reference List Name field on top of window. (see SRS for details)
#TODO: Make + button work properly

import Tkinter as tk
import ttk

class Reference_List_Window(tk.Frame):
    def _new_entry(self, frame, c, r):
        tk.Entry(frame, text = " ").grid(column = c, row = r+1)
        tk.Entry(frame, text = " ").grid(column = c+1, row = r+1)

    def init_window(self):

        #root.wm_title('Packet Information')

        frame = tk.Frame(self)
        frame.pack()
        tk.Label(frame,text='Value').grid(column=0,row=0)
        tk.Label(frame,text='Description').grid(column=1, row=0)
        entry1 = ttk.Entry(frame)
        entry1.grid(column = 0 , row = 1)
        entry2 = ttk.Entry(frame)
        entry2.grid(column = 1 , row = 1)
        tk.Button(frame, text="+",command = lambda: self._new_entry(frame,0,1)).grid(column = 3, row = 2)



    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.root = parent
        self.root.title("Refernce List [Reference List Name]")
        self.init_window()

if __name__ == "__main__":
    root = tk.Tk()
    app = Reference_List_Window(root)
    app.pack()
    app.mainloop()