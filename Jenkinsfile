pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/mukul1357/Jenkis-demo.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Prog1.py"
                sh "./Prog1.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "chmod u+x rTest.py"
                sh "./Test.py"
            }
        }
    } 
}
