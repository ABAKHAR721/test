pipeline {
    agent {
        label 'lsi_agent'  // Assuming this is your Windows agent
    }
    stages {
        stage('Build') {
            steps {
                // Use the Windows batch syntax for environment variables
                bat 'docker build -t abakhar217/abakhar:%BUILD_NUMBER% .'
                
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerpassword', usernameVariable: 'dockeruser')]) {
                    // Correct environment variable syntax for Windows
                    bat "docker login -u %dockeruser% -p %dockerpassword%"
                    bat "docker push abakhar217/abakhar:%BUILD_NUMBER%"
                }
            }
        }
        stage('Deploy') {
            steps {
                // Correct environment variable syntax for Windows
                bat "docker run -d -p 5000:5000 abakhar217/abakhar:%BUILD_NUMBER%"
            }
        }
    }
}
