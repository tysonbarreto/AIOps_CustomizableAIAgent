pipeline{
    agent any
    environment{
        SONAR_PROJECT_KEY = 'AIOps_CustomizableAIAgent'
		SONAR_SCANNER_HOME = tool 'Sonarqube'
        AWS_REGION = 'eu-north-1'
        ECR_REPO = 'aiops-agents'
        IMAGE_TAG = 'latest'
    }
    stages{
        stage("Clonning GitHub Repo to Jenkins"){
            steps{
                script{
                    echo 'Clonning Github Repo...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/tysonbarreto/AIOps_CustomizableAIAgent.git']])

                }
        }
    }
        stage('Sonarqube Analysis'){
            steps{
                withCredentials([string(credentialsId:'sonarqube-token',variable:'SONAR_TOKEN')]){
                    withSonarQubeEnv('Sonarqube'){
                        sh"""
                        ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                        -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://sonarqube-dind:9000 \
                        -Dsonar.login=${SONAR_TOKEN}
                        """
                    }
                }
            }
        }
        stage('Build and Push Docker Image to ECR') {
                steps {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-token']]) {
                        script {
                            def accountId = sh(script: "aws sts get-caller-identity --query Account --output text", returnStdout: true).trim()
                            def ecrUrl = "${accountId}.dkr.ecr.${env.AWS_REGION}.amazonaws.com/${env.ECR_REPO}"

                            sh """
                            aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ecrUrl}
                            docker build -t ${env.ECR_REPO}:${IMAGE_TAG} .
                            docker tag ${env.ECR_REPO}:${IMAGE_TAG} ${ecrUrl}:${IMAGE_TAG}
                            docker push ${ecrUrl}:${IMAGE_TAG}
                            """
                        }
                    }
                }
            }
}
}