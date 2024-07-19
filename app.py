from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

def get_domain_info(domain_name):
    try:
        result = subprocess.run(['whois', domain_name], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    domain_name = request.form['domain_name']
    domain_info = get_domain_info(domain_name)
    return render_template('index.html', domain_info=domain_info)

if __name__ == '__main__':
    app.run(debug=True)
