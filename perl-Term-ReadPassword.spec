#
# Conditional build:
%bcond_with	tests		# perform "make test" (interactive)
#
%define		pdir	Term
%define		pnam	ReadPassword
Summary:	Term::ReadPassword - asking the user for a password
Summary(pl.UTF-8):	Term::ReadPassowrd - pytanie użytkownika o hasło
Name:		perl-Term-ReadPassword
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e4e611f2a1efcf99c2b0c0488dd615e6
URL:		http://search.cpan.org/dist/Term-ReadPassword/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Term::ReadLine)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module lets you ask the user for a password in the traditional
way, from the keyboard, without echoing.

%description -l pl.UTF-8
Ten moduł pozwala zapytać użytkownika o hasło w tradycyjny sposób - z
klawiatury, bez echa.

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
%doc Changes
%{perl_vendorlib}/Term/*.pm
%{_mandir}/man3/*
