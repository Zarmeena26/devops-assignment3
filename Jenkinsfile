pipeline {
    agent any

    stages {
        stage('Code Linting') {
            steps {
                echo 'Running Linting Stage'
                // Using --break-system-packages to bypass Ubuntu 24.04 restrictions
                sh 'pip install flake8 --break-system-packages'
                // || true ensures the pipeline continues even if there are style warnings
                sh 'python3 -m flake8 app/ || true'
            }
        }

        stage('Code Build') {
            steps {
                echo 'Building Docker Image'
                sh 'docker build -t flask-app ./app'
            }
        }

        stage('Containerized Deployment') {
            steps {
                echo 'Deploying Container'
                // Stops and removes the old container to free up port 5000
                sh 'docker stop flask-container || true && docker rm flask-container || true'
                sh 'docker run -d --name flask-container -p 5000:5000 flask-app'
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                echo 'Running Selenium Tests'
                sh '''
                    # Setup fresh environment inside Jenkins workspace
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install selenium webdriver-manager
                    # Run tests (ensure your scripts use Headless mode!)
                    python3 tests/test_homepage.py
                    python3 tests/test_title.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline Execution Finished'
        }
    }
}
