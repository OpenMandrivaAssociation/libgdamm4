%define shortname	gdamm
%define origname	libgdamm

%define api		5.0
%define major		13
%define lib_name 	%mklibname %{shortname} %{api} %{major}
%define develname	%mklibname gdamm %{api} -d

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:           %{origname}%{api}
Summary:        C++ wrappers for libgda
Version:        4.99.11
Release:	1
Group: 		System/Libraries
License:	LGPLv2+
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/%{origname}/%{url_ver}/%{origname}-%{version}.tar.xz
BuildRequires:	pkgconfig(glibmm-2.4) >= 2.27.93
BuildRequires:	pkgconfig(libgda-5.0) >= 5.0.2

%description
C++ wrappers for libgda. libgdamm is part of a set of powerful
C++ bindings for the GNOME libraries, which provide additional
functionality above GTK+/gtkmm.

%package -n     %{lib_name}
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
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains headers and libraries that programmers will need
to develop applications which use libgdamm.

%prep
%setup -q -n %{origname}-%{version}

%build
%configure2_5x --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%files -n %{lib_name}
%doc AUTHORS ChangeLog NEWS
%{_libdir}/lib*-%{api}.so.%{major}{,.*}

%files -n %{develname}
%doc %_datadir/doc/libgdamm-%api
%doc %_datadir/devhelp/books/libgdamm-%api
%{_includedir}/libgdamm-%api
%{_libdir}/*.so
%{_libdir}/libgdamm-%api
%{_libdir}/pkgconfig/*.pc
