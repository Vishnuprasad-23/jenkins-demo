pipeline {
  agent any

  tools {
    git 'Default'
  }

  stages {
    stage('Checkout') {
      steps {
        // Jenkins auto-checks out when using pipeline script from SCM
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
      mail to: 'vishnuprasad2301@gmail.com',
           subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
           body: "Good news! Build ${env.BUILD_NUMBER} of ${env.JOB_NAME} succeeded.\n\nSee: ${env.BUILD_URL}"
    }
    failure {
      echo "Build failed."
      mail to: 'vishnuprasad2301@gmail.com',
           subject: "FAILURE: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
           body: "Oops! Build ${env.BUILD_NUMBER} of ${env.JOB_NAME} failed.\n\nCheck console: ${env.BUILD_URL}console"
    }
  }
}
