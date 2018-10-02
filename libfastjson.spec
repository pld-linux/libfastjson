#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	A JSON implementation in C
Name:		libfastjson
Version:	0.99.8
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://download.rsyslog.com/libfastjson/%{name}-%{version}.tar.gz
# Source0-md5:	fe7b4eae1bf40499f6f92b51d7e5899e
URL:		https://github.com/rsyslog/libfastjson
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LIBFASTJSON implements a reference counting object model that allows
you to easily construct JSON objects in C, output them as JSON
formatted strings and parse JSON formatted strings back into the C
representation of JSON objects.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.4

%files devel
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_libdir}/%{name}.so
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}.a
%endif
