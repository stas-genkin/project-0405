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

    stage('Setup Python venv & install deps') {
      steps {
        sh '''
          set -e
          PY=python3
          $PY -V || true
          # create venv inside workspace (handles spaces and @2)
          $PY -m venv "$WORKSPACE/.venv"
          . "$WORKSPACE/.venv/bin/activate"
          pip install --upgrade pip
          if [ -f "$WORKSPACE/requirements.txt" ]; then
            pip install -r "$WORKSPACE/requirements.txt"
          else
            # minimal deps (fallback) – comment out if not needed
            pip install flask
          fi
          which python
          pip list
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
              set -e
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
              . "$WORKSPACE/.venv/bin/activate"
              python "$TARGET"
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

