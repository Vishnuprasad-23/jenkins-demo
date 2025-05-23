pipeline {
  agent any

  stages {
    stage('Install Python & Dependencies') {
      steps {
        sh '''
          which python3 || (apt-get update && apt-get install -y python3 python3-pip python3-venv)
          python3 -m venv venv
          . venv/bin/activate
          pip install -U pip pytest
        '''
      }
    }

    stage('Run Tests') {
      steps {
        sh '''
          . venv/bin/activate
          pytest
        '''
      }
    }

    stage('Lint') {
      steps {
        sh '''
          . venv/bin/activate
          pip install flake8
          flake8 calculator.py
        '''
      }
    }
  }

  post {
    always {
      echo 'Build or tests failed.'
    }
  }
}
