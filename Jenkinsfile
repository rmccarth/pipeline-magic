pipeline {
   agent any
   stages {
      stage('Fetch') {
         steps {
            git 'https://github.com/rmccarth/pipeline-magic.git'
         }
      }
      stage('Test') {
         steps {
            sh 'python3 tester.py'
      }
      }
      stage('Run') {
         steps {
            sh 'python3 sample.py'
      }
      }
   }
}
