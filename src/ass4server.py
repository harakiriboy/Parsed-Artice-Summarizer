from flask import Flask, request, render_template
from flask.helpers import make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from re import U, template
import time
import jwt
import tableforass4, newspaperkk, getsummary

###########################################################################

app = tableforass4.app
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

###########################################################################

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")

###########################################################################   

@app.route("/mainpage", methods=['POST'])
def main():
    username = request.form.get("ussername")
    password = request.form.get("passwordd")
    userid = 1
    tableforass4.Usser.tablefunc(userid)
    if username == tableforass4.loginn and password == tableforass4.passwordd:
        return render_template("main.html")
    
    return "Could not verify"

############################################################################

@app.route("/formpage")
def formpage():
    return render_template("findbyform.html")

############################################################################

@app.route('/formanswer', methods=['POST'])
def formanswer():
    #-----------------------------------------------------------------------------#
    coinname = request.form.get("coinname")
    newscount = request.form.get("newscount")
    #-----------------------------------------------------------------------------#


    #-----------------------------------------------------------------------------#
    #url of the page we want to scrape
    url = 'https://coinmarketcap.com/currencies/' + coinname + '/news/'
  
    # initiating the webdriver. Parameter includes the path of the webdriver.
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Downloads\chromedriver.exe', options = options) 
    driver.get(url) 
    loadmorebutton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/div/div/main/button')
    for i in range(1):
        loadmorebutton.click() 
        time.sleep(5)  
    #-----------------------------------------------------------------------------#


    #-----------------------------------------------------------------------------#
    # this renders the JS code and stores all
    # of the information in static HTML code.
    html = driver.page_source
    #-----------------------------------------------------------------------------#
  
    
    
    #-----------------------------------------------------------------------------#
    # Now, we could simply apply bs4 to html variable
    soup = BeautifulSoup(html, "html.parser")
    all_divs = soup.find('div', {'class' : 'wav26n-1 gWmJSZ'})
    job_profiles = all_divs.find_all('a')
    count = 0
    listoflinks = []
    for link in job_profiles:
        mylink = link.get('href')
        if(mylink.startswith("https://")):
            listoflinks.append(mylink)
        else:
            mynewlink = "https://coinmarketcap.com/" + mylink
            listoflinks.append(mynewlink)
        count = count + 1
        if(count == newscount) :
            break
    driver.close()
    #------------------------------------------------------------------------------#



    #------------------------------------------------------------------------------#
    listindex1 = 0
    listofarticles = []
    for i in range(len(listoflinks)):
        listofarticles.append(newspaperkk.getarticle(listoflinks[listindex1]))
        listindex1 = listindex1 + 1
    #-------------------------------------------------------------------------------#



    #-------------------------------------------------------------------------------#
    new_info = tableforass4.Articles(1, ''+str(coinname)+'', 'hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello6', 'hello7', 'hello8', 'hello9', 'hello10')
    tableforass4.db.session.add(new_info)
    tableforass4.db.session.commit() 
    #-------------------------------------------------------------------------------#


    #-------------------------------------------------------------------------------#
    countfortable = 1
    listindex2 = 0
    for i in listofarticles:
        listofarticles[listindex2] = getsummary.getsum('''''' + str(listofarticles[listindex2]) + '''''')
        listindex2 = listindex2 + 1
    #-------------------------------------------------------------------------------#


    #-------------------------------------------------------------------------------#
    listindex2 = 0
    for i in listofarticles:
        with tableforass4.engine.connect() as connection:
            result = connection.execute(text('update articles set article' + str(countfortable) + ' = $$' + str(listofarticles[listindex2]) + '$$ where articles.coin_name = '+ "'" + str(coinname) + "'"))
        connection.close()
        if(countfortable == newscount):
            break
        countfortable = countfortable + 1
        listindex2 = listindex2 + 1
    #-------------------------------------------------------------------------------#



    return render_template("formanswer.html", len = len(listofarticles), listofarticles = listofarticles, amount = int(newscount))

####################################################################################################


if __name__ == '__main__':
    app.run(debug=True)