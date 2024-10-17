pipeline {
    agent {
        label 'agent1'
    } 
    stages {
        stage('build') {
            steps {
                sh "docker build -t abakhar217/abakhar:${env.BUILD_NUMBER} ."
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerpassword', usernameVariable: 'dockeruser')]) {
                    sh "docker login -u $dockeruser -p $dockerpassword"
                    sh "docker push abakhar217/abakhar:${env.BUILD_NUMBER}"
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
                  name: abakhar-main-deployment
                spec:
                  replicas: 1
                  selector:
                    matchLabels:
                      app: abakhar-main
                  template:
                    metadata:
                      labels:
                        app: abakhar-main
                    spec:
                      containers:
                      - name: abakhar-main-container
                        image: abakhar217/abakhar:${BUILD_NUMBER}
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
                  name: abakhar-main-service
                spec:
                  type: LoadBalancer
                  ports:
                  - port: 80
                    targetPort: 5000
                  selector:
                    app: abakhar-main
                EOF
                '''
            }
        }
    }
}
