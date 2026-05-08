from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    # Changed text to verify the CI/CD pipeline works
    return "DevOps Assignment - CI/CD Pipeline Tested Successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
