from flask import Flask, jsonify, render_template
import pandas as pd
import random
import time

app = Flask(__name__)

dataset = pd.read_excel('news_dataset.xlsx')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_news')
def get_news():
    time.sleep(5)
    
    header_index = random.randint(0, len(dataset) - 1)
    header = dataset.loc[header_index, 'header']
    label = dataset.loc[header_index, 'label']
    source = dataset.loc[header_index, 'source']
    date = dataset.loc[header_index, 'date']

    return jsonify({'header': header, 'label': label, 'source': source, 'date': date})

if __name__ == '__main__':
    app.run(debug=True)