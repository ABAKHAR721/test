//windows pipeline
pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                // Build the Docker image
                bat "docker build -t abakhar217/abakhar:${env.BUILD_NUMBER}_Heart ."
                
                // Docker login with credentials stored in Jenkins
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerpassword', usernameVariable: 'dockeruser')]) {
                    bat "docker login -u %dockeruser% -p %dockerpassword%"
                    bat "docker push abakhar217/abakhar:${env.BUILD_NUMBER}_Heart"
                }
            }
        }
        stage('Deploy') {
            steps {
                // Run the Docker container
                bat "docker run -d -p 5001:5000 abakhar217/abakhar:${env.BUILD_NUMBER}_Heart"
            }
        }
    }
}
