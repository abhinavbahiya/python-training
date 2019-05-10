import flask

app = flask.Flask('myapp')

@app.route('/')
def homePage():
    return 'Welcome'

@app.route('/home')
def home():
    return 'Home'

@app.route('/about')
def about():
    return 'About'
# login

@app.route('/verifylogin', methods=['post'])
def verifyLogin():
    u = flask.request.form.get('uname')
    p = flask.request.form.get('pwd')
    if u and p:
        return 'Good'
    else:
        #return 'Hell'
        #bottle.TEMPLATE_PATH.append(r'C:\Abhinav\bin')
        import sqlite3
        con = sqlite3.connect('mydb.sqlite3')
        cur = con.cursor()
        cur.execute('SELECT * from LOGDATA')
        result = cur.fetchall()
        return flask.render_template('report.html', res = result)

@app.route('/empid/<int:eid>') #only int is allowed
def empid(eid):
    return str(eid)

#not supported in flask
#@app.route('/regex/<r:re:[a-z0-9]+>')
#def regex(r):
#    return r

@app.route('/fpath/<path:p>')
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
    res = flask.jsonify(res)
    return res

@app.route('/download/<fname>')
def downloadfile(fname):
    return flask.static_file(filename=fname, directory=r'C:\Abhinav\bin', download=True)

import requests



@app.errorhandler(404)
def errorPage(err):
    return 'Page under construction'



app.run(port = 3000)

resp = requests.get('http://127.0.0.1:3000/json')
resp = resp.json()
print(resp)