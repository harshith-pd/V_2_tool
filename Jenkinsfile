pipeline {
  agent any
  stages {
    stage('checkout SCM') {
      steps {
        sh 'echo "In this stage, we will sync the code from multiple SCMs"'
      }
    }
    stage('Check Dependencies') {
      steps {
        script {
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
    stage('Run tests for the iOS & Android test applications') {
      parallel {
        stage('Run tests for the iOS & Android test applications') {
          steps {
            script {
              try{
                stage ("test on demo.ipa"){
                  sh "echo ${env.WORKSPACE}"
                  sh "${env.WORKSPACE}/install_and_configure.sh -input_app_file=\"${env.WORKSPACE}/demo.ipa\""
                  assert fileExists("${env.WORKSPACE}/last_run/report/assessment_report.pdf") : "Report generation failed"
                  assert readFile("${env.WORKSPACE}/last_run/report/assessment_report.pdf") : "Report generated but not readable"
                }
              }
              catch(Exception e){
                println("Error running the tests : ${e.message}")
              }
            }

          }
        }
        stage('test on demo.apk') {
          steps {
            script {
              try{
                stage ("test on demo.apk"){
                  sh "echo ${env.WORKSPACE}"
                  sh "${env.WORKSPACE}/install_and_configure.sh -input_app_file=\"${env.WORKSPACE}/demo.apk\""
                  assert fileExists("${env.WORKSPACE}/last_run/report/assessment_report.pdf") : "Report generation failed"
                  assert readFile("${env.WORKSPACE}/last_run/report/assessment_report.pdf") : "Report generated but not readable"
                }
              }
              catch(Exception e){
                println("Error running the tests : ${e.message}")
              }
            }

          }
        }
      }
    }
  }
  post {
    always {
      archiveArtifacts(artifacts: 'last_run/report/**/*', fingerprint: true)

    }

  }
  triggers {
    pollSCM('* * * * *')
  }
}
