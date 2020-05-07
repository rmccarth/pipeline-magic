pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
            git 'https://github.com/rmccarth/pipeline-magic.git'

            sh "./build.sh"
         }

      }
      stage('Test') {
          steps {
            sh "./test.sh"
          }
      }
      stage('Deploy') {
          steps {
            echo "We deploy"
          }
      }
   }
}
