pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello sunshine v2'
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
