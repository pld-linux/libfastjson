#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	A JSON implementation in C
Summary(pl.UTF-8):	Implementacja JSON w C
Name:		libfastjson
Version:	0.99.8
Release:	2
License:	MIT
Group:		Libraries
Source0:	https://download.rsyslog.com/libfastjson/%{name}-%{version}.tar.gz
# Source0-md5:	fe7b4eae1bf40499f6f92b51d7e5899e
URL:		https://github.com/rsyslog/libfastjson
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LIBFASTJSON implements a reference counting object model that allows
you to easily construct JSON objects in C, output them as JSON
formatted strings and parse JSON formatted strings back into the C
representation of JSON objects.

%description -l pl.UTF-8
LIBFASTJSON implementuje model obiektów ze zliczaniem referencji,
pozwalający na łatwe konstruowanie obiektów JSON w C, wypisywanie ich
jako sformatowanych łańcuchów JSON oraz analizowanie sformatowanych
łańcuchów JSON z powrotem do reprezentacji obiektów JSON w C

%package devel
Summary:	Header files for LIBFASTJSON library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LIBFASTJSON
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LIBFASTJSON library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LIBFASTJSON.

%package static
Summary:	Static LIBFASTJSON library
Summary(pl.UTF-8):	Statyczna biblioteka LIBFASTJSON
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LIBFASTJSON library.

%description static -l pl.UTF-8
Statyczna biblioteka LIBFASTJSON.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfastjson.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.html
%attr(755,root,root) %{_libdir}/libfastjson.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfastjson.so.4

%files devel
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libfastjson.so
%{_includedir}/libfastjson
%{_pkgconfigdir}/libfastjson.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfastjson.a
%endif
