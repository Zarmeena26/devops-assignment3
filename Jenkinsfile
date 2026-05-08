pipeline {
    agent any

    stages {

        stage('Code Linting') {
            steps {
                echo 'Running Linting Stage'

                sh '''
                    python3 -m pip install flake8 --break-system-packages
                    python3 -m flake8 app/ || true
                '''
            }
        }

        stage('Code Build') {
            steps {
                echo 'Building Docker Image'

                sh '''
                    docker build -t flask-app ./app
                '''
            }
        }

        stage('Containerized Deployment') {
            steps {
                echo 'Deploying Container'

                sh '''
                    docker stop flask-container || true
                    docker rm flask-container || true

                    docker run -d \
                    --name flask-container \
                    -p 5000:5000 \
                    flask-app
                '''
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                echo 'Running Selenium Tests'

                sh '''
                    rm -rf venv

                    python3 -m venv venv
                    . venv/bin/activate

                    pip install --no-cache-dir selenium webdriver-manager

                    python3 tests/test_homepage.py
                    python3 tests/test_title.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline Execution Finished'

            cleanWs()
        }
    }
}
