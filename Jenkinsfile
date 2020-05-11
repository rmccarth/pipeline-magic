pipeline {
   agent any
   stages {
      stage('Fetch') {
         steps {
            sh 'git config --global user.email "rob.mccarthy31@gmail.com"'
            sh 'git config --global user.name "rmccarth"'
            git 'https://github.com/rmccarth/pipeline-magic.git'
            sh 'git checkout -B dev'
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
                        sh('''
                           git config --local credential.helper "!f() { echo username=\\$GIT_USERNAME; echo password=\\$GIT_PASSWORD; }; f"
                           git add .
                           git commit -m "adding artifact to repo from jenkins"
                           git push origin dev:master
                        ''')
               }
      }
      }
   }
}
