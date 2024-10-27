pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/RahulI142/BookMarkIt.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }
    }
}
