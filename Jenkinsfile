pipeline {
    agent any
    stages {
        // Remove the 'Checkout' stage entirely
        stage('Build Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker stop flask-container || true && docker rm flask-container || true'
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }
        stage('Selenium Tests') {
            steps {
                // Make sure the path to your venv and tests is correct
                sh 'source venv/bin/activate && python3 tests/test_homepage.py'
                sh 'source venv/bin/activate && python3 tests/test_title.py'
            }
        }
    }
}
