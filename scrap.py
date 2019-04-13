from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox
from threading import Thread,Lock
import threading
import csv
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import sys
tu=0
yu=0
def chooseDir():
    a.sourceFolder =  filedialog.askdirectory(parent=a, initialdir= "/", title='Please select a directory')
    b.set(a.sourceFolder)
def threadstart():
    global t1
    t1.start()
def threadstop():
    global t2
    t2.start()
def stoplogger():
    global yu
    yu=1
    a.destroy()
def startlogger():
    global tu
    global yu
    if myfruit.get() == "Politico":
        xyz=b.get()+"/politico.csv"
        with open(xyz, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Heading', 'Description'])
        for z in range(1,199):
            if tu==1:
                break
            z1=str(z)
            wiki = "https://www.politico.com/news/terrorism/"+z1
            page=urllib.request.urlopen(wiki)
            soup = BeautifulSoup(page,"lxml")
            al=soup.find("ul",class_="story-frag-list layout-grid grid-3")
            xy=al.find_all("li")
            #print(xy)
            for i in xy:
                if i.find("p",class_="timestamp"):
                    try:
                        a=i.find('a', href=True)
                        wikii=a['href']
                        pagee=urllib.request.urlopen(wikii)
                        soupp = BeautifulSoup(pagee,"lxml")
                        alt2=soupp.find("div",class_="summary")
                        alt21=alt2.find("h1", class_=True)
                        alt211=alt21.find("span" , itemprop="headline")
                        alt2111=alt211.text
                        alt=soupp.find("div",class_="content-group story-core")
                        alt1=alt.select(".story-text > p")
                        t=""
                        if yu==0:  
                            for k in alt1:
                                abb=k.text
                                t=t+abb
                            with open(xyz, 'a') as csfile:
                                writer = csv.writer(csfile)
                                writer.writerow([alt2111, t])
                        else:
                            tu=1
                            break
                    except:
                        pass
                else:
                    pass
            
    elif myfruit.get() == "EuroNews":
        xyz=b.get()+"/euronews.csv"
        with open(xyz, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Heading', 'Description'])
        for z in range(1,65):
            if tu==1:
                break
            z1=str(z)
            wiki = "https://www.euronews.com/tag/terrorism?p="+z1
            page=urllib.request.urlopen(wiki)
            soup = BeautifulSoup(page,"lxml")
            al=soup.find_all("section", class_="media-section")
            for i in al:
                alk=i.find("a", href=True)
                wikki=alk['href']
                wi="https://www.euronews.com"+wikki
                pa=urllib.request.urlopen(wi)
                sou = BeautifulSoup(pa,"lxml")
                try:
                    alt=sou.find("h1", class_="c-article-title")
                    alt1=alt.text
                    alt2=sou.find("div", class_="column small-12 medium-10 xlarge-11 u-zindex--bottom js-responsive-iframes-container")
                    alt21=alt2.find_all("p")
                    t=""
                    if yu==0: 
                        for k in alt21:
                            abb=k.text
                            t=t+abb
                        with open(xyz, 'a') as csfile:
                            writer = csv.writer(csfile)
                            writer.writerow([alt1, t])
                    else:
                        tu=1
                        break
                except:
                    pass
    
a=Tk()
t1=Thread(target=startlogger)
t2=Thread(target=stoplogger)
a.sourceFolder = ''
b = StringVar()
myfruit=StringVar()
a.title("scrapper")
a.geometry("500x400+100+100")
ll=Label(text="COLLEGE OF MILITARY ENGINEERING",fg="black",font= "Verdana 14 underline").place(x=80,y=20)
l1=Label(text="Data Base on Global Terrorism ",fg="black",font=6).place(x=140,y=100)
ll1=Label(text=" Select Source",fg="black",font=6).place(x=100,y=200)
combo =Combobox(a,state="readonly",textvariable=myfruit,values=["Politico","EuroNews"]).place(x=240,y=200)
ll1=Label(text=" Select Destination",fg="black",font=6).place(x=100,y=240)
text=Entry(textvariable=b).place(x=240,y=240)
bb=Button(text="...",command=chooseDir).place(x=370,y=235)
bb1=Button(text="RUN",command=threadstart).place(x=150,y=335)
bb2=Button(text="CLOSE",command=threadstop).place(x=250,y=335)
a.mainloop()