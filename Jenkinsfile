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
          ./test.sh
      }
      }
      stage('Build') {
         steps {
          ./build.sh
      }
      }
      stage('Run') {
         steps {
          ./runner.sh
      }
      }
   }
}
