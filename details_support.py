#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 12, 2020 12:55:36 PM IST  platform: Windows NT

import sys
import psycopg2
from psycopg2 import sql
from tkinter import messagebox

con = psycopg2.connect(database ="payment", user = "postgres", password = "root", host = "127.0.0.1", port = "5432" )
cur = con.cursor()

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def menu(p1):
    top_level.destroy()
    import menu
    menu.vp_start_gui()

def advance(p1):

    Name = w.name.get()
    Name = Name.lower()
    w.text.delete(0,100)
    w.text.insert(100,f"{'Name':^33}|{'Site':^30}|{'Date':^37}|{'Amount':^33}|{'Reason':^30}")
    w.text.insert(100, '_'*95)
    cur.execute(sql.SQL("SELECT * FROM advance.{}").format(sql.Identifier(Name)))
    rows = cur.fetchall()
    for row in rows:
        w.text.insert(100,"{0:^30}|{1:^30}|          {2}           |{3:^35}|{4:^20}".format(row[0].title(), row[1].capitalize(), row[2], row[3], row[4].capitalize()))
        
def bio(p1):

    Name = w.name.get()
    Name = Name.lower()
    w.text.delete(0,100)
    w.text.insert(100,f"{'Name':^33}|{'Role':^20}|{'Account No.':^33}|{'Account Name.':^33}|{'Bank Name':^20}|{'Branch Name':^20}|{'IFSC':^20}")
    w.text.insert(100, '_'*120)
    cur.execute("SELECT * FROM biodata WHERE name = %s",[Name])
    rows = cur.fetchall()
    for row in rows:
        w.text.insert(100,"{0:^30}|{1:^20}|{2:^31}|{3:^37}|{4:^21}|{5:^25}|{6:^20}".format(row[0].title(), row[1].capitalize(), row[2].upper(), row[3].title(), row[4].upper(), row[5].capitalize(), row[6].upper()))
        
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    con.close()
    top_level = None

if __name__ == '__main__':
    import details
    details.vp_start_gui()




