#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  15  2018
@author:    Daniel Ornelas
            Gerardo Cervantes
            Oliver Martinez
            Isaac Hoffman
            Christopher Soto
"""

from menu import MenuWindow
from packet_stream_area_view_window import PacketStreamAreaWindow
import Tkinter as tk
from workspace_save_window import Workspace_save_window
from project_navigator_window import ProjectNavigatorWindow
from dissected_stream_window import Dissected_stream_window
from raw_data_window import Raw_data_window
from console_error_view import ConsoleErrorView
from dissector_builder_area import Dissector_builder_area

class MainWindow(tk.Frame):

    def init_window(self):
        self.root.deiconify()
        
        self.menu = MenuWindow(self.root, self)
        self.menu.place(x = 100, y = 20, height = 100, width = 2000)
        #Need to be moving frames
        self.dba = Dissector_builder_area(self.root)
        self.dba.place(x = 500, y = 60, height = 550, width = 2000)
        self.psa = PacketStreamAreaWindow(self.root)
        self.psa.place(x = 100, y = 800, height = 550, width = 1050)
        
        self.proj_nav = ProjectNavigatorWindow(self.root)
        ProjectNavigatorWindow.current = self.proj_nav
        self.proj_nav.mv.f.place(x = 0, y = 60, height = 500, width = 200)
        self.stream_window = Dissected_stream_window(self.root)
        self.stream_window.mv.f.place(x = 0, y = 600, height = 200, width = 350)
        self.raw_data_w = Raw_data_window(self.root)
        self.raw_data_w.mv.f.place(x = 350, y = 600, height = 200, width = 350)
        self.console_error_window = ConsoleErrorView(self.root)
        self.console_error_window.mv.f.place(x = 700, y = 600, height = 200, width = 350)
        
        



    def init_launcher(self):
        self.launcher = tk.Toplevel(self.root)
        Workspace_save_window(self, self.launcher)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.root.title('Protocol-Dissector Generator System')
        self.init_launcher()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    app = MainWindow(root)
    root.mainloop()
