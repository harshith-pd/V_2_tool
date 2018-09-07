pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        sh 'echo "code synced from git"'
        script{
          try{
            sh "pyht"
          }
          catch {
            sh 'echo "command not installed"'
          }
        }
      }
    }
  }
}
