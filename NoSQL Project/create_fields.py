from tkinter import *


def fun(top, showid, type, title, director, cast, country, release_year, date_added, rating,
        duration, description, listed_in):
    # labels
    inslbl = Label(top, text="Insert data", font=("Arial", 20)).place(x=100, y=10)
    showid_lbl = Label(top, text="Insert Show ID", font=("Arial", 10)).place(x=30, y=60)
    type_lbl = Label(top, text="Insert Type", font=("Arial", 10)).place(x=30, y=110)
    title_lbl = Label(top, text="Insert Title", font=("Arial", 10)).place(x=30, y=160)
    director_lbl = Label(top, text="Insert Director", font=("Arial", 10)).place(x=30, y=210)
    cast_lbl = Label(top, text="Insert Cast", font=("Arial", 10)).place(x=30, y=260)
    country_lbl = Label(top, text="Insert Country", font=("Arial", 10)).place(x=30, y=310)
    release_year_lbl = Label(top, text="Insert Release Year", font=("Arial", 10)).place(x=30, y=360)
    date_added_lbl = Label(top, text="Insert Date Added", font=("Arial", 10)).place(x=30, y=410)
    rating_lbl = Label(top, text="Insert Rating", font=("Arial", 10)).place(x=30, y=460)
    duration_lbl = Label(top, text="Insert Duration", font=("Arial", 10)).place(x=30, y=510)
    description_lbl = Label(top, text="Insert Description", font=("Arial", 10)).place(x=30, y=560)
    listed_in_lbl = Label(top, text="Insert Category", font=("Arial", 10)).place(x=30, y=610)

    # textfields
    showidt = Entry(top, width=80, textvariable=showid).place(x=200, y=60)
    typet = Entry(top, width=80, textvariable=type).place(x=200, y=110)
    titlet = Entry(top, width=80, textvariable=title).place(x=200, y=160)
    directort = Entry(top, width=80, textvariable=director).place(x=200, y=210)
    castt = Entry(top, width=80, textvariable=cast).place(x=200, y=260)
    countryt = Entry(top, width=80, textvariable=country).place(x=200, y=310)
    release_yeart = Entry(top, width=80, textvariable=release_year).place(x=200, y=360)
    date_addedt = Entry(top, width=80, textvariable=date_added).place(x=200, y=410)
    ratingt = Entry(top, width=80, textvariable=rating).place(x=200, y=460)
    durationt = Entry(top, width=80, textvariable=duration).place(x=200, y=510)
    descriptiont = Entry(top, width=80, textvariable=description).place(x=200, y=560)
    listed_int = Entry(top, width=80, textvariable=listed_in).place(x=200, y=610)
