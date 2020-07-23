from project import app
from project.model import Eval
from flask import render_template
from flask import request

@app.route('/')
def start(): # Function to render the initial page
    return render_template('main.html')

@app.route('/main',methods=['GET','POST'])
def evaluate(): # Catch the information insert in the webpage and direct to model (rule)
    if request.method == 'POST':
        colection = Eval()
        info = dict()
        info['nome'] = request.form['nome']
        info['email'] = request.form['email']
        info['htmlskill'] = request.form['html_skill']
        info['cssskill'] = request.form['css_skill']
        info['javascriptskill'] = request.form['javascript_skill']
        info['pythonskill'] = request.form['python_skill']
        info['djangoskill'] = request.form['django_skill']
        info['iosskill'] = request.form['ios_skill']
        info['androidskill'] = request.form['android_skill']
        colection.show_string(info)
        return render_template('result.html')
    return render_template('main.html')
