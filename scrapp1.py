#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import selenium
from selenium import webdriver
import time
import pandas as df
import sys
xcomments=[]
xusername=[]
xtime =[]
like=[]
share=[]
pages = [];
compilecomments=[]
compileusername=[]
compiletime =[]
compilelike=[]
compileshare=[]

def clearLists():
    xusername.clear()
    xcomments.clear()
    xtime.clear()
    like.clear()
    share.clear()

def checkpage(strg, browser):
    browser.get(strg)

    #Scroll to the end of the page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)#sleep_between_interactions
    
    comments = browser.find_elements_by_class_name('narrow')
    username = browser.find_elements_by_class_name('user')
    comtime = browser.find_elements_by_xpath('//span[@class="s"]')
    activity = browser.find_elements_by_tag_name('td')



    bae = False;
    count=0;

    for t in range(len(activity)):
        try:
            a = activity[t].find_element_by_tag_name("div").text
            bae = True
            #print("No "+str(count)+".div. "+str(a))
        except:
            bae = False
            continue

        try:
            xcomments.append(comments[count].text)
            #print("No "+str(count)+".user. "+username[count].text)
        except:
            pass

        try:
            xusername.append(username[count].text)
            #print("No "+str(count)+".user. "+username[count].text)
        except:
            pass

        try:
            xtime.append(comtime[count].text)
            #print("No "+str(count)+".user. "+comments[count].text)
        except:
            pass

        try:
            q = activity[t].find_element_by_tag_name("p").text
            #print("No "+str(count)+".reaction. "+str(q))
            #3 Likes 1 Share
            try:
                if (q.find("Likes")>0):
                    z = q.split(" ")
                    like.append(z[0])
                    #print("like="+str(z[0]))
                else:
                    like.append(0)
            except:
                pass
            
            try:
                if (q.find("Share")>0):
                    w = q.split(" ")
                    share.append(w[2])
                    #print("shares="+str(w[2]))
                else:
                    share.append(0)
            except:
                pass

        except:
            like.append(0)
            share.append(0)
            #print("No "+str(count)+".reaction. "+"No reaction")


        if(bae):
            count=count+1
  
            
def linkChecker(URL, browser):
    for g in range(len(like)):
        print(str(g)+".  Time:>"+str(xtime[g])+".  Username:>"+str(xusername[g])+".  Comments:>"
              +str(xcomments[g])+".  Shares:>"+str(share[g])
              +" --- Likes:>"+str(like[g]))
    
    dictionary = {}
    linkpages = []
    #URL = "https://www.nairaland.com/6577081/umahi-sacks-over-1000-board"
    linkpages.append(URL)

    browser.get(URL)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)#sleep_between_interactions
    pam = browser.find_elements_by_tag_name('p')
    for y in range(len(pam)):
        zam = pam[y].find_elements_by_tag_name('a')
        for z in range (len(zam)):
            try:
                link = str(zam[z].get_attribute('href'))
                if(link.find(URL)>=0):
                    if(link.find("#down")<0 and link.find("#up")<0):
                        linkpages.append(link)
            except:
                pass

    linkpages = list(dictionary.fromkeys(linkpages))
    print(len(linkpages))

    for u in range(len(linkpages)):
        print("linkpages:"+linkpages[u])

    for h in range(len(linkpages)):
        print("Going trip: "+str(h))
        try:
            checkpage(linkpages[h], browser)
        except:
            pass;


    totalcomments=len(xcomments)
    totalusername = len(xusername)
    totaltime = len(xtime)
    totallike = len(like)
    totalshare = len(share)
    
    print(str(totalcomments)+","+str(totalusername)+","+str(totaltime)
          +","+str(totallike)+","+str(totalshare))
    
    
    try:
        
        dict = {'Username': xusername, 'Comments': xcomments, 'Time': xtime, 'Share': share, 'Like': like}  
        vals = df.DataFrame(dict) 
        #saving the dataframe 
        filename = URL.replace("https://www.nairaland.com", "")
        filename = filename.replace("/", "")
        print(filename)
        vals.to_csv(filename+".csv")
        
        rollCall = 0;
        pages.append(len(xcomments));
        for r in range(len(pages)):
            rollCall+=pages[r]
        
        print("rollCall:"+str(rollCall))
        
        for xz in range(len(xcomments)):
            compilecomments.append(xcomments[xz])
        
        for xy in range(len(xusername)):
            compileusername.append(xusername[xy])
            
        for xx in range(len(xtime)):
            compiletime.append(xtime[xx])
        
        for xu in range(len(like)):
            compilelike.append(like[xu])
            
        for xv in range(len(share)):
            compileshare.append(share[xv])
            
        
        if(rollCall >= 500):
            dictiony={}
            print("final saving:"+str(pages))
            dictiony = {'Username': compileusername, 'Comments': compilecomments, 
                    'Time': compiletime, 'Share': compileshare, 'Like': compilelike}  
            valws = df.DataFrame(dictiony) 
            #saving the dataframe 
           
            valws.to_csv("nairalandTop500.csv")
            
            clearLists()
            headlines.clear()
            browser.close()
        
        clearLists()
    except:
        clearLists()
        pass

    
def main(site, browser):
    
    headlines = []

    browser.get(site)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)#sleep_between_interactions
    pac = browser.find_elements_by_class_name('featured')
    #pam = pac.find_elements_by_tag_name('td')
    for y in range(len(pac)):
        sam = pac[y].find_elements_by_tag_name('a')
        for s in range(len(sam)):
            headlines.append(str(sam[s].get_attribute('href')))
            print(str(sam[s].get_attribute('href')))


    for i in range(len(headlines)):
        if(len(headlines)>0):    #because I am using this to end at 500 data
            print("going:>"+str(i))
            linkChecker(headlines[i], browser)
        else:
            quit()


    browser.close()
    


# In[ ]:





# In[ ]:




