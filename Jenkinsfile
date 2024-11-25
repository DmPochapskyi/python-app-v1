pipeline {
    agent any

    environment {
        APP_NAME = "python-docker-app"
        IMAGE_NAME = "python-docker-app"
        TAG = "latest"
        APP_PORT = "5000" //app port
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/DmPochapskyi/python-app-v1.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t ${IMAGE_NAME}:${TAG} .
                '''
            }
        }
        stage('Update Services with Docker Compose') {
            steps {
                sh '''
                echo "Updating services with Docker Compose..."
                docker-compose up -d --build --no-recreate
                '''
            }
        }
        stage('Test Application') {
            steps {
                sh '''
                echo "Testing application..."
                sleep 5
                curl -s http://localhost:${APP_PORT} | grep "Hello, World!"
                '''
            }
        }
    }
    post {
        always {
            script {
                echo "Pipeline finished."
                sh '''
                docker ps
                echo "Services are running."
                '''
            }
        }
    }
}
