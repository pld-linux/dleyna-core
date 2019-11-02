Summary:	UPnP and DLNA core library
Name:		dleyna-core
Version:	0.5.0
Release:	3
License:	LGPL v2
Group:		Libraries
Source0:	https://01.org/sites/default/files/downloads/dleyna/%{name}-%{version}.tar.gz
# Source0-md5:	f9fca59e28f01608bbe98d193184f729
Patch0:		gupnp-1.2.patch
URL:		https://01.org/dleyna/
BuildRequires:	autoconf >= 2.66
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gupnp-devel >= 0.20.5
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig >= 1:0.16
Requires:	glib2 >= 1:2.28.0
Requires:	gupnp >= 0.20.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of utility functions that are used by the higher level dLeyna
libraries to communicate with DLNA devices. It provides APIs for
logging, error, settings and task management, and an IPC abstraction.

%package devel
Summary:	Development files for dleyna-core library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	gupnp-devel >= 0.20.5

%description devel
This package provides development files for dleyna-core library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/dleyna-1.0/connectors

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libdleyna-core-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdleyna-core-1.0.so.4
%dir %{_libdir}/dleyna-1.0
%dir %{_libdir}/dleyna-1.0/connectors

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdleyna-core-1.0.so
%dir %{_includedir}/dleyna-1.0
%{_includedir}/dleyna-1.0/libdleyna
%{_pkgconfigdir}/dleyna-core-1.0.pc
