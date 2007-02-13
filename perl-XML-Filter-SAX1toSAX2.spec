#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-SAX1toSAX2
Summary:	XML::Filter::SAX1toSAX2 - convert SAX1 events to SAX2
Summary(pl.UTF-8):	XML::Filter::SAX1toSAX2 - konwersja zdarzeń SAX1 do SAX2
Name:		perl-XML-Filter-SAX1toSAX2
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7189c56d9f9c23f92f6a66808423afd2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-libxml
BuildRequires:	perl-XML-Handler-YAWriter
BuildRequires:	perl-XML-NamespaceSupport
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-SAX-Writer
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a very simple module for creating SAX2 events from SAX1
events. It is useful in the case where you have a SAX1 parser but want
to use a SAX2 handler or filter of some sort.

%description -l pl.UTF-8
Ten moduł jest bardzo prostym modułem do tworzenia zdarzeń SAX2 ze
zdarzeń SAX1. Jest przydatny w przypadku kiedy mamy parser SAX1, ale
chcemy używać jakiejś procedury obsługi czy filtra SAX2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/XML/*/*.pm
%{_mandir}/man3/*
