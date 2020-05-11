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
            withCredentials([usernamePassword(credentialsId: 'd87d8042-fa99-4745-ab9c-ab4cfa120802', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                        sh('git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/rmccarth/pipeline-magic.git') }
      }
      }
   }
}
