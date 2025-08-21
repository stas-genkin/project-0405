pipeline {
  agent any

  options {
    skipDefaultCheckout(true)
    timestamps()
  }

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

    stage('Setup Python venv & install deps') {
      steps {
        sh '''
          set -euxo pipefail
          export PATH="$HOME/.local/bin:$PATH"
          PY=python3
          VENV_DIR="$WORKSPACE/.venv"

          # try stdlib venv; if it fails (ensurepip missing), fall back to virtualenv
          if $PY -m venv "$VENV_DIR" 2>/dev/null; then
            echo "Created venv with stdlib"
          else
            echo "stdlib venv failed; falling back to virtualenv"
            $PY -m pip install --user --upgrade pip virtualenv
            virtualenv "$VENV_DIR"
          fi

          . "$VENV_DIR/bin/activate"
          python -V
          pip --version
          pip install --upgrade pip

          if [ -f "$WORKSPACE/requirements.txt" ]; then
            pip install -r "$WORKSPACE/requirements.txt"
          else
            pip install flask || true
          fi

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
          steps { sh 'echo firstBranch running' }
        }
        stage('secondBranch') {
          steps {
            sh '''
              set -euxo pipefail
              VENV_DIR="$WORKSPACE/.venv"
              . "$VENV_DIR/bin/activate"

              TARGET="$WORKSPACE/app.py"
              if [ ! -f "$TARGET" ]; then
                TARGET=$(find "$WORKSPACE" -maxdepth 3 -type f -name "app.py" | head -n1 || true)
              fi

              if [ -z "${TARGET:-}" ]; then
                echo "app.py not found in workspace; skipping run" >&2
                exit 0
              fi

              echo "Using: $TARGET"
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

