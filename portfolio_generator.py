from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def generate_portfolio():
    # Read configuration from a JSON file
    with open('portfolio_config.json', 'r') as file:
        config = json.load(file)

    return render_template('portfolio_template.html', config=config)

if __name__ == '__main__':
    app.run(debug=True)
