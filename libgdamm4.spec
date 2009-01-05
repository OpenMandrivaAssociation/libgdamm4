%define shortname gdamm
%define origname libgdamm
# api is the part of the library name before the .so
%define api 4.0
# major is the part of the library name after the .so
%define major 10
%define lib_name %mklibname %{shortname} %{api} %{major}
%define develname %mklibname gdamm %{api} -d

Name:           libgdamm4

#(!) summary for SRPM only
Summary:        C++ wrappers for libgda
Version:        3.99.7
Group: 		System/Libraries
License:	LGPLv2+
Release:        %mkrel 2
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgdamm/2.9/%{origname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  glibmm2.4-devel
BuildRequires:  libgda4.0-devel >= 3.99.7

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
%configure2_5x --enable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
# ..
# include the major number (and api if present) in the file list to catch
#changes on version upgrade
%doc AUTHORS COPYING ChangeLog NEWS
%{_libdir}/lib*-%{api}.so.%{major}*

%files -n %{develname}
%{_includedir}/libgdamm-%api
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/libgdamm-%api
%{_libdir}/pkgconfig/*.pc
