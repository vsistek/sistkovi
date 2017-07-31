pipeline {
    agent none

    stages {
        stage('build') {
            steps {
                docker.image('jenkins-rpmbuild').inside('-v /srv/pkgrepo:/pkgrepo:rw') {
                    checkout scm
                    sh('HOME=/home/jenkins; rpm/buildrpm.sh')
                    sh('cp rpm/*.rpm /pkgrepo/; createrepo_c --update /pkgrepo')
                }
            }
        }
        stage('deploy') {
            steps {
                node('master') {
                    sh('sudo /usr/bin/zypper update -y --repo vsistek')
                }
            }
        }
    }
}
