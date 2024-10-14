pipeline{
    agent any 
    stages{
        stage('build'){
            steps{
                git branch: 'main', credentialsId: 'Github', url: 'https://github.com/ABAKHAR721/Book-Recommendation-System.git'
                
                sh "docker build -t abakhar217/abakhar:${env.BUILD_NUMBER} ."
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerpassword', usernameVariable: 'dockeruser')]) {
                    sh "docker login -u $dockeruser -p $dockerpassword "
                    sh "docker push abakhar217/abakhar:${env.BUILD_NUMBER}"
                }
            }
        }
        stage('deploy'){
            steps{
                sh "docker run -d -p 5001:5000 abakhar217/abakhar:${env.BUILD_NUMBER} "
            }
        }
    }
}
