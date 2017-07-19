#
# spec file for package sistkovi
#
# Copyright (c) 2017 Vaclav Sistek
#

Name:           sistkovi
Version:	1
Release:	-VERSION-
Vendor:		Vaclav Sistek
License:	GPLv3
Summary:	sistkovi.cz website
Url:		http://www.sistkovi.cz/
Group:		Unspecified
Source:		sistkovi.tar.gz
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:	nginx

%description
sistkovi.cz website files and nginx configuration

%prep
%setup -q

%build


%install
rm -rf %{buildroot}
install -d 	%{buildroot}/srv/www/sistkovi.cz
install -d 	%{buildroot}/srv/www/sistkovi.cz/www
install -m 644 	www/index.html %{buildroot}/srv/www/sistkovi.cz/www/index.html
install -m 644 	www/dary.html %{buildroot}/srv/www/sistkovi.cz/www/dary.html
install -m 644 	www/english.html %{buildroot}/srv/www/sistkovi.cz/www/english.html
install -m 644 	www/harmonogram.html %{buildroot}/srv/www/sistkovi.cz/www/harmonogram.html
install -m 644  www/obrad.html %{buildroot}/srv/www/sistkovi.cz/www/obrad.html
install -m 644  www/oslava.html %{buildroot}/srv/www/sistkovi.cz/www/oslava.html
install -m 644  www/ubytovani.html %{buildroot}/srv/www/sistkovi.cz/www/ubytovani.html
install -m 644  www/fotoalbum.html %{buildroot}/srv/www/sistkovi.cz/www/fotoalbum.html
install -d 	%{buildroot}/srv/www/sistkovi.cz/www/css
install -m 644	www/css/main.css %{buildroot}/srv/www/sistkovi.cz/www/css/main.css
install -m 644  www/css/jquery.lightbox-0.5.css %{buildroot}/srv/www/sistkovi.cz/www/css/jquery.lightbox-0.5.css
install -d	%{buildroot}/srv/www/sistkovi.cz/www/images
install -m 644	www/images/favicon.png %{buildroot}/srv/www/sistkovi.cz/www/images/favicon.png
install -m 644	www/images/cats-linocut.png %{buildroot}/srv/www/sistkovi.cz/www/images/cats-linocut.png
install -m 644  www/images/cce.png %{buildroot}/srv/www/sistkovi.cz/www/images/cce.png
install -m 644  www/images/lightbox-blank.gif %{buildroot}/srv/www/sistkovi.cz/www/images/lightbox-blank.gif
install -m 644  www/images/lightbox-btn-close.gif %{buildroot}/srv/www/sistkovi.cz/www/images/lightbox-btn-close.gif
install -m 644  www/images/lightbox-btn-next.gif %{buildroot}/srv/www/sistkovi.cz/www/images/lightbox-btn-next.gif
install -m 644  www/images/lightbox-btn-prev.gif %{buildroot}/srv/www/sistkovi.cz/www/images/lightbox-btn-prev.gif
install -m 644  www/images/lightbox-ico-loading.gif %{buildroot}/srv/www/sistkovi.cz/www/images/lightbox-ico-loading.gif
install -d  %{buildroot}/srv/www/sistkovi.cz/www/js
install -m 644  www/js/jquery.js %{buildroot}/srv/www/sistkovi.cz/www/js/jquery.js
install -m 644  www/js/jquery.lightbox-0.5.min.js %{buildroot}/srv/www/sistkovi.cz/www/js/jquery.lightbox-0.5.min.js
install -d  %{buildroot}/srv/www/sistkovi.cz/www/photos
install -m 644  www/photos/01.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/01.jpg
install -m 644  www/photos/02.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/02.jpg
install -m 644  www/photos/03.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/03.jpg
install -m 644  www/photos/04.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/04.jpg
install -m 644  www/photos/r05.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r05.jpg
install -m 644  www/photos/r06.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r06.jpg
install -m 644  www/photos/r07.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r07.jpg
install -m 644  www/photos/r08.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r08.jpg
install -m 644  www/photos/r09.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r09.jpg
install -m 644  www/photos/r10.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r10.jpg
install -m 644  www/photos/r11.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r11.jpg
install -m 644  www/photos/r12.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r12.jpg
install -m 644  www/photos/r13.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r13.jpg
install -m 644  www/photos/r14.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r14.jpg
install -m 644  www/photos/r15.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r15.jpg
install -m 644  www/photos/r16.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r16.jpg
install -m 644  www/photos/r17.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r17.jpg
install -m 644  www/photos/r18.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r18.jpg
install -m 644  www/photos/r19.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r19.jpg
install -m 644  www/photos/r20.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r20.jpg
install -m 644  www/photos/r21.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r21.jpg
install -m 644  www/photos/r22.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r22.jpg
install -m 644  www/photos/r23.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r23.jpg
install -m 644  www/photos/r24.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r24.jpg
install -m 644  www/photos/r25.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r25.jpg
install -m 644  www/photos/r26.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r26.jpg
install -m 644  www/photos/r27.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r27.jpg
install -m 644  www/photos/r28.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/r28.jpg
install -m 644  www/photos/thumb_01.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_01.jpg
install -m 644  www/photos/thumb_02.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_02.jpg
install -m 644  www/photos/thumb_03.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_03.jpg
install -m 644  www/photos/thumb_04.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_04.jpg
install -m 644  www/photos/thumb_r05.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r05.jpg
install -m 644  www/photos/thumb_r06.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r06.jpg
install -m 644  www/photos/thumb_r07.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r07.jpg
install -m 644  www/photos/thumb_r08.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r08.jpg
install -m 644  www/photos/thumb_r09.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r09.jpg
install -m 644  www/photos/thumb_r10.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r10.jpg
install -m 644  www/photos/thumb_r11.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r11.jpg
install -m 644  www/photos/thumb_r12.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r12.jpg
install -m 644  www/photos/thumb_r13.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r13.jpg
install -m 644  www/photos/thumb_r14.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r14.jpg
install -m 644  www/photos/thumb_r15.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r15.jpg
install -m 644  www/photos/thumb_r16.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r16.jpg
install -m 644  www/photos/thumb_r17.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r17.jpg
install -m 644  www/photos/thumb_r18.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r18.jpg
install -m 644  www/photos/thumb_r19.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r19.jpg
install -m 644  www/photos/thumb_r20.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r20.jpg
install -m 644  www/photos/thumb_r21.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r21.jpg
install -m 644  www/photos/thumb_r22.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r22.jpg
install -m 644  www/photos/thumb_r23.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r23.jpg
install -m 644  www/photos/thumb_r24.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r24.jpg
install -m 644  www/photos/thumb_r25.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r25.jpg
install -m 644  www/photos/thumb_r26.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r26.jpg
install -m 644  www/photos/thumb_r27.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r27.jpg
install -m 644  www/photos/thumb_r28.jpg %{buildroot}/srv/www/sistkovi.cz/www/photos/thumb_r28.jpg
install -d	%{buildroot}/etc/nginx/vhosts.d
install -m 644	nginx/sistkovi.cz.conf %{buildroot}/etc/nginx/vhosts.d/sistkovi.cz.conf

%post
echo Reloading nginx.
/usr/bin/systemctl reload nginx

%files
%dir /srv/www/sistkovi.cz
%dir /srv/www/sistkovi.cz/www
%dir /srv/www/sistkovi.cz/www/css
%dir /srv/www/sistkovi.cz/www/images
%dir /srv/www/sistkovi.cz/www/js
%dir /srv/www/sistkovi.cz/www/photos
%defattr(-,root,root)
/srv/www/sistkovi.cz/www/index.html
/srv/www/sistkovi.cz/www/dary.html
/srv/www/sistkovi.cz/www/english.html
/srv/www/sistkovi.cz/www/harmonogram.html
/srv/www/sistkovi.cz/www/obrad.html
/srv/www/sistkovi.cz/www/oslava.html
/srv/www/sistkovi.cz/www/ubytovani.html
/srv/www/sistkovi.cz/www/fotoalbum.html
/srv/www/sistkovi.cz/www/css/main.css
/srv/www/sistkovi.cz/www/css/jquery.lightbox-0.5.css
/srv/www/sistkovi.cz/www/images/favicon.png
/srv/www/sistkovi.cz/www/images/cats-linocut.png
/srv/www/sistkovi.cz/www/images/cce.png
/srv/www/sistkovi.cz/www/images/lightbox-blank.gif
/srv/www/sistkovi.cz/www/images/lightbox-btn-close.gif
/srv/www/sistkovi.cz/www/images/lightbox-btn-next.gif
/srv/www/sistkovi.cz/www/images/lightbox-btn-prev.gif
/srv/www/sistkovi.cz/www/images/lightbox-ico-loading.gif
/srv/www/sistkovi.cz/www/js/jquery.js
/srv/www/sistkovi.cz/www/js/jquery.lightbox-0.5.min.js
/srv/www/sistkovi.cz/www/photos/01.jpg
/srv/www/sistkovi.cz/www/photos/02.jpg
/srv/www/sistkovi.cz/www/photos/03.jpg
/srv/www/sistkovi.cz/www/photos/04.jpg
/srv/www/sistkovi.cz/www/photos/r05.jpg
/srv/www/sistkovi.cz/www/photos/r06.jpg
/srv/www/sistkovi.cz/www/photos/r07.jpg
/srv/www/sistkovi.cz/www/photos/r08.jpg
/srv/www/sistkovi.cz/www/photos/r09.jpg
/srv/www/sistkovi.cz/www/photos/r10.jpg
/srv/www/sistkovi.cz/www/photos/r11.jpg
/srv/www/sistkovi.cz/www/photos/r12.jpg
/srv/www/sistkovi.cz/www/photos/r13.jpg
/srv/www/sistkovi.cz/www/photos/r14.jpg
/srv/www/sistkovi.cz/www/photos/r15.jpg
/srv/www/sistkovi.cz/www/photos/r16.jpg
/srv/www/sistkovi.cz/www/photos/r17.jpg
/srv/www/sistkovi.cz/www/photos/r18.jpg
/srv/www/sistkovi.cz/www/photos/r19.jpg
/srv/www/sistkovi.cz/www/photos/r20.jpg
/srv/www/sistkovi.cz/www/photos/r21.jpg
/srv/www/sistkovi.cz/www/photos/r22.jpg
/srv/www/sistkovi.cz/www/photos/r23.jpg
/srv/www/sistkovi.cz/www/photos/r24.jpg
/srv/www/sistkovi.cz/www/photos/r25.jpg
/srv/www/sistkovi.cz/www/photos/r26.jpg
/srv/www/sistkovi.cz/www/photos/r27.jpg
/srv/www/sistkovi.cz/www/photos/r28.jpg
/srv/www/sistkovi.cz/www/photos/thumb_01.jpg
/srv/www/sistkovi.cz/www/photos/thumb_02.jpg
/srv/www/sistkovi.cz/www/photos/thumb_03.jpg
/srv/www/sistkovi.cz/www/photos/thumb_04.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r05.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r06.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r07.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r08.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r09.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r10.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r11.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r12.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r13.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r14.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r15.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r16.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r17.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r18.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r19.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r20.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r21.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r22.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r23.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r24.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r25.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r26.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r27.jpg
/srv/www/sistkovi.cz/www/photos/thumb_r28.jpg
/etc/nginx/vhosts.d/sistkovi.cz.conf

