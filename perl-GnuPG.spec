#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	GnuPG
Summary:	GnuPG - Perl module to use GnuPG
Summary(pl):	GnuPG - Obs�uga GnuPG
Name:		perl-GnuPG
Version:	0.09
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
URL:		http://www.gnupg.org/
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Class-MethodMaker
Requires:	perl-Class-MethodMaker
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts make using HTML templates simple and natural.

%description -l pl
Niniejszy modu� jest pr�b� �atwej i naturalnej obs�ugi GnuPG.

%prep
%setup -q -n %{pdir}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:TEST_SHARED_MEMORY=1 TEST_FILE_CACHE=1 %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_sitelib}/%{pdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS MANIFEST
%{perl_sitelib}/%{pdir}/*.pm
%dir %{perl_sitelib}/%{pdir}/
%{_mandir}/man3/*
