from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET','POST'])
def facts():
    import docx2txt
    prac = docx2txt.process("iotprac.docx")
    value = str(prac)
    data = {
       'iot' : value+"/n",
        
    }
    data = json.dumps(data)
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=False)
