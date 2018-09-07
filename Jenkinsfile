pipeline {
  agent any
  triggers { pollSCM('* * * * *') }
  stages {
    stage('checkout') {
      steps {
        sh 'echo "code synced from git"'
        script{
          try{
            sh "python3 --version"
            sh "java --verison"
          }
          catch (Exception e){
            sh 'echo "command not installed"'
            println (e)
            exit 1
          }
        }
      }
    }
  }
}
