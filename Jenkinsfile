pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                jobDsl(sandbox: true, removedJobAction: 'DELETE', removedViewAction: 'DELETE',
                        targets: 'jobs/*.groovy', unstableOnDeprecation: true)
            }
        }
    }
}
