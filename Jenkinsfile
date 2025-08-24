pipeline {
  agent any

  triggers {
    cron('* * * * *')
  }

  stages {
    stage('Hello') {
      steps {
        echo 'Hello World'
        sh 'echo hi'
      }
    }

    stage('Hello again') {
      steps {
        echo 'Hello World'
        sh 'echo hi'
      }
    }

    stage('build docker image') {
      parallel {
        stage('firstBranch') {
          steps {
            sh 'echo firstBranch running'
          }
        }
        stage('secondBranch') {
          steps {
            echo 'Hello from secondBranch'
            sh 'echo hi'
          }
        }
      }
    }

    stage('push to hub') {
      steps {
        echo 'Hello World'
        sh 'echo hi'
      }
    }
  }
}

