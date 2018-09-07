pipeline {
  agent any
  triggers {
    pollSCM('* * * * *')
  }
  stages{
//////////////////////////////////////////////////////////////////////////////////////////
    stage("checkout SCM"){
      steps{
        sh 'echo "In this stage, we will sync the code from multiple SCMs"'
      }
    }
//////////////////////////////////////////////////////////////////////////////////////////
    stage("Check Dependencies"){
      steps{
        script{
          try{
            sh 'echo "Checking for Java "'
            sh 'java -version'
            sh 'echo "Checking for python3"'
            sh 'python3 --version'
          }
          catch(Exception e){
            println("Error checking dependencies : ${e.message}")
          }
        }
      }
    }
//////////////////////////////////////////////////////////////////////////////////////////
    stage("Run tests for the iOS & Android test applications"){
      steps{
          script{
            try{
              def test_array = ["demo.apk", "demo.ipa"]
              for (item in test_array){
                sh "echo ${env.WORKSPACE}"
                sh "echo ${item}"
                sh "${env.WORKSPACE}/install_and_configure.sh -input_app_file=\"${env.WORKSPACE}/${item}\""
              }
            }
            catch(Exception e){
              println("Error running the tests : ${e.message}")
            }
          }
        }
      }
//////////////////////////////////////////////////////////////////////////////////////////
  }
}
