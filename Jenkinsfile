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
            python3 -m venv .venv
            .venv/bin/python -m pip install --upgrade pip
            .venv/bin/python -m pip install -r requirements.txt
        '''
    }
}

        stage('Run Tests') {
    steps {
        sh '''
            .venv/bin/python -m pytest
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
