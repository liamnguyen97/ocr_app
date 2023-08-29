pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello sunshine'
            }
        }
        stage('Deploy') {
            steps {
                withKubeConfig(caCertificate: '', clusterName: '', contextName: '', credentialsId: 'K8S', namespace: '', restrictKubeConfigAccess: false, serverUrl: '') {
                    sh "helm upgrade --install k8sdemo ./helm/" 
                }
            }
        }
    }
}
