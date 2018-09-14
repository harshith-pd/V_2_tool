pipeline{
agent any
stages{
stage("parallel stages"){
  parallel{
    stage("stage1"){
      steps{
        echo "stage 1"
      }
    }
    stage("stage2"){
      steps{
        echo "stage 2"
      }
    }
  }
}
}
}
