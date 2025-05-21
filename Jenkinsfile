pipeline {
  agent any

  tools {
    git 'Default'
  }

  stages {
    stage('Checkout') {
      steps {
        echo "Checked out code"
      }
    }
    stage('Build') {
      steps {
        echo "Building project..."
        sh 'cat index.html'
      }
    }
  }

  post {
    success {
      echo "Build succeeded!"
    }
    failure {
      echo "Build failed."
    }
  }
}
