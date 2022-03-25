pipeline {
    agent any
    stages {
        stage('Submit Stack') {
            steps {
            sh "aws cloudformation create-stack --stack-name subhashssm --template-body file://cfnpracat.yml --region 'ap-south-1'"
              }
             }
            }
            }
