#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	GnuPG
Summary:	GnuPG - Perl module interface to the GNU Privacy Guard
Summary(pl):	GnuPG - modu³ interfejsu perlowego do GPG (GNU Privacy Guard)
Name:		perl-GnuPG
Version:	0.09
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
Patch0:		perl-GnuPG.pld.patch
URL:		http://www.gnupg.org/
BuildRequires:	gnupg
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG is a Perl interface to the GNU Privacy Guard. It uses the shared
memory coprocess interface that gpg provides for its wrappers. It
tries its best to map the interactive interface of the gpg to a more
programmatic model.

%description -l pl
GnuPG to interfejs Perla do GPG (GNU Privacy Guard). U¿ywa interfejsu
pamiêci dzielonej, udostêpnianego przez gpg. Próbuje jak najlepiej
odwzorowaæ interaktywny interfejs gpg do bardziej programistycznego
modelu.

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
%{perl_sitelib}/%{pdir}/Tie*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
