import bottle

app = bottle.Bottle()

@app.route('/')
def homePage():
    return 'Welcome'

@app.route('/home')
def home():
    return 'Home'

@app.route('/about')
def about():
    return 'About'

@app.post('verifylogin')
def verifyLogin():
    u = bottle.request.forms.get('uname')
    p = bottle.request.forms.get('pwd')
    if u and p:
        return 'Good'
    else:
        #return 'Hell'
        bottle.TEMPLATE_PATH.append(r'C:\Abhinav\bin')
        import sqlite3
        con = sqlite3.connect('mydb.sqlite3')
        cur = con.cursor()
        cur.execute('SELECT * from LOGDATA')
        result = cur.fetchall()
        return bottle.template('report.tpl', res = result)

@app.route('/empid/<eid:int>') #only int is allowed
def empid(eid):
    return str(eid)

@app.route('/regex/<r:re:[a-z0-9]+>')
def regex(r):
    return r

@app.route('/fpath/<p:path>')
def fpath(p):
    return str(p)
    #return str(bottle.request.filter)

@app.route('/json')
def json():
    D = {'a': 10, 'b': 12}
    F = open('mydata.json', 'w')

    import json

    json.dump(D,F)
    F.close()

    F = open('mydata.json')
    res = json.load(F)
    F.close()
    return res

@app.route('/download/<fname>')
def downloadfile(fname):
    return bottle.static_file(filename=fname, root=r'C:\Abhinav\bin', download=True)

import requests



@app.error(404)
def errorPage(err):
    return 'Page under construction'



app.run(port = 3000)

resp = requests.get('http://127.0.0.1:3000/json')
resp = resp.json()
print(resp)