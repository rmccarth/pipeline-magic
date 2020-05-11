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
      stage('Publish') {
         //should publish a file to the git repo that indicates a successful build
         steps {
            sh 'python3 generate_Artifact.py'
            sh 'git push https://github.com/rmccarth/pipeline-magic.git'
      }
      }
   }
}
