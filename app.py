from flask import Flask, render_template, request
import openai
import webbrowser
import requests

app = Flask(__name__)
API_KEY = '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'
openai.api_key = API_KEY
model = 'text-davinci-003'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Completion.create(
            prompt=prompt,
            model=model, 
            max_tokens=2500
        )
        res = response.choices[0].text
        htmlstring = res
        with open("code.html", "w") as file:
            file.write(htmlstring)
            
        generated_code = res

        webbrowser.open("code.html")
        return render_template('index.html', response=res)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
