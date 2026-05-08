pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Run Container') {
            steps {
                // Stops old container if it exists, then runs new one
                sh 'docker stop flask-container || true && docker rm flask-container || true'
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }
        stage('Selenium Tests') {
            steps {
                sh 'source venv/bin/activate && python3 tests/test_homepage.py'
                sh 'source venv/bin/activate && python3 tests/test_title.py'
            }
        }
    }
}
