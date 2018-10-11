pipeline {
  agent any
  triggers {
    pollSCM('* * * * *')
  }
  options {
    buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
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
            sh '''echo "Checking for Java "
                  java -version
                  echo "Checking for python3"
                  python3 --version
                  echo "Checking for the wkhtmltopdf"
                  wkhtmltopdf --version || echo "Please make sure the wkhtmltopdf version 0.12.5 is installed && exit 1"
                  '''
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
              def rootPath = "${env.WORKSPACE}/test_apps"
              def app_list_file = "${env.WORKSPACE}/app_files.txt"

              sh "ls $rootPath > $app_list_file"
              def test_apps_array = readFile( "$app_list_file" ).split( "\\r?\\n" );
              sh "rm -f $app_list_file"
                for (item in test_apps_array){
                 stage ("test on ${item}"){
                    sh "echo ${env.WORKSPACE}"
                    sh "echo ${item}"
                    sh "${env.WORKSPACE}/install_and_configure.sh -input_app_file=\"test_apps/${item}\""
                    //assert fileExists("${env.WORKSPACE}/last_run/report/assessment_report.pdf") : "Report generation failed"
                    //assert readFile("${env.WORKSPACE}/last_run/report/assessment_report.pdf") : "Report generated but not readable"
                 }
                stage ("Archive artifacts for ${item}") {
                        archiveArtifacts artifacts: 'last_run/**/report/**/*', fingerprint: true
                  }
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
//////////////////////////////////////////////////////////////////////////////////////////

}
