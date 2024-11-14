pipeline {
    agent {
        label 'lsi_agent'  // Assuming this is your Windows agent
    }
    stages {
        stage('Build') {
            steps {
                bat 'docker build -t abakhar217/abakhar:${env.BUILD_NUMBER} .'
                
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerpassword', usernameVariable: 'dockeruser')]) {
                    bat "docker login -u %dockeruser% -p %dockerpassword%"
                    bat "docker push abakhar217/abakhar:${env.BUILD_NUMBER}"
                }
            }
        }
        stage('Deploy') {
            steps {
                bat "docker run -d -p 5000:5000 abakhar217/abakhar:${env.BUILD_NUMBER}"
            }
        }
    }
}
