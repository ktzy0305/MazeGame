pipeline {
    agent { 
        dockerfile true
    }
    stages {
        stage('build') {
            steps {
                sh 'pytest -v --cov'
            }
        }
        stage('test') {
            steps {
                sh 'pytest -v --cov'
            }
        }
        stage('deploy') {
            steps {
                sh 'pytest -v --cov'
            }
        }
    }
}