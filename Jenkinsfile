pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'python3 src/api/routes/tests/test_routes_general.py'
            }
        }
        stage('Build') {
            steps {
                sh('''
                    pip install -r src/requirements.txt
                    python3 -m pip install --user --upgrade setuptools wheel
                    python3 setup.py sdist bdist_wheel

               ''')
            }
        }
    }
}
