pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo "Testing"
                sh "python3 -m pytest test_reverse_factorial.py"
                
            }
        }
    }
}
