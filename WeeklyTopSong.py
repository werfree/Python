from bs4 import BeautifulSoup
import lxml
from tkinter import *
import urllib.request
import tkinter
w=Tk()
w.title("TOP 50 @SAyantan")
w.geometry(
    "360x250")
w.configure(background='black')
w.resizable(0,0)
w.wm_attributes("-topmost",1)

'''def eng():
    print("ENGLISH \n \n")
    res=urllib.request.urlopen("https://www.saavn.com/s/featured/english/Weekly+Top+Songs").read()
    res = res.decode("utf-8")
    soup=BeautifulSoup(res,"lxml")
    #soup=soup.body5
    data=soup.find('ol',{"class":"content-list"})
    allsong=data.find_all('div',{'class':"details content-list"})
    count=0
    for s in (allsong):
        count+=1
        song=s.find('p',{"class":"song-name ellip"})
        print(count,song.text)
    print("\n")

def bengali():
    print("BENGALI \n \n")
    res=urllib.request.urlopen("https://www.saavn.com/s/featured/bengali/Weekly+Top+Songs").read()
    res = res.decode("utf-8")
    soup=BeautifulSoup(res,"lxml")
    #soup=soup.body5
    data=soup.find('ol',{"class":"content-list"})
    allsong=data.find_all('div',{'class':"details content-list"})
    count=0
    for s in (allsong):
        count+=1
        song=s.find('p',{"class":"song-name ellip"})
        print(count,song.text)
    print("\n ")

def hindi():
    global uh
    print("HINDI \n")
    res = urllib.request.urlopen(uh).read()
    res = res.decode("utf-8")
    soup = BeautifulSoup(res, "lxml")
    data = soup.find("ol", {"class": "content-list"})
    song = data.find_all("div", {'class': "details content-list"})
    c = 0
    for i in song:
        c += 1
        s = i.find('p', {"class": "song-name ellip"})
        print(c, s.text)
    print("\n")
'''




def top(u,e):
    
    print(e)
    print("\n")
    res=urllib.request.urlopen(u).read()
    res = res.decode("utf-8")
    soup=BeautifulSoup(res,"lxml")
    #soup=soup.body5
    #data=soup.find('ol',{"class":"content-list"})
    allsong=soup.find_all('div',{'class':"track_npqitemdetail"})
    count=0
    for s in (allsong):
        count+=1
        #song=s.find('p',{"class":"song-name ellip"})
        print(count,end=" ")
        k=s.text
        for i in k:
            if i=="-":
                print("")
                break
            else:
                print(i,end="")
            
    print("\n ")


    
def song():
    l1=Label(w,text="HINDI",font=("Helvetica 20 bold"),fg="Yellow",bg="Black")
    h1=Button(w,text="TOP 50",command=lambda:top("https://gaana.com/playlist/gaana-dj-bollywood-top-50-1","BOLLYWOOD TOP 50"))
    h3=Button(w,text="ROMANTIC",command=lambda:top("https://gaana.com/playlist/gaana-dj-bollywood-romance-songs","ROMANTIC  (H)"))
    h2=Button(w,text="PARTY",command=lambda:top("https://gaana.com/playlist/gaana-dj-bollywood-party-songs","PARTY  (H)"))

    l1.grid(row=1,column=1,columnspan=3)
    h1.grid(row=2,column=1)
    h2.grid(row=2,column=2)
    h3.grid(row=2,column=3)

    l2=Label(w,text="ENGLISH",font=("Helvetica 20 bold"),fg="Yellow",bg="Black")
    e1=Button(w,text="Top 50",command=lambda:top("https://gaana.com/playlist/gaana-dj-gaana-international-top-50","INTERNATIONAL TOP 50"))
    e2=Button(w,text="ROMANTIC",command=lambda:top("https://gaana.com/playlist/gaana-dj-latest-love-2017-international","ROMANTIC  (E)"))
    e3=Button(w,text="PARTY",command=lambda:top("https://gaana.com/playlist/gaana-dj-latest-dance-2018-international","PARTY  (E)"))

    l2.grid(row=3,column=1,columnspan=3)
    e1.grid(row=4,column=1)
    e2.grid(row=4,column=2)
    e3.grid(row=4,column=3)

    l3=Label(w,text="OTHERS",font=("Helvetica 20 bold"),fg="Yellow",bg="Black")
    o1=Button(w,text="BENGALI",command=lambda:top("https://gaana.com/playlist/gaana-dj-bengali-top-50","BENGALI TOP 50"))
    o2=Button(w,text="EDM",command=lambda:top("https://gaana.com/playlist/gaana-dj-latest-edm-2016-","LATEST EDM"))
    o3=Button(w,text="OUR CHOICE",command=lambda:top("https://gaana.com/playlist/gaana-dj-latest-love-2018-bollywood","MY FAV"))

    l3.grid(row=5,column=1,columnspan=3)
    o1.grid(row=6,column=1)
    o2.grid(row=6,column=2)
    o3.grid(row=6,column=3)

    

    

    
    
    

if __name__=="__main__":
    song()
