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
            steps {
                echo 'Testing models..'
            }
            script {
                sh 'gdown gdown 16k5MBIqa1w7eUdbIyVNllavM6I7pba0U && unzip model_storage.zip'
            }
        }
        stage('Build') {
            steps {
                // sh 'docker build -t ocr_app .'
                script {
                    echo 'Building image for deployment..'
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                    echo 'Pushing image to dockerhub..'
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying models..'
                echo 'Running a script to trigger pull and start a docker container'
            }
        }
    }
}