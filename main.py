from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    file=open("data.txt","r")
    text=file.readlines()
    file.close()
    print(text)
    return render_template('index.html',template_text=text)
  
@app.route('/message', methods = ['GET', 'POST'])
def message():
  if request.method == 'GET':
    file=open("data.txt","r")
    text=file.readlines()
    file.close()
    print(text)
    return render_template('index.html',template_text=text)
    
  if request.method == 'POST':
    print("POST")
    text=request.form['text']
    print(text)
    file=open("data.txt","a")
    file.write("\n"+text)
    file.close()
    return render_template('index.html',template_text=text)
    
@app.route('/clear', methods = ['GET','DELETE'])
def delete():
  file=open("data.txt","w")
  file.write("")
  file.close()
  return render_template('index.html',template_text="  ")
