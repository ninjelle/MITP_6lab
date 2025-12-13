from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    greeting = None
    name = ''
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        
        if name:
            greeting = f"Hello, {name}! Nice to see you!"
        else:
            greeting = "Please, enter your name!"
    
    return render_template('index.html', 
                         greeting=greeting, 
                         name=name)

if __name__ == '__main__':
    app.run(debug=True, port=8000)