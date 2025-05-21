pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        echo "Code checkout complete."
      }
    }

    stage('Build') {
      steps {
        echo "Building project..."
        sh 'cat index.html || echo "index.html not found"'
      }
    }

    stage('Install Dependencies') {
      steps {
        sh '''
          python3 -m venv venv
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
