pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                script {
                    retry(3) {
                        sh "docker build -t abakhar217/abakhar:${env.BUILD_NUMBER}_Heart ."
                    }
                }
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerpassword', usernameVariable: 'dockeruser')]) {
                    sh "docker login -u $dockeruser -p $dockerpassword"
                    sh "docker push abakhar217/abakhar:${env.BUILD_NUMBER}_Heart"
                }
            }
        }
        stage('deploy') {
            steps {
                // Create Kubernetes Deployment
                sh '''
                cat <<EOF | kubectl apply -f -
                apiVersion: apps/v1
                kind: Deployment
                metadata:
                  name: abakhar-heart-deployment
                spec:
                  replicas: 1
                  selector:
                    matchLabels:
                      app: abakhar-heart
                  template:
                    metadata:
                      labels:
                        app: abakhar-heart
                    spec:
                      containers:
                      - name: abakhar-heart-container
                        image: abakhar217/abakhar:${env.BUILD_NUMBER}_Heart
                        ports:
                        - containerPort: 5000
                EOF
                '''

                // Create Kubernetes Service
                sh '''
                cat <<EOF | kubectl apply -f -
                apiVersion: v1
                kind: Service
                metadata:
                  name: abakhar-heart-service
                spec:
                  type: LoadBalancer
                  ports:
                  - port: 81
                    targetPort: 5000
                  selector:
                    app: abakhar-heart
                EOF
                '''
            }
        }
    }
}
