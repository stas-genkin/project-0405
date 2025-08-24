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



stage('Docker build & push') {
  when { expression { return fileExists("${WORKSPACE}/Dockerfile") } }
  steps {
    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PWD', usernameVariable: 'DOCKER_USER')]) {
      sh '''#!/usr/bin/env bash
set -Eeuo pipefail
IMAGE="stasgenkin/0405-app:latest"

docker --version || { echo "Docker not available, skipping"; exit 0; }

echo "$DOCKER_PWD" | docker login -u "$DOCKER_USER" --password-stdin
docker build -t "$IMAGE" "$WORKSPACE"
docker push "$IMAGE"
docker logout
'''
    }
  }
}

