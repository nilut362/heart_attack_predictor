from flask import Flask, render_template, request
import functions

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predictor')
def predictor():
    return render_template('predictor.html')

@app.route('/result',methods=['POST'])
def result():
    data = request.form.to_dict()
    prediction = functions.predictor(data)
    return render_template('result.html',data=prediction)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)