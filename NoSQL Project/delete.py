import tkinter
from tkinter import *

from functools import partial

from tkinter import *
from tkinter import messagebox
import pymongo
from create_fields import fun

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["movies"]


def delete_data(l, showid, type, title, director, cast, country, release_year, date_added, rating, duration,
                description, listed_in):
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

    x = mycol.delete_many(query)

    if x.deleted_count > 0:
        messagebox.showinfo("Success", "{} documents were deleted".format(x.deleted_count))
    else:
        messagebox.showerror("Error", "No documents were found for the query")


def deletef():
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

    displaydata = partial(delete_data, l, showid, type, title, director, cast, country, release_year, date_added,
                          rating,
                          duration, description, listed_in)
    submit = Button(top, text="Submit", command=displaydata).place(x=900, y=590)
