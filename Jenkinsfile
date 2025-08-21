pipeline {
  agent any
  triggers { cron('* * * * *') }

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
              TARGET="$WORKSPACE/main.py"
              if [ ! -f "$TARGET" ]; then
                echo "main.py not found at $TARGET, searching..." >&2
                TARGET_FOUND=$(find "$WORKSPACE" -maxdepth 3 -type f -name "main.py" | head -n1)
                if [ -z "$TARGET_FOUND" ]; then
                  echo "main.py not found in workspace" >&2
                  exit 2
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
}

