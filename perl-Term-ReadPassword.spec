#
# Conditional build:
%bcond_with	tests		# perform "make test" (interactive)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define	pnam	ReadPassword
Summary:	Term::ReadPassword - Asking the user for a password
#Summary(pl):	
Name:		perl-Term-ReadPassword
Version:	0.01
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c720da162f62d4cbbd849406ab0b5d84
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Term::ReadLine)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module lets you ask the user for a password in the traditional way,
from the keyboard, without echoing.

# %description -l pl
# TODO

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
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
