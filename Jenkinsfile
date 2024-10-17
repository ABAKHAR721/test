pipeline{
    agent any 
    stages{
        stage('build'){
            steps{
                sh "docker build -t abakhar217/abakhar:${env.BUILD_NUMBER}_Heart ."
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerpassword', usernameVariable: 'dockeruser')]) {
                    sh "docker login -u $dockeruser -p $dockerpassword "
                    sh "docker push abakhar217/abakhar:${env.BUILD_NUMBER}_Heart"
                }
            }
        }
        stage('deploy'){
            steps{
                sh "docker run -d -p 5001:5000 abakhar217/abakhar:${env.BUILD_NUMBER}_Heart"
            }
        }
    }
}
