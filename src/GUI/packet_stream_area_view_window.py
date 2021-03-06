#! python2
# -*- coding: utf-8 -*-
"""
Created on  Mar  15  2018

@author:    Daniel Ornelas

"""

import Tkinter as tk
class PacketStreamAreaWindow(tk.Frame):
#    pcap = [['1', '11.2', '192.1.1', '192.1.2', 'HTTP', "HELLO"], ['2', '11.4', '192.1.1', '192.1.2', 'TCP', "WORLD"]]
    pcap = []
    def _display_packets(self, PCAP,position):
        col = 0
        row = 0
        for packet in PCAP:
            color="green"#this is the line we will change to change color packet.color
            #tk.Frame(position,bg=color).grid(row=ro, column=0, columnspan=6, sticky='nesw')
            for val in packet:
                tk.Label(position, text=val[:10],bg=color).grid(column=row, row=col+1)
                col += 1
            row += 1
            col = 0

    def init_window(self):
       # self.wm_title('Packet Stream Area View')
       headers = ['TBD', 'TBD', 'TBD', 'TBD']
       self.add_headers(headers)
#       self._display_packets(self.pcap, self)

    def add_headers(self, headers):
        for i, header in enumerate(headers):
            tk.Label(self,text = header,width = 30).grid(column=i,row=0)
        self._display_packets(self.pcap,self)
        
    def hide_window(self):
        self.pack_forget()

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.root = parent
        self.init_window()

        
if __name__ == "__main__":
    root = tk.Tk()
    app = PacketStreamAreaWindow(root)
    app.pack()
    app.mainloop()
