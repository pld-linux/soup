Summary:	SOAP (Simple Object Access Protocol) implementation in C
Summary(pl):	Implementacja w C SOAP (Simple Object Access Protocol)
Name:		soup
Version:	0.2
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	glib-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

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
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files, etc you can use to develop SOAP applications.

%description -l pl devel
Pliki nag³ówkowe itp. Jednym s³owem wszystko czego potrzebujesz aby
samemu tworzyæ sobie aplikacje korzystaj±ce z SOAP.

%package static
Summary:	%{name} static libraries
Summary(pl):	Biblioteki statyczne %{name}
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
%{name} static libraries.

%description -l pl static
Biblioteki statyczne %{name}.

%prep
%setup  -q -n %{name}-%{version}.1

%build
rm missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c

CPPFLAGS="%{rpmcflags} -I%{_prefix}"; export CPPFLAGS
%configure \
	--enable-ssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz

%dir %{_sysconfdir}
%dir %{_sysconfdir}/sound
%dir %{_sysconfdir}/sound/events
%config %{_sysconfdir}/mime-magic*
%config %{_sysconfdir}/paper.config
%config %{_sysconfdir}/sound/events/gnome.soundlist
%config %{_sysconfdir}/sound/events/gtk-events.soundlist

%attr(755,root,root) %{_libdir}/lib*.so.*.*


%files devel
%defattr(644,root,root,755)
%doc devel-docs/{README.gtkcauldron*,*.txt.gz,*.sgml,*/{*.txt.gz,*.sgml}}

%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh

%{_includedir}/*
%{_libdir}/gnome-libs
%{_datadir}/doc

%{_mandir}/man1/gnome-config.1*
%{_mandir}/man3/*

%{_datadir}/idl/*
%{_aclocaldir}/*.m4
%dir %{_aclocaldir}/gnome
%{_aclocaldir}/gnome/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
