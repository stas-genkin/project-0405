pipeline {
  agent any

  options {
    skipDefaultCheckout(true)
    timestamps()
  }

  triggers {
    cron('* * * * *')
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh '''
          echo "WORKSPACE=$WORKSPACE"
          ls -la "$WORKSPACE"
        '''
      }
    }

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
            sh '''
              TARGET="$WORKSPACE/app.py"
              if [ ! -f "$TARGET" ]; then
                echo "app.py not found at $TARGET, searching..." >&2
                TARGET_FOUND=$(find "$WORKSPACE" -maxdepth 3 -type f -name "app.py" | head -n1)
                if [ -z "$TARGET_FOUND" ]; then
                  echo "app.py not found in workspace (skip run)" >&2
                  exit 0
                fi
                TARGET="$TARGET_FOUND"
              fi
              echo "Using: $TARGET"
              python3 "$TARGET"
            '''
            echo 'Hello from secondBranch'
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

  post {
    always {
      echo "Build finished with status: ${currentBuild.currentResult}"
    }
  }
}

