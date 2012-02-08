# SPEC file for sidplay2, primary target is the Fedora Extras
# RPM repository. Based on the RPM for Mandriva.

Name:		sidplay
Version:	2.0.9
Release:	12%{?dist}
Summary:	A command-line tool for playing back SID files
URL:		http://sidplay2.sourceforge.net/
Group:		Applications/Multimedia
Source:		http://downloads.sourceforge.net/sidplay2/%{name}-%{version}.tar.gz
# Patch lifted from Debian
# http://packages.debian.org/unstable/oldlibs/sidplay
Patch0:		sidplay_2.0.9-5.diff.gz
Patch1:		gcc440.patch
Patch2:		sidplay-alsa.patch
Patch3:		sidplay-autohell-fixes.patch
License:	GPLv2+
BuildRequires:	libsidplay-devel
BuildRequires:	sidplay-libs-devel >= 2.1.1-11
BuildRequires:	libstdc++-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	alsa-lib-devel
Provides:	sidplay2 = %{version}-%{release}
Obsoletes:	sidplay2 < %{version}-%{release}

%description
Sidplay2 is the second in the Sidplay series and provides a console
front end for the libsidplay2 library.  This library is cycle accurate
for improved sound reproduction and is capable of playing all C64 mono
and stereo file formats.  Also supported is a full C64 emulation
environment, which allows tunes to be taken directly from the C64
without the need for special modifications.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
ACLOCAL='aclocal -I unix' autoreconf -v --force --install
%configure --with-sidbuilders=%{_libdir} --with-alsa
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{_mandir}/man*/*
%{_bindir}/*

%changelog
* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep  8 2011 Hans de Goede <j.w.r.degoede@gmail.com> - 2.0.9-11
- Rebuild against new sidplay-libs with dynamic builders

* Thu Sep 10 2009 Linus Walleij <triad@df.lth.se> 2.0.9-10
- Requires alsa-lib-devel too!

* Thu Sep 10 2009 Linus Walleij <triad@df.lth.se> 2.0.9-9
- Think it BuildRequires libtool then it'll build I hope?

* Mon Sep 7 2009 Bernie Innocenti <bernie@codewiz.org> 2.0.9-8
- Add sidplay-alsa.patch, stolen from Gentoo
- Add sidplay-autohell-fixes.patch, rolled in house
- Rock!

* Mon May 11 2009 Linus Walleij <triad@df.lth.se> 2.0.9-7
- Located a suspect GCC 4.4.0 rebuild bug.

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.0.9-6
- rebuild for new F11 features

* Wed Nov 13 2008 Linus Walleij <triad@df.lth.se> 2.0.9-5
- Fixed the scratch build issue, needed the static libs.

* Wed Nov 12 2008 Linus Walleij <triad@df.lth.se> 2.0.9-4
- Import into RPMFusion.
- Update to latest Debian patchset.

* Mon Nov 19 2007 Linus Walleij <triad@df.lth.se> 2.0.9-3
- Rebuild from Debian patchset.

* Thu Sep 15 2005 Linus Walleij <triad@df.lth.se> 2.0.9-2
- Fixed dependency on libsidplay.

* Sun Sep 11 2005 Linus Walleij <triad@df.lth.se> 2.0.9-1
- First try at a sidplay2 RPM for Fedora Extras.

* Wed Aug 24 2005 Goetz Waschk <waschk@mandriva.org> 2.0.9-2mdk
- Rebuild

* Mon Jul 26 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.0.9-1mdk
- requires new sidutils
- New release 2.0.9

* Sun Jun  6 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-4mdk
- fix deps
- source URL
- rebuild for g++

* Tue Oct  7 2003 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-3mdk
- drop prefix
- fix buildrequires

* Mon Apr 14 2003 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-2mdk
- fix buildrequires

* Mon Dec 30 2002 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-1mdk
- new version

* Fri Dec 20 2002 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-0.20021220.1mdk
- fix build with automake1.6
- new snapshot

* Thu Nov 14 2002 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-0.20021114.1mdk
- new snapshot

* Mon Oct  7 2002 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-0.20021007.1mdk
- new snapshot
- better buildrequires

* Tue Sep  3 2002 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-0.20020903.1mdk
- new snapshot

* Fri Aug 16 2002 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-0.20020729.2mdk
- rebuild with gcc 3.2-0.3mdk

* Mon Jul 29 2002 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-0.20020729.1mdk
- update from CVS

* Sun May 26 2002 Goetz Waschk <waschk@linux-mandrake.com> 2.0.8-0.20020526.1mdk
- update to CVS version

* Mon Nov  5 2001 Goetz Waschk <waschk@linux-mandrake.com> 2.0.7-3mdk
- add Obsoletes tag for sidplay2 package

* Thu Apr 19 2001 Goetz Waschk <waschk@linux-mandrake.com> 2.0.7-2mdk
- adapted for Mandrake

* Sun Apr 1 2001 Simon White <s_a_white@email.com> 2.0.7-1mdk
- First spec file.
