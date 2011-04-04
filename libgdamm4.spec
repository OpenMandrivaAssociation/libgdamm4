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
Version:        4.1.2
Group: 		System/Libraries
License:	LGPLv2+
Release:        %mkrel 1
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgdamm/%{origname}-%{version}.tar.bz2
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
