pipeline {
  agent {
    docker {
      image 'python:3.10-slim'
    }
  }

  stages {
    stage('Checkout') {
      steps {
        echo "Code checkout complete."
      }
    }

    stage('Install Dependencies') {
      steps {
        sh '''
          python -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install pytest
        '''
      }
    }

    stage('Run Tests') {
      steps {
        sh '''
          . venv/bin/activate
          pytest --maxfail=1 --disable-warnings --tb=short
        '''
      }
    }
  }

  post {
    success {
      echo "Build and tests succeeded!"
    }
    failure {
      echo "Build or tests failed."
    }
  }
}
