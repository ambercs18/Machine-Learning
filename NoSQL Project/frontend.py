import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter.font import BOLD
from functools import partial
import pymongo
from query import queryf
from update import updatef
from delete import deletef
from create_fields import fun

import matplotlib.pyplot as plt

filename = "disney_plus_titles.csv"

# initializing the titles and rows list
# fields = []
rows = []

# reading csv file
# with open(filename, 'r', encoding='utf-8') as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)
#
#     fields = next(csvreader)
#
#     # extracting each data row one by one
#     for row in csvreader:
#         rows.append(row)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["movies"]

# data = []
# for row in rows:
#     d = {}
#     for i in range(len(row)):
#         d[fields[i]] = row[i]
#     data.append(d)
#
# x = mycol.insert_many(data)

myquery = {"release_year":{"$regex": "1"}}

mydoc = mycol.find(myquery)


grp={}
for x in mydoc:
    k=x["release_year"]
    if k in grp:
        grp[k]+=1
    else:
        grp[k]=1

x=sorted(list(grp.keys()))
y=sorted(list(grp.values()))

plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Movies per year!')

plt.tick_params(axis='x', which='major', labelsize=3)

# function to show the plot
plt.show()

print(x)
print(y)

root = Tk()
root.title("Movie Database Interface")


# functions





def fill_data(l, showid, type, title, director, cast, country, release_year, date_added, rating, duration, description,
              listed_in):
    d = {}
    d["show_id"] = showid.get()
    d["type"] = type.get()
    d["title"] = title.get()
    d["director"] = director.get()
    d["cast"] = cast.get()
    d["country"] = country.get()
    d["release_year"] = release_year.get()
    d["date_added"] = date_added.get()
    d["rating"] = rating.get()
    d["duration"] = duration.get()
    d["description"] = description.get()
    d["listed_in"] = listed_in.get()

    f = 0
    for k in d:
        if d[k] == "":
            messagebox.showerror("Error", "One or more fields were empty")
            f = 1
        if f == 1:
            break
    if f == 0:
        mycol.insert_one(d)




def insert():
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

    fun(top,showid, type, title, director, cast, country, release_year, date_added, rating,
        duration, description, listed_in)



    filldata = partial(fill_data, l, showid, type, title, director, cast, country, release_year, date_added, rating,
                       duration, description, listed_in)
    submit = Button(top, text="Submit", command=filldata).place(x=900, y=590)


# define elements
myLabel = Label(root, text="Operations", font=("Arial", 25, BOLD))
insertBtn = Button(root, text="Insert", font=("Arial", 14), command=insert)
updateBtn = Button(root, text="Update", font=("Arial", 14), command=updatef)
deleteBtn = Button(root, text="Delete", font=("Arial", 14), command=deletef)
displayBtn = Button(root, text="Display", font=("Arial", 14), command=queryf)

# grid
myLabel.place(x=700, y=50)
insertBtn.place(x=600, y=150)
updateBtn.place(x=750, y=150)
deleteBtn.place(x=900, y=150)
displayBtn.place(x=1050, y=150)

root.mainloop()
