#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	GnuPG
Summary:	GnuPG - Perl module to use GnuPG
Summary(pl):	GnuPG - Obs³uga GnuPG
Name:		perl-GnuPG
Version:	0.09
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
Patch0:		perl-GnuPG.pld.patch
URL:		http://www.gnupg.org/
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts make using GnuPG simple and natural.

%description -l pl
Niniejszy modu³ jest prób± ³atwej i naturalnej obs³ugi GnuPG.

%prep
%setup -q -n %{pdir}-%{version}
%patch0

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
%doc README NEWS
%{perl_sitelib}/*.pm
%dir %{perl_sitelib}/%{pdir}/*
%dir %{perl_sitelib}/%{pdir}/Tie/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
