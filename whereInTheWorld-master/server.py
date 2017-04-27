import os
import psycopg2
import psycopg2.extras
from flask import Flask, render_template, request
app = Flask(__name__)

def connect():
    connection= 'dbname=world user=rudiment3 password=c host=localhost'

    try:
        return psycopg2.connect(connection)
    except:
        print("Cant connect")

@app.route('/', methods=['GET','POST'])
def mainIndex():
    conn=connect()
    cur=conn.cursor()
    results=[]
    results2=[]
    results3=[]
    results4=[]
    names = "a";
    populations="a";
    countrycodes="a";
    District = "a";
    
    names2="a";
    populations2="a";
    continents="a";
    life="a";
    print("aaaaa")
    
    if request.method == 'POST':
        
        try: 
            print("bbbbbbbb") 
            
            cur.execute("SELECT name, population, Continent, LifeExpectancy FROM country WHERE Continent = %s",(request.form['worldSearch'],))
            
        except:
            print("Error executing select")
        results4=cur.fetchall()
    
    if request.method == 'POST':
        
        try: 
            print("bbbbbbbb") 
            
            cur.execute("SELECT name, population, Continent, LifeExpectancy FROM country WHERE name = %s",(request.form['worldSearch'],))
            
        except:
            print("Error executing select")
        results=cur.fetchall()
        
    if request.method == 'POST':
        
        try: 
            print("bbbbbbbb") 
            
            cur.execute("SELECT name, population, Continent, LifeExpectancy FROM country WHERE Code = %s",(request.form['worldSearch'],))
            
        except:
            print("Error executing select")
        results3=cur.fetchall()
        
   
        
        
    if request.method == 'POST':
        
        try: 
           
            
            cur.execute("SELECT name, population, CountryCode, District FROM City WHERE name = %s",(request.form['worldSearch'],))
            
            
            #name, population, CountryCode, District
        except:
            print("Error executing select")
        results2=cur.fetchall()
        
    
        print("cccccc")
    
        for (key, value) in request.form.items():
            print key, value
        #a=request.form['namecheckbox']
        if 'namecheckbox' in request.form:
            names="b";
        if 'population' in request.form:
            populations="b";
        if 'countrycode' in request.form:
            countrycodes="b";
        if 'district' in request.form:
            District="b";
            
        if 'namecheckbox2' in request.form:
            names2="b";
        if 'population2' in request.form:
            populations2="b";
        if 'continent' in request.form:
            continents="b";
        if 'life' in request.form:
            life="b";
        
    return render_template('index.html', selectedMenu='Home',countries=results,countries2=results3,countries3=results4,cities=results2,columnname=names,columnpop=populations,columncode=countrycodes,columndistrict=District,columnname2=names2,columnpop2=populations2,columncode2=continents,columndistrict2=life)

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)


 #cur.execute("""SELECT Name FROM country WHERE Name LIKE(worldSearch)
 #           VALUES (%s);""",
 #           (request.form['worldSearch']))
# cur.execute("""SELECT Name FROM country WHERE Name LIKE(worldSearch);""",(request.form['worldSearch']))