from functools import partial

import pymongo

# from frontend import mycol
import tkinter
from tkinter import *
import json
from tkinter import messagebox
from create_fields import fun

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["movies"]

from bson import ObjectId

global f
f = 0


# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return json.JSONEncoder.default(self, o)


def display_data(l, showid, type, title, director, cast, country, release_year, date_added, rating, duration,
                 description, listed_in, top):
    global f, query, query2
    if f == 0:
        query = {}

        if showid.get() != "":
            query["show_id"] = showid.get()
        if type.get() != "":
            query["type"] = type.get()
        if title.get() != "":
            query["title"] = title.get()
        if director.get() != "":
            query["director"] = director.get()
        if cast.get() != "":
            query["cast"] = cast.get()
        if country.get() != "":
            query["country"] = country.get()
        if release_year.get() != "":
            query["release_year"] = release_year.get()
        if date_added.get() != "":
            query["date_added"] = date_added.get()
        if rating.get() != "":
            query["rating"] = rating.get()
        if duration.get() != "":
            query["duration"] = duration.get()
        if description.get() != "":
            query["description"] = description.get()
        if listed_in.get() != "":
            query["listed_in"] = listed_in.get()

        f += 1
        # top.quit()
        updatef()
    elif f == 1:
        query2 = {}
        f += 1
        if showid.get() != "":
            query2["show_id"] = showid.get()
        if type.get() != "":
            query2["type"] = type.get()
        if title.get() != "":
            query2["title"] = title.get()
        if director.get() != "":
            query2["director"] = director.get()
        if cast.get() != "":
            query2["cast"] = cast.get()
        if country.get() != "":
            query2["country"] = country.get()
        if release_year.get() != "":
            query2["release_year"] = release_year.get()
        if date_added.get() != "":
            query2["date_added"] = date_added.get()
        if rating.get() != "":
            query2["rating"] = rating.get()
        if duration.get() != "":
            query2["duration"] = duration.get()
        if description.get() != "":
            query2["description"] = description.get()
        if listed_in.get() != "":
            query2["listed_in"] = listed_in.get()

        setquery = {"$set": query2}
        x = mycol.update_many(query, setquery)

        if x.modified_count > 0:
            messagebox.showinfo("Success", "{} documents were updated".format(x.modified_count))
        else:
            messagebox.showerror("Error", "No documents were found for the query")


def updatef():
    print(f)
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
                          duration, description, listed_in, top)
    submit = Button(top, text="Submit", command=displaydata).place(x=900, y=590)
