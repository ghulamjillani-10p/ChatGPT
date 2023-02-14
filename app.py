from flask import Flask, render_template, request
import openai
import webbrowser

app = Flask(__name__)
API_KEY = # Add key here
openai.api_key = API_KEY
model = 'text-davinci-003'
file_content = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global file_content
    if request.method == 'POST':
        prompt = request.form['prompt']
        uploaded_file = request.files['file']
        if uploaded_file:
            file_content = uploaded_file.read()
        if file_content:
            prompt1 = prompt + '\n' + file_content.decode('utf-8')
            response = openai.Completion.create(
                prompt=prompt1,
                model=model, 
                max_tokens=2500
            )
            res = response.choices[0].text
            htmlstring = res
            with open("code.html", "w") as file:
                file.write(htmlstring)
            #webbrowser.open("code.html")
            return render_template('index.html', response=res, prompt=prompt)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
