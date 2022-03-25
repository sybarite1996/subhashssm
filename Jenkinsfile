pipeline {
    agent any
    stages {
        stage('Submit Stack') {
            steps {
            sh "aws cloudformation update-stack --stack-name subhashssm --template-body file://cfnpracat.yml --region 'ap-south-1'"
              }
             }
            }
            }
