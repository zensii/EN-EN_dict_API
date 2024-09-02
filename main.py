from flask import Flask, render_template
import pandas as pd

app = Flask('Dictionary_API')
df = pd.read_csv('dictionary.csv')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def translate(word):

    if word in df['word'].values:
        translation = df.loc[df['word'] == word]['definition'].squeeze()

        return {'Word:': word,
                'Definition: ': translation}
    else:
        return 'No such word exists in the dictionary'


translate('house')
app.run(debug=True)
