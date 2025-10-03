pipeline{
    agent any
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
                        tool Sonarqube/bin/sonar-scanner \
                        -Dsonar.projectKey=AIOps_CustomizableAIAgent \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://sonarqube-dind:9000 \
                        -Dsonar.login=${SONAR_TOKEN}
                        """
                    }
                }
            }
        }
}
}