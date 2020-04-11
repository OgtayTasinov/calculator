pipeline {
    agent {
        label 'generic'
    }
    stages {
        stage("Setup script") {
            steps {
                sh """
                    pip install --upgrade pip4
                    pip3 install pytest
                """
            } // steps
        } // stage
        stage("Run unit tests") {
            steps {
                sh """
                    python -m pytest
                """
            } // steps
        } // stage
    } // stages
    post {
        always {
            sh """
                pip uninstall pytest -y
            """
        } // always
    } // post
}// pipeline