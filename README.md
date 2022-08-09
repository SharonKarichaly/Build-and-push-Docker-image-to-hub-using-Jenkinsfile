
How to build and push a docker image to dockerhub using Jenkinsfile

# FlowDiagram

<img width="724" alt="Screenshot 2022-08-09 at 4 12 10 PM" src="https://user-images.githubusercontent.com/106381638/183634394-2aa5004b-d382-4819-b4ae-3d2881f5d3f7.png">

# Objective

Here I containerised a python application first, Then save the source code and the Dockerfile into GitHub. Using Jenkins we will checkout the code from GitHub. Then create the docker image using the Dockerfile into the Jenkins node. Once the image is ready we will push it to the docker hub. 

Currently I am pushing this image into my private repository, In production environment we can push images to our organisation project repository and other developers can pull and use the image and work collabaretively.

# Prerequisites:
1. Install the Docker Pipelines plugin on Jenkins
2. Create secret token from Docker Hub and Setup the Jenkins Credential for dockerhub account
3. Docker to be installed on the Jenkins node where we are building the image.
4. jenkins user should be added to the docker group #sudo usermod -a -G docker jenkins

# Creation of Jenkinsfile

1. Set environment variable in Jenkins Pipeline.where dockerhub-sharon is the id used when defining the Docker Hub credentials in Jenkins.

```
environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-sharon')
    }
```
3. Checkout latest code from Github

```
stages { 
        stage('SCM Checkout') {
            steps{
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SharonKarichaly/Build-and-push-Docker-image-to-hub-using-Jenkinsfile.git']]])
            }
        }
```

5. Build docker image using Dockerfile

```
        stage('Build docker image') {
            steps {  
                sh 'docker build -t ksharon/python:latest .'
            }
        }
```

7. Logging in to Docker Hub


```
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
```

9. Push Image to Docker Hub

```
        stage('push image') {
            steps{
                sh 'docker push ksharon/python:latest'
            }
        }
```

11. Logout from Docker Hub
```
post {
        always {
            sh 'docker logout'
        }
    }
```





