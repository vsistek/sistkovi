#!/bin/bash
set -x
cd `dirname $0`
cd ..

mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

VERSION=`date -u +%Y%m%d%H%M`
cp rpm/sistkovi.spec ~/rpmbuild/SPECS/
sed -i "s/-VERSION-/$VERSION/g" ~/rpmbuild/SPECS/sistkovi.spec

rm ~/rpmbuild/SOURCES/sistkovi.tar.gz
mkdir ~/rpmbuild/SOURCES/sistkovi-1
cp -r www nginx ~/rpmbuild/SOURCES/sistkovi-1/
( cd ~/rpmbuild/SOURCES/; tar cvzf sistkovi.tar.gz sistkovi-1 )
rm -r ~/rpmbuild/SOURCES/sistkovi-1

rpmbuild -bb -v ~/rpmbuild/SPECS/sistkovi.spec

rm rpm/*.rpm
cp ~/rpmbuild/RPMS/noarch/*.rpm rpm/
