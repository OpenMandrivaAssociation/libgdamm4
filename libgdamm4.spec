%define shortname gdamm
%define origname libgdamm
# api is the part of the library name before the .so
%define api 4.0
# major is the part of the library name after the .so
%define major 13
%define lib_name %mklibname %{shortname} %{api} %{major}
%define develname %mklibname gdamm %{api} -d

Name:           libgdamm4

#(!) summary for SRPM only
Summary:        C++ wrappers for libgda
Version:        4.1.3
Group: 		System/Libraries
License:	LGPLv2+
Release:        2
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgdamm/%{origname}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  glibmm2.4-devel >= 2.27.93
BuildRequires:  libgda4.0-devel >= 4.1.7
BuildRequires:	gnome-common

#Full and generic description of the whole package. (this will be the SRPM
#description only)
%description
C++ wrappers for libgda. libgdamm is part of a set of powerful
C++ bindings for the GNOME libraries, which provide additional
functionality above GTK+/gtkmm.

#main package (contains ''.so.[major].''' only)
%package -n     %{lib_name}

#(!) summary for main lib RPM only
Summary:        Main library for gdamm
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{lib_name}
C++ wrappers for libgda. libgdamm is part of a set of powerful
C++ bindings for the GNOME libraries, which provide additional
functionality above GTK+/gtkmm.

%package -n     %{develname}
Summary:        Headers for developing programs that will use gda
Group:          Development/GNOME and GTK+
Requires:       %{lib_name} = %{version}
#(!) '''''MANDATORY'''''
Provides:       %{lib_name}-devel = %{version}-%{release}
#(!) '''''MANDATORY'''''
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains headers and libraries that programmers will need
to develop applications which use libgdamm.

%prep
%setup -q -n %{origname}-%{version}

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure2_5x --enable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT


%files -n %{lib_name}
# ..
# include the major number (and api if present) in the file list to catch
#changes on version upgrade
%doc AUTHORS ChangeLog NEWS
%{_libdir}/lib*-%{api}.so.%{major}*

%files -n %{develname}
%doc %_datadir/doc/libgdamm-%api
%doc %_datadir/devhelp/books/libgdamm-%api
%{_includedir}/libgdamm-%api
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/libgdamm-%api
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Sep 22 2011 Götz Waschk <waschk@mandriva.org> 4.1.3-1mdv2012.0
+ Revision: 700828
- new version
- xz tarball

* Mon Apr 04 2011 Funda Wang <fwang@mandriva.org> 4.1.2-1
+ Revision: 650227
- rebuild
- update to new version 4.1.2

* Sat Oct 16 2010 Götz Waschk <waschk@mandriva.org> 4.1.1-1mdv2011.0
+ Revision: 586125
- update to new version 4.1.1
- spec file cleanup

* Fri Aug 06 2010 Götz Waschk <waschk@mandriva.org> 3.99.21-1mdv2011.0
+ Revision: 567068
- update to new version 3.99.21
- new version
- bump libgda dep

* Thu Feb 25 2010 Götz Waschk <waschk@mandriva.org> 3.99.19-1mdv2010.1
+ Revision: 511311
- update to new version 3.99.19

* Sat Aug 29 2009 Götz Waschk <waschk@mandriva.org> 3.99.17.1-1mdv2010.0
+ Revision: 422128
- update to new version 3.99.17.1

* Wed Aug 26 2009 Götz Waschk <waschk@mandriva.org> 3.99.17-1mdv2010.0
+ Revision: 421494
- new version
- new major
- update file list

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 3.99.16-1mdv2010.0
+ Revision: 390562
- update to new version 3.99.16

* Mon Jun 01 2009 Götz Waschk <waschk@mandriva.org> 3.99.15-1mdv2010.0
+ Revision: 381867
- new version
- new major

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 3.99.14-1mdv2009.1
+ Revision: 356298
- new version
- bump libgda4.0 dep

* Tue Mar 10 2009 Götz Waschk <waschk@mandriva.org> 3.99.13-1mdv2009.1
+ Revision: 353434
- new version

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 3.99.12-1mdv2009.1
+ Revision: 346880
- update to new version 3.99.12

* Sun Feb 15 2009 Götz Waschk <waschk@mandriva.org> 3.99.11-1mdv2009.1
+ Revision: 340679
- update to new version 3.99.11

* Fri Jan 16 2009 Götz Waschk <waschk@mandriva.org> 3.99.8-1mdv2009.1
+ Revision: 330310
- new version
- fix source URL

* Mon Jan 05 2009 Götz Waschk <waschk@mandriva.org> 3.99.7-2mdv2009.1
+ Revision: 325027
- fix license
- rename libgdamm3 package
- new version
- new api version 4.0
- new version
- rebuild

  + mandrake <mandrake@mandriva.com>
    - %repsys markrelease
      version: 3.99.7
      release: 1mdv2009.1
      revision: 324512
      Copying 3.99.7-1mdv2009.1 to releases/ directory.

  + Thierry Vignaud <tv@mandriva.org>
    - fix srpm description (extra spacing due to comments)
    - kill re-definition of %%buildroot on Pixel's request

  + Funda Wang <fwang@mandriva.org>
    - drop libmajor for devel package name
    - New version 3.0.0
    - obsoletes old devel package
    - fix libname
    - New version 2.9.81

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Jérôme Soyer <saispo@mandriva.org>
    - import libgdamm3

