pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                // Points to the 'app' directory where your Dockerfile lives
                sh 'docker build -t flask-app ./app'
            }
        }

        stage('Run Container') {
            steps {
                // Stops and removes old container if it exists to avoid port 5000 conflicts
                sh 'docker stop flask-container || true && docker rm flask-container || true'
                // Runs the new container
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }

        stage('Selenium Tests') {
            steps {
                sh '''
                    # Creates a fresh virtual environment inside Jenkins workspace
                    python3 -m venv venv
                    . venv/bin/activate
                    # Installs dependencies needed for the tests
                    pip install selenium webdriver-manager
                    # Runs both test cases
                    python3 tests/test_homepage.py
                    python3 tests/test_title.py
                '''
            }
        }
    }
    
    post {
        always {
            // Optional: Clean up workspace to save disk space on your EC2
            cleanWs()
        }
    }
}
