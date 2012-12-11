%define upstream_name    Crypt-RC5
%define upstream_version 2.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Crypt-RC5 module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module is a perl implementation of the RC5 encryption algorithm.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Crypt/RC5.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.0.0-6mdv2011.0
+ Revision: 680866
- mass rebuild

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 2.0.0-5mdv2011.0
+ Revision: 505682
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.00-4mdv2010.0
+ Revision: 430377
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.00-3mdv2009.0
+ Revision: 256338
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.00-1mdv2008.1
+ Revision: 136699
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 2.00-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.00-1mdk
- initial Mandriva package

