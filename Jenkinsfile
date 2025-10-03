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
}
}