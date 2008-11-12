# SPEC file for sidplay2, primary target is the Fedora Extras
# RPM repository. Based on the RPM for Mandriva.

Name:		sidplay
Version:	2.0.9
Release:	4%{?dist}
Summary:	A command-line tool for playing back SID files
URL:		http://sidplay2.sourceforge.net/
Group:		Applications/Multimedia
Source:		http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Patch lifted from Debian
# http://packages.debian.org/unstable/oldlibs/sidplay
Patch0:		sidplay_2.0.9-5.diff.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License:	GPL
BuildRequires:	libsidplay-devel
BuildRequires:	sidplay-libs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	automake
BuildRequires:	autoconf
Provides:	sidplay2
Obsoletes:	sidplay2

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

%build
%configure --with-sidbuilders=%{_libdir}/sidplay/builders
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
%{_mandir}/man*/*
%{_bindir}/*

%changelog
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
