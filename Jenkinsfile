pipeline {
    agent any

    stages {
        // stage("Fix the permission issue") {
        //     steps {
        //         sh "sudo chown root:jenkins /run/docker.sock"
        //     }

        // }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.8' 
                }
            }
            steps {
                
                echo 'Testing model correctness..'
                
                // sh 'python3 -m venv env && . ./env/bin/activate'
                // sh 'pip3 install --upgrade pip3'
                sh 'pip install -r requirements.txt '
            }
        }
        stage('Build') {
            steps {
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
                withKubeConfig(caCertificate: '', clusterName: '', contextName: '', credentialsId: 'K8S', namespace: '', restrictKubeConfigAccess: false, serverUrl: '') {
                    echo 'Running deployment'
                    sh "helm upgrade --install k8sdemo ./helm/" 
                }
            }
        }
    }
}
