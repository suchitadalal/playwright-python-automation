pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install playwright pytest pytest-json-report'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}