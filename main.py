from flask import Flask, render_template

app = Flask('Dictionary_API')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def translate(word):
    translation = word.capitalize()
    return {'Word:': word,
            'Translation: ': translation}


app.run(debug=True)
