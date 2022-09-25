from flask import Flask, send_from_directory, request
import transformers
import datasets
import torch
from transformers import OPTForSequenceClassification, pipeline, AutoTokenizer

app = Flask(__name__)

@app.route('/')
def base():
    return send_from_directory('public','index.html')

@app.route('/<path:path>')
def home(path):
    return send_from_directory('public',path)

@app.route('/analyse',methods=['GET','POST'])
def analyse():
    try:
        model = OPTForSequenceClassification.from_pretrained("./yy_tuned",num_labels=2)
        tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
        analysis = pipeline(task="zero-shot-classification",model=model,tokenizer=tokenizer) 
        sentence = request.args.get('text')
        labels = ['spam','ham']
        results = analysis(sentence,labels)
        return results
    except Exception as e:
        print(e)
    return "Error",400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, use_reloader=False)

