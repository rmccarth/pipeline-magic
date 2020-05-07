pipeline {
   agent any

   stages {
      stage('Build') {
         steps {
            git 'https://github.com/rmccarth/pipeline-magic.git'
            echo "running build"
            sh "./build.sh"
         }
      }
      stage('Test') {
          steps {
            echo "running test"

            def testResult = ./test.sh
            if (testResult == 'Failed') {
               error "test failed"
            }
            
          }
      }
      stage('Deploy') {
          steps {
            echo "We deploy"
          }
      }
   }
}
