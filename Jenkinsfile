pipeline {
    agent any

    stages {
        stage('Code Linting') {
            steps {
                sh 'pip install --user flake8'
                sh '~/.local/bin/flake8 app/ || true' // || true prevents build fail on minor style issues
            }
        }

        stage('Code Build') {
            steps {
                sh 'docker build -t flask-app ./app'
            }
        }

        stage('Containerized Deployment') {
            steps {
                sh 'docker stop flask-container || true && docker rm flask-container || true'
                sh 'docker run -d --name flask-container -p 5000:5000 flask-app'
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                // Ensure your 'tests' folder has its own Dockerfile
                sh 'docker build -t selenium-tests ./tests'
                sh 'docker run --network host selenium-tests'
            }
        }
    }
}
