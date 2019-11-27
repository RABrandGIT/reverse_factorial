pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo "Testing"
                sh "pytest test_reverse_factorial.py"
                
            }
        }
    }
}
