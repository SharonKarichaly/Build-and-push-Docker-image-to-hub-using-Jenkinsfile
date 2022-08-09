pipeline {
    agent any 
    environment {
    DOCKERHUB_CREDENTIALS = credentials('Docker-Python')
    }
    stages { 
        stage('SCM Checkout') {
            steps{
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SharonKarichaly/Build-and-push-Docker-image-to-hub-using-Jenkinsfile.git']]])
            }
        }

        stage('Build docker image') {
            steps {  
                sh 'docker build -t ksharon/python:latest .'
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push image') {
            steps{
                sh sh 'docker push ksharon/python:latest'
            }
        }
}
post {
        always {
            sh 'docker logout'
        }
    }
}
