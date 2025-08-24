pipeline {
  agent any

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
          steps { sh 'echo firstBranch running' }
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

    stage('Docker build & push') {
      when {
        expression { fileExists('Dockerfile') }
      }
      steps {
        sh 'echo "docker build & push goes here (optional)"'
      }
    }
  }
}


