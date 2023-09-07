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

        // stage('Install packages for Jenkins') {
        //     agent {
        //         docker {
        //             image 'python:3.8' 
        //         }
        //     }
        //     steps {
                
        //         echo 'Testing model correctness..'
                
        //         // sh 'python3 -m venv env && . ./env/bin/activate'
        //         // sh 'pip3 install --upgrade pip'
        //         sh 'pip install wget && pip install unzip --user'
        //     }
        // }
        stage('Clean old Image') {
            // agent {
            //     docker {
            //         image 'python:3.8' 
            //     }
            // }    

            steps {
                def a = currentBuild.previousBuild.number
                echo " TAG ${a} "
                def a2 = $($BUILD_NUMBER - 1)
                echo " TAG ${a2} "
                script { 
                    // def a = $($BUILD_NUMBER - 1)
                    // echo " TAG ${a} "
                    // echo "imageTag: ${imageTag}..."
                    // def imageName = "${registry}"
                    // env.imageName = "${imageName}"
                    // def oldImageID = sh( 
                    //                         script: 'docker images -qf reference=\${imageName}:\${imageTag}',
                    //                         returnStdout: true
                    //                     )

                    // echo "Image Name: " + "${imageName}"
                    // echo "Old Image: ${oldImageID}"

                    // if ( "${oldImageID}" != '' ) {
                    //     echo "Deleting image id: ${oldImageID}..."
                    //     sh "docker rmi -f ${oldImageID}"
                    // } else {
                    //     echo "No image to delete..."
                    //     } 
                }  
            }
        }

        // stage('Build') {
        //     // steps {
        //     //     echo 'Building image for deployment..'
        //     // }
        //     agent {
        //         docker {
        //             image 'python:3.8' 
        //         }
        //     }         
        //     steps {
        //         sh 'pip install gdown && pip install unzip'
        //         sh 'gdown 16k5MBIqa1w7eUdbIyVNllavM6I7pba0U && unzip -o model_storage.zip'
        //         sh 'curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
        //             && tar xzvf docker-17.04.0-ce.tgz \
        //             && mv docker/docker /usr/local/bin \
        //             && rm -r docker docker-17.04.0-ce.tgz'
               
        //         script {
        //             echo 'Building image for deployment..'
        //             dockerImage = docker.build registry + ":$BUILD_NUMBER" 
        //             echo 'Pushing image to dockerhub..'
        //             docker.withRegistry( '', registryCredential ) {
        //                 // dockerImage.push()
        //                 dockerImage.push('latest')
        //             }
        //             // sh "docker rmi -f ${dockerImage}"
        //         }
        //     }
        // }
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
