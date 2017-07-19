def rpmbuild = docker.image('jenkins-rpmbuild')

rpmbuild.inside('-v /srv/pkgrepo:/pkgrepo:rw') {
    stage("checkout") {
        git '/srv/git/sistkovi.git'
    }
    stage("build") {
        sh('HOME=/home/jenkins; rpm/buildrpm.sh')
    }
    stage("repo") {
        sh('cp rpm/*.rpm /pkgrepo/; createrepo_c --update /pkgrepo')
    }
}

node('master') {
    stage("deploy") {
        sh('sudo /usr/bin/zypper update -y --repo vsistek')
    }
}
