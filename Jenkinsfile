pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t devops-demo:1.0 .
                '''
            }
        }
    }
}
