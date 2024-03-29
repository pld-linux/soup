Summary:	SOAP (Simple Object Access Protocol) implementation in C
Summary(pl.UTF-8):	Implementacja w C SOAP (Simple Object Access Protocol)
Name:		soup
Version:	0.7.11
Release:	1
License:	LGPL v2+ (libsoup), GPL v2+ (utilities)
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/soup/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	61bb2fef816ce164af62f8a3a5bd782e
Patch0:		%{name}-make.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It provides an queued asynchronous callback-based mechanism for
sending and servicing SOAP requests, and a WSDL (Web Service
Definition Language) to C compiler which generates client stubs and
server skeletons for easily calling and implementing SOAP methods.

%description -l pl.UTF-8
Pakiet dostarcza interfejs kolejkowalnego, asynchronicznego mechanizmu
do wysyłania i serwowania żądań SOAP oraz WSDL (Web Service Definition
Language) dla kompilatora C, który generuje klienckie stub i szkielety
serwerów dla łatwego wywoływania i implementowania metod SOAP.

%package devel
Summary:	Include files etc to develop SOAP applications
Summary(pl.UTF-8):	Pliki nagłówkowe, dokumentacja dla SOAP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-doc-common

%description devel
Header files, etc you can use to develop SOAP applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe itp., jednym słowem wszystko czego potrzeba, aby
samemu tworzyć aplikacje korzystające z SOAP.

%package static
Summary:	SOAP static libraries
Summary(pl.UTF-8):	Biblioteki statyczne SOAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
SOAP static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne SOAP.

%prep
%setup -q
%patch0 -p1

%build
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

%post	-p /sbin/ldconfig
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
