pipeline {
    agent any

    options{
        buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '5'))
        timestamps()
    }

    environment{
        registry = 'dongnguyen18891/ocr_app'
        registryCredential = 'dockerhub'      
    }

    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3.8' 
                }
            }
         
            steps {
                echo 'Testing models...'
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8' 
                }
            }
            steps {
                script {
                    echo 'Building image for deployment..'
                    // sh 'pip install gdown && pip install unzip'
                    // sh 'gdown 16k5MBIqa1w7eUdbIyVNllavM6I7pba0U && unzip -o model_storage.zip'
                    // sh 'curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
                    // && tar xzvf docker-17.04.0-ce.tgz \
                    // && mv docker/docker /usr/local/bin \
                    // && rm -r docker docker-17.04.0-ce.tgz'

                    // dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                    // echo 'Pushing image to dockerhub..'
                    // docker.withRegistry( '', registryCredential ) {
                    //     dockerImage.push()
                    //     dockerImage.push('latest')
                    // }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying models..'
                echo 'Running a script to trigger pull and start a docker container'
                echo 'Check helm and kubectl command'
                sh 'helm version'
                sh 'kubectl version'
            }
        }
    }
}