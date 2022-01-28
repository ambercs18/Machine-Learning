from functools import partial

import pymongo

from create_fields import fun
import tkinter
from tkinter import *
import json
from tkinter import ttk

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["movies"]

import matplotlib

from bson import ObjectId


class Table:

    def __init__(self, root, total_rows=0, total_columns=0, lst=[]):

        # code for creating table
        print(total_columns, total_rows, lst)
        for i in range(total_rows + 1):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def display_data(l, showid, type, title, director, cast, country, release_year, date_added, rating, duration,
                 description, listed_in):
    query = {}

    if showid.get() != "":
        query["show_id"] = {"$regex": showid.get()}
    if type.get() != "":
        query["type"] = {"$regex": type.get()}
    if title.get() != "":
        query["title"] = {"$regex": title.get()}
    if director.get() != "":
        query["director"] = {"$regex": director.get()}
    if cast.get() != "":
        query["cast"] = {"$regex": cast.get()}
    if country.get() != "":
        query["country"] = {"$regex": country.get()}
    if release_year.get() != "":
        query["release_year"] = {"$regex": release_year.get()}
    if date_added.get() != "":
        query["date_added"] = {"$regex": date_added.get()}
    if rating.get() != "":
        query["rating"] = {"$regex": rating.get()}
    if duration.get() != "":
        query["duration"] = {"$regex": duration.get()}
    if description.get() != "":
        query["description"] = {"$regex": description.get()}
    if listed_in.get() != "":
        query["listed_in"] = {"$regex": listed_in.get()}

    mydoc = mycol.find(query)
    # result = ""
    #
    # for x in mydoc:
    #     result += JSONEncoder().encode(x)

    # print(query, mydoc)
    # myquery = {"type": "b"}
    #
    # mydoc = mycol.find(myquery)
    #
    # for x in mydoc:
    #     print(x)

    lst = [l]
    for doc in mydoc:
        f = []
        # print(doc)
        for i in range(len(l)):
            f.append(doc[l[i]])
        lst.append(f)
    newTop = Toplevel()

    newTop.resizable(width=100, height=100)
    treev = ttk.Treeview(newTop, selectmode='browse')

    # Calling pack method w.r.to treeview
    treev.pack(side='top', fill=BOTH, expand=True)

    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(newTop,
                               orient="vertical",
                               command=treev.yview)

    # Calling pack method w.r.to vertical
    # scrollbar
    verscrlbar.pack(side='right', fill='x')

    # Configuring treeview
    treev.configure(xscrollcommand=verscrlbar.set)

    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")

    treev['show'] = 'headings'

    for i in range(1, len(l) + 1):
        treev.column(str(i), width=90, anchor='c')

    for i in range(1, len(l) + 1):
        treev.heading(str(i), text=l[i - 1])

    for i in range(len(lst) - 1):
        treev.insert("", 'end', text="L1",
                     values=lst[i + 1])

    # t = Table(newTop, len(lst)-1, len(l), lst)

    newTop.mainloop()
    # ans = Label(top, text=result, font=("Arial", 20),wraplength=300, justify="center").place(x=600, y=10)


def queryf():
    top = Toplevel()
    l = ["show_id", "type", "title", "director", "cast", "country", "release_year", "date_added", "rating", "duration",
         "description", "listed_in"]

    showid = tkinter.StringVar()
    type = tkinter.StringVar()
    title = tkinter.StringVar()
    director = tkinter.StringVar()
    cast = tkinter.StringVar()
    country = tkinter.StringVar()
    release_year = tkinter.StringVar()
    date_added = tkinter.StringVar()
    rating = tkinter.StringVar()
    duration = tkinter.StringVar()
    description = tkinter.StringVar()
    listed_in = tkinter.StringVar()

    fun(top, showid, type, title, director, cast, country, release_year, date_added, rating,
        duration, description, listed_in)

    displaydata = partial(display_data, l, showid, type, title, director, cast, country, release_year, date_added,
                          rating,
                          duration, description, listed_in)
    submit = Button(top, text="Submit", command=displaydata).place(x=900, y=590)
