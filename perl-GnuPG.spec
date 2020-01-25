#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	GnuPG
Summary:	GnuPG - Perl module interface to the GNU Privacy Guard
Summary(pl.UTF-8):	GnuPG - moduł interfejsu perlowego do GPG (GNU Privacy Guard)
Name:		perl-GnuPG
Version:	0.18
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	86f1a79389a0bede2db6bd758b464b8b
URL:		http://www.gnupg.org/
BuildRequires:	gnupg
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG is a Perl interface to the GNU Privacy Guard. It uses the shared
memory coprocess interface that gpg provides for its wrappers. It
tries its best to map the interactive interface of the gpg to a more
programmatic model.

%description -l pl.UTF-8
GnuPG to interfejs Perla do GPG (GNU Privacy Guard). Używa interfejsu
pamięci dzielonej, udostępnianego przez gpg. Próbuje jak najlepiej
odwzorować interaktywny interfejs gpg do bardziej programistycznego
modelu.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:TEST_SHARED_MEMORY=1 TEST_FILE_CACHE=1 %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/%{pdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/%{pdir}/Tie*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
