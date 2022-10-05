from flask import Flask
from flask import request
import random

app = Flask(__name__)

notes = ["I am a man", 22];

@app.route("/")
def hello_world():
    return "hello";




@app.get('/')
def login_get():
    return "Hello"

@app.get('/notes')
def get_note():
    return notes;

@app.get('/notes/<index>')
def get_note_by_index(index):
    return notes[index];

@app.put('/notes/<index>')
def add_content_to_notes(index,request):
    content = request.form['content']
    notes[index] = content;
    return {index, content};


@app.post('/notes')
def post_all_notes(request):
    note = request.form['content']
    notes.append(note);
    index = len(notes) - 1;
    return {index, note};

@app.delete('/notes/<index>')
def del_note_by_index(index):
    notes[index] = null;
    return 204;

@app.post('/notes/<index>')
def sliceing_notes_by_index(index):
    content = request.form['content'];
    return {notes[index, content]};

@app.post("/documents")
def print_documents():
    docId = random.randint(1, 1000000000000);
    f = open("{}.txt".format(docId), "x")
    return {docId};

@app.get('/documents/<id>')
def get_documents(id):
    f = open("{}.txt".format(id), "r")
    return {"docId":id, "content":f.read() };

@app.get('/math/<num1>/<num2>/<amount>')
def calc(num1, num2, amount):
    
    for x in range(amount):
        num1 * num2;
    return "Done";

memo = {};

@app.get('/factorial/<num>')
def get_factorial(num):
    product = 1;
    for x in range(num+1):
        product *= num;
    return product;


"""
@app.get('coordinates/<amount>')
def get_coordinates(amonut):
    coordinates = [];
    for x in range(amonut):
        lat = random.randint(0, 180);
        long = random.randint(180, 360);
        nsHemisphere = "North" if lat > 0  else "south";
        ewHemisphere = "East" if long > 0 else "west";
        coordinate = {lat, long, nsHemisphere, ewHemisphere};
        coordinates.append(coordinate);
    return coordinates;
"""



@app.post('/login')
def login_post():
    return do_the_login()