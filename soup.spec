%define		mver		0.7
%define		subver		4

Summary:	SOAP (Simple Object Access Protocol) implementation in C
Summary(pl):	Implementacja w C SOAP (Simple Object Access Protocol)
Name:		soup
Version:	%{mver}.%{subver}
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/mirror/gnome.org/sources/%{name}/%{mver}/%{name}-%{version}.tar.bz2
# Source0-md5:	848ccf5e7616cd897593bab72bbc9b5a
Patch0:		%{name}-make.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It provides an queued asynchronous callback-based mechanism for
sending and servicing SOAP requests, and a WSDL (Web Service
Definition Language) to C compiler which generates client stubs and
server skeletons for easily calling and implementing SOAP methods.

%description -l pl
Pakiet dostarcza interfejs kolejkowalnego, asynchronicznego mechanizmu
do wysy³ania i serwowania ¿±dañ SOAP oraz WSDL (Web Service Definition
Language) dla kompilatora C, który generuje klienckie stub i szkielety
serwerów dla ³atwego wywo³ywania i implementowania metod SOAP.

%package devel
Summary:	Include files etc to develop SOAP applications
Summary(pl):	Pliki nag³ówkowe, dokumentacja dla SOAP
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk-doc-common

%description devel
Header files, etc you can use to develop SOAP applications.

%description devel -l pl
Pliki nag³ówkowe itp., jednym s³owem wszystko czego potrzeba, aby
samemu tworzyæ aplikacje korzystaj±ce z SOAP.

%package static
Summary:	SOAP static libraries
Summary(pl):	Biblioteki statyczne SOAP
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
SOAP static libraries.

%description static -l pl
Biblioteki statyczne SOAP.

%prep
%setup -q
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--with-html-dir=%{_gtkdocdir} \
	--enable-ssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pkgconfigdir=%{_pkgconfigdir} \
	m4datadir=%{_aclocaldir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/soup-ssl-proxy
%attr(755,root,root) %{_bindir}/soup-httpd
%attr(755,root,root) %{_bindir}/soup-wsdl
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*
%{_gtkdocdir}/*
%{_pkgconfigdir}/*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
