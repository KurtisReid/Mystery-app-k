from flask import Flask
from flask import request
from flask import jsonify
import random
import string

app = Flask(__name__)

notes = ["I am a man", 22];


@app.get('/')
def login_get():
    return 'Hello';

@app.get('/notes')
def get_note():
    return jsonify(notes);

@app.get('/notes/<int:index>')
def get_note_by_index(index):
    return jsonify(notes[index]);

@app.put('/notes/<int:index>')
def add_content_to_notes(index,request):
    content = request.get_json()['content']
    print(content);
    notes[index] = content;
    return {"index":index, "content":content};


@app.post('/notes')
def post_all_notes():
    note = request.get_json()['content']
    notes.append(note);
    index = len(notes) - 1;
    return {"index":index, "content":note};

@app.delete('/notes/<int:index>')
def del_note_by_index(index):
    notes.pop(index);
    return '', 204;

@app.post('/notes/<int:index>')
def sliceing_notes_by_index(index):
    content = request.get_json()['content'];
    notes.insert(index, content);
    print(notes[index]);
    return {"index":index, "content":notes[index]};

@app.post("/documents")
def print_documents():
    docId = ''.join(random.choices(string.ascii_lowercase, k=5));
    content = request.get_json()['content'];
    f = open("{}.txt".format(docId), "x")
    f.write(content);
    f.close();
    return docId;

@app.get('/documents/<id>')
def get_documents(id):
    f = open("{}.txt".format(id), "r")
    return {"docId":id, "content":f.read() };

@app.get('/math/<int:num1>/<int:num2>/<int:amount>')
def calc(num1, num2, amount):
    
    for x in range(amount):
        num1 * num2;
    return "Done";

memo = {};

@app.get('/factorial/<int:num>')
def get_factorial(num):
    if num in memo:
        return str(memo[num]);
    else:
        product = 1;
        for x in range(num+1):
            product *= num;
        print(product);
        return str(product);



@app.get('/coordinates/<int:amount>')
def get_coordinates(amount):
    print(amount);
    coordinates = [];
    for x in range(int(amount)):
        lat = random.randint(0, 180);
        long = random.randint(180, 360);
        nsHemisphere = "North" if lat > 0  else "south";
        ewHemisphere = "East" if long > 0 else "west";
        coordinate = {"lattitude":lat, "longitude": long, "nsHemisphere": nsHemisphere, "ewHemisphere":ewHemisphere};
        coordinates.append(coordinate);
    print(coordinates);
    return jsonify(coordinates);




@app.get('/login')
def login_post():
    return do_the_login()

def do_the_login():
    strCle = 'Hello from Cleveland'
    str2 = 'The greatest location in the nation'
    strWrong = 'Go Steelers!'
    return strCle + "\n" + str2 + "\n" + strWrong;

if __name__ == "__main__":
    app.run(debug=True)