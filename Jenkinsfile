pipeline {
  agent any

  environment {
    DOCKERHUB_USER = 'stas696970'
    DOCKERHUB_REPO = 'flask_app'
    DOCKER_IMAGE = "${DOCKERHUB_USER}/${DOCKERHUB_REPO}:v1"
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/stas-genkin/project-0405.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE .'
      }
    }

    stage('Push to DockerHub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh 'echo $PASS | docker login -u $USER --password-stdin'
          sh 'docker push $DOCKER_IMAGE'
        }
      }
    }

    stage('Deploy with Helm') {
      steps {
        sh 'helm upgrade --install myflaskapp ./mychart --set image.repository=$DOCKERHUB_USER/$DOCKERHUB_REPO --set image.tag=v1'
      }
    }

    stage('Test Service') {
      steps {
        sh '''
          kubectl rollout status deployment/myflaskapp-mychart
          kubectl get svc
        '''
      }
    }
  }
}

