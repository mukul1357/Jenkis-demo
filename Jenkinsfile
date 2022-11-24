pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/BThangaraju/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x prime_tester.py"
                sh "./prime_tester.py"
            }
        }
        stage('Test Code 1') {
            steps {
                sh "chmod u+x rTest.py"
                sh "./rTest.py"
            }
        }
        stage('Test Code 2') {
            steps {
                sh "chmod u+x fTest.py"
                sh "./fTest.py"
            }
        }
    } 
}
