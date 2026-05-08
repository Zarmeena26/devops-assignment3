pipeline {
    agent any
    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -t flask-app ./app'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker stop flask-container || true && docker rm flask-container || true'
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }
    }
}
