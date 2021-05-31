#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import scrapp1 as scrapp
from tkinter import *
from tkinter import ttk
import pandas as dd
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox as mb
from tkinter import filedialog as fd 
import selenium
from selenium import webdriver

name=""
website=""

def web():
    mb.showinfo(title="Important Driver", message="Select FireFox geckodriver")
    name= fd.askopenfilename() 
    drt = "Using: "+name
    labelDriver.config(text = drt)
    
    website= my_entry.get()
    print(website)
    if(website == "website"):
        mb.showerror(title="Wrong!", message="Enter website: https://www.nairaland.com")
    elif(website.find("https")>=0):
        #PATH = "/Users/adetunjiayoade/WebScrapping/geckodriver"
        print("name:"+name)
        browser = webdriver.Firefox(executable_path = name)
        try:
            scrapp.main(website, browser)
        except:
            print("scrapping done")
    else:
        mb.showinfo(title="Entry", message="Enter website: https://www.nairaland.com")
        
def do_layout():
    f1.grid(column=0, row=0)
    f2.grid(column=1, row=0)
    f3.grid(column=0, row=1)
    f4.grid(column=1, row=1)
    
    g1.grid(column=0, row=0)
    g2.grid(column=1, row=0)
    g3.grid(column=0, row=1)
    g4.grid(column=1, row=1)
    
    a2.pack(side = TOP)
    a3.pack(side = BOTTOM )
    a1.pack(side = LEFT )
    
    

root = tk.Tk()
root.title("Python Assessment - nairaland.com scrapping")
root.geometry("900x550")

tp = ttk.Notebook(root)
path = "nothing"
url =  "https://www.nairaland.com"


anotherframe = ttk.Frame(tp)
mainframe=ttk.Frame(tp)
plotframe = ttk.Frame(tp)

a1 = tk.Frame(anotherframe, bg='blue', width=1000,height=300)
a2 = tk.Frame(anotherframe, bg='yellow', width=500, height=300)
a3= tk.Frame(anotherframe, bg='yellow', width=500, height=300)

f1 = tk.Frame(mainframe, bg='blue', width=500,height=400)
f2 = tk.Frame(mainframe, bg='yellow', width=500, height=400)
f3 = tk.Frame(mainframe, bg='red', width=500, height=400)
f4 = tk.Frame(mainframe, bg='orange', width=500, height=400)

g1 = tk.Frame(plotframe, bg='blue', width=500,height=300)
g2 = tk.Frame(plotframe, bg='yellow', width=500, height=300)
g3 = tk.Frame(plotframe, bg='red', width=500, height=300)
g4 = tk.Frame(plotframe, bg='orange', width=500, height=300)

tp.add(anotherframe, text ='Data')
tp.add(mainframe, text ='Analysis')
tp.add(plotframe, text ='Plots')
tp.pack(expand = 1, fill ="both")


labelframe = LabelFrame(f1, text="Longest Comments")
labelframe.pack(fill="both", expand="yes")

labelframe2 = LabelFrame(f2, text="Highest Likes")
labelframe2.pack(fill="both", expand="yes")

labelframe3 = LabelFrame(f3, text="Highest Commentator")
labelframe3.pack(fill="both", expand="yes")

labelframe4 = LabelFrame(f4, text="Highest Shares")
labelframe4.pack(fill="both", expand="yes")


plotframe = LabelFrame(g1, text="Got the most likes")
plotframe.pack(fill="both", expand="yes")

plotframe2 = LabelFrame(g2, text="Great at Sharing")
plotframe2.pack(fill="both", expand="yes")

plotframe3 = LabelFrame(g3, text="Most Inclined to comment")
plotframe3.pack(fill="both", expand="yes")

plotframe4 = LabelFrame(g4, text="Wrote lots of words")
plotframe4.pack(fill="both", expand="yes")


processframe = LabelFrame(a1, text="NOTICE", width=700, height=300)
processframe.pack(fill="both", expand="yes", )

processframe2 = LabelFrame(a2, text="SELECT OPERATION FILES", width=700, height=300)
processframe2.pack(fill="both", expand="yes")

processframe3 = LabelFrame(a3, text="CLEANED DATA", width=700, height=300)
processframe3.pack(fill="both", expand="yes")

df = dd.read_csv("/Users/adetunjiayoade/tKinterWork/nairalandTop500.csv")
#All Data display
df.drop(df.columns[[0]], axis = 1, inplace = True)

comments = df.Comments
commentLent = []

for a in range(len(comments)):
    kk = str(comments[a])
    words = kk.split()
    wordCount = len(words)
    commentLent.append(wordCount)

df['Comment Length'] = commentLent
df.info()
cols = list(df.columns)
print(cols)
tree = ttk.Treeview(processframe3)
tree.pack()
tree["columns"] = cols
for i in cols:
    tree.column(i, anchor="w")
    tree.heading(i, text=i, anchor='w')

for index, row in df.iterrows():
    tree.insert("",0,text=index,values=list(row))

    
#button = Button(processframe2, text = "Browse", command = set,
                #fg = "light blue", font = "Verdana 14",
               # bd = 2, bg = "light blue", relief = "groove")
#button.grid(column=0, row=0)

button2 = Button(processframe2, text = "Scrap", command = web,
                fg = "light blue", font = "Verdana 14",
                bd = 2, bg = "light blue", relief = "groove")
button2.grid(column=2, row=1)

labelDriver = Label(processframe2, text = "You need to download Firefox geckodriver and unzip it" )
labelDriver.grid(column=0, row=1)

labelWeb = Label(processframe2, text = "Enter website to scrap:" )
labelWeb.grid(column=1, row=0)

my_entry = Entry(processframe2, width = 20)
my_entry.insert(0,'website')
my_entry.grid(column=2, row=0)

# Create text widget and specify size.
T = Text(processframe, height = 300, width = 700, bg = "light gray", font=("Calibri", 15))
T.tag_configure('tag-center', justify='center')

Fact ="""This application is a GUI represensation of the assessment:
IRTW001
Python Training: Level 2 | Mini data analysis project"""
T.pack()
T.insert('end', Fact, 'tag-center')
T.wrap=WORD

T.insert('end', "", 'tag-center')

Fact2 ="""

The application when launched, would first scrap Nairaland.com for latest posts.
It collects approximately 500 rows of data. The data includes comments, likes and shares.
Using Selenium, the data cleaned, errors and nulls removed. After which it saves the data in
a .csv file.
The next step is to process the .csv file using Panda and displaying the dataFrame with Tkinter
GUI. The GUI illustrates the descriptive statistics by comparing the outcomes of the data. 
With matplotlib Figure, it then displays the resulting set of visualisations - bar chart, 
scatter plot, pie chart on a canvas. 
Page 1: this page contains all data scrapped.
Page 2: contains the statistics.
Page 3: contains the plot. 
Please click above buttons to view it."""
T.insert('end', Fact2, 'tag-center')
# Insert The Fact.
#T.insert(tk.END, Fact)



    
#Longest Comments
# df.sort_values(by="Like", ascending=True, kind="mergesort")
dfj = df.sort_values(by=["Comment Length"], ascending=True, kind="mergesort")[["Username", "Comment Length"]]
coljs= list(dfj.columns)

tree = ttk.Treeview(labelframe)
tree.pack()
tree["columns"] = coljs

for j in coljs:
    tree.column(j, anchor="w")
    tree.heading(j, text=j, anchor='w')

for index, row in dfj.iterrows():
    tree.insert("",0,text=index,values=list(row))


#Highest Likes
# df.sort_values(by="Like", ascending=True, kind="mergesort")
dfq = df.sort_values(by=["Like"], ascending=True, kind="mergesort")[["Username", "Like"]]
coles= list(dfq.columns)

tree = ttk.Treeview(labelframe2)
tree.pack()
tree["columns"] = coles

for e in coles:
    tree.column(e, anchor="w")
    tree.heading(e, text=e, anchor='w')

for index, row in dfq.iterrows():
    tree.insert("",0,text=index,values=list(row))

    
#Highest Shares
# df.sort_values(by="Like", ascending=True, kind="mergesort")
dfz = df.sort_values(by=["Share"], ascending=True, kind="mergesort")[["Username", "Share"]]
colzs= list(dfz.columns)

tree = ttk.Treeview(labelframe4)
tree.pack()
tree["columns"] = colzs

for z in colzs:
    tree.column(z, anchor="w")
    tree.heading(z, text=z, anchor='w')

for index, row in dfz.iterrows():
    tree.insert("",0,text=index,values=list(row))

    
#Highest commentator
dfx = df.groupby(['Username'])['Comments'].count().reset_index(
  name='Count').sort_values(['Count'], ascending=True)
colxs = list(dfx.columns)

tree = ttk.Treeview(labelframe3)
tree.pack()
tree["columns"] = colxs

for c in colxs:
    tree.column(c, anchor="w")
    tree.heading(c, text=c, anchor='w')

for index, row in dfx.iterrows():
    tree.insert("",0,text=index,values=list(row))
    
#print(df.apply(lambda row: row.astype(str).str.contains('PeaceforNigeria').any(), axis=1))

contain_values = df[df['Username'].str.contains('PeaceforNigeria')]
print (contain_values)



dfq= dfq.sort_values('Like', ascending = False)
dfq= dfq[0:10]
users = dfq['Username']
liker = dfq['Like']
fig = Figure(figsize = (6,3), dpi = 100)
a = fig.add_subplot()
a.scatter(users, liker, color=['orange', 'red', 'green', 'blue', 'cyan', 'orange', 'brown', 'gray', 'violet', 'green'], label = "Like")
a.tick_params(axis='both', which='major', labelsize=5)
a.tick_params(axis='both', which='minor', labelsize=6)
a.set_xlabel("Users")
a.set_ylabel("Likes")
a.set_title("10 Users with most likes")
a.legend()
canv = FigureCanvasTkAgg(fig, master = plotframe)
canv.draw()
get_widz = canv.get_tk_widget()
get_widz.pack()


dfz= dfz.sort_values('Share', ascending = False)
dfz= dfz[0:11]
users = dfz['Username']
sharer = dfz['Share']
fig = Figure(figsize = (6,3), dpi = 100)
a = fig.add_subplot()
a.bar(users, sharer, color=['orange', 'red', 'green', 'blue', 'cyan', 'orange', 'brown', 'gray', 'violet', 'green'], label = "Share")
a.tick_params(axis='both', which='major', labelsize=5)
a.tick_params(axis='both', which='minor', labelsize=6)
a.set_xlabel("Users")
a.set_ylabel("Shares")
a.set_title("10 Users with most Shares")
a.legend()
canv = FigureCanvasTkAgg(fig, master = plotframe2)
canv.draw()
get_widz = canv.get_tk_widget()
get_widz.pack()


dfx= dfx.sort_values('Count', ascending = False)
dfx= dfx[0:10]
users = dfx['Username']
comm = dfx['Count']
fig = Figure(figsize = (6,3), dpi = 100)
a = fig.add_subplot()

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
a.pie(comm, explode, users)
a.tick_params(axis='both', which='major', labelsize=5)
a.tick_params(axis='both', which='minor', labelsize=6)
a.set_title("10 most active commentators")
canv = FigureCanvasTkAgg(fig, master = plotframe3)
canv.draw()
get_widz = canv.get_tk_widget()
get_widz.pack()


dfj= dfj.sort_values('Comment Length', ascending = False)
dfj= dfj[0:10]
users = dfj['Username']
commlen = dfj['Comment Length']
fig = Figure(figsize = (6,3), dpi = 100)
a = fig.add_subplot()
a.barh(users, commlen, color=['orange', 'red', 'green', 'blue', 'cyan', 'orange', 'brown', 'gray', 'violet', 'magenta'],label = "Most Words")
a.tick_params(axis='both', which='major', labelsize=7)
a.tick_params(axis='both', which='minor', labelsize=6)
a.set_xlabel("Words")
a.set_ylabel("Users")
a.set_title("10 Users with most words")
a.legend()
canv = FigureCanvasTkAgg(fig, master = plotframe4)
canv.draw()
get_widz = canv.get_tk_widget()
get_widz.pack()


do_layout()

root.mainloop()


# In[ ]:





# In[ ]:




