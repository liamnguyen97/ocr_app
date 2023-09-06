pipeline {
    agent any
    environment{
        registry = 'dongnguyen18891/ocr_app'
        registryCredential = 'dockerhub'      
    }
    stages {
        // stage("Fix the permission issue") {
        //     steps {
        //         sh "sudo chown root:jenkins /run/docker.sock"
        //     }

        // }

        stage('Install packages for Jenkins') {
            agent {
                docker {
                    image 'python:3.8' 
                }
            }
            steps {
                
                echo 'Testing model correctness..'
                
                // sh 'python3 -m venv env && . ./env/bin/activate'
                // sh 'pip3 install --upgrade pip'
                sh 'pip install wget && pip install unzip --user'
            }
        }
        stage('Build') {
            steps {
                sh 'wget https://drive.google.com/file/d/16k5MBIqa1w7eUdbIyVNllavM6I7pba0U/view?usp=drive_link'
                sh 'unzip model_storage.zip model_storage'
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
        // stage('Deploy') {
        //     steps {
        //         withKubeConfig(caCertificate: '', clusterName: '', contextName: '', credentialsId: 'K8S', namespace: '', restrictKubeConfigAccess: false, serverUrl: '') {
        //             echo 'Running deployment'
        //             sh "helm upgrade --install k8sdemo ./helm/" 
        //         }
        //     }
        // }
    }
}
