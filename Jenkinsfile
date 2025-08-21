pipeline {
  agent any

  options {
    skipDefaultCheckout(true)
    timestamps()
  }

  triggers { pollSCM('* * * * *') }

  environment {
    VENV_DIR = "${WORKSPACE}/.venv"
    DOCKER_IMAGE = "stasgenkin/0405-app:latest"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh '''#!/usr/bin/env bash
set -Eeuo pipefail
echo "WORKSPACE=$WORKSPACE"
ls -la "$WORKSPACE"
'''
      }
    }

    stage('Python venv + deps') {
      steps {
        sh '''#!/usr/bin/env bash
set -Eeuo pipefail
export PATH="$HOME/.local/bin:$PATH"
PY=python3

# try stdlib venv; fallback to virtualenv if ensurepip missing
if "$PY" -m venv "$VENV_DIR" 2>/dev/null; then
  echo "venv created with stdlib"
else
  echo "stdlib venv failed; using virtualenv"
  "$PY" -m pip install --user --upgrade pip virtualenv
  virtualenv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"
python -V
pip --version
pip install --upgrade pip
[ -f "$WORKSPACE/requirements.txt" ] && pip install -r "$WORKSPACE/requirements.txt" || true
pip list
'''
      }
    }

    stage('Hello') {
      steps {
        echo 'Hello World'
        sh '''#!/usr/bin/env bash
set -Eeuo pipefail
echo hi
'''
      }
    }

    stage('Hello again') {
      steps {
        echo 'Hello World'
        sh '''#!/usr/bin/env bash
set -Eeuo pipefail
echo hi
'''
      }
    }

    stage('build docker image') {
      parallel {
        stage('firstBranch') {
          steps {
            sh '''#!/usr/bin/env bash
set -Eeuo pipefail
echo firstBranch running
'''
          }
        }
        stage('secondBranch') {
          steps {
            sh '''#!/usr/bin/env bash
set -Eeuo pipefail
source "$VENV_DIR/bin/activate"

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

    stage('Docker build (optional)') {
      when { expression { return fileExists("${WORKSPACE}/Dockerfile") } }
      steps {
        sh '''#!/usr/bin/env bash
set -Eeuo pipefail
if ! command -v docker >/dev/null 2>&1; then
  echo "Docker not available, skipping"
  exit 0
fi
docker build -t "${DOCKER_IMAGE}" "$WORKSPACE"
echo "Built ${DOCKER_IMAGE}"
'''
      }
    }

    stage('Deploy to Kubernetes (manifests)') {
      when { expression { return fileExists("${WORKSPACE}/deployment.yaml") } }
      steps {
        sh '''#!/usr/bin/env bash
set -Eeuo pipefail
if ! command -v kubectl >/dev/null 2>&1; then
  echo "kubectl not available, skipping"
  exit 0
fi
kubectl config current-context || { echo "no kube context, skipping"; exit 0; }

kubectl apply -f "$WORKSPACE/configmap.yaml"    || true
kubectl apply -f "$WORKSPACE/secret.yaml"       || true
kubectl apply -f "$WORKSPACE/deployment.yaml"   || true
kubectl apply -f "$WORKSPACE/service.yaml"      || true
kubectl apply -f "$WORKSPACE/hpa.yaml"          || true
kubectl apply -f "$WORKSPACE/cronjob.yaml"      || true

kubectl get pods,svc,hpa
'''
      }
    }
  }

  post {
    always {
      echo "Build finished with status: ${currentBuild.currentResult}"
    }
  }
}

