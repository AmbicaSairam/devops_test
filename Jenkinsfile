pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t app .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }
}
