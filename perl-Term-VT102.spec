%define upstream_name    Term-VT102
%define upstream_version 0.91

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Term::VT102 - a class to emulate a DEC VT102 terminal
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The VT102 class provides emulation of most of the functions of a
DEC VT102 terminal. Once initialised, data passed to a VT102
object is processed and the in-memory screen modified accordingly.
This screen can be interrogated by the external program in a
variety of ways.

This allows your program to interface with full-screen console
programs by running them in a subprocess and passing their output
to a VT102 class. You can then see what the application has
written on the screen by querying the class appropriately.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/Term/VT102
%dir %{perl_vendorlib}/Term/VT102/examples
%{perl_vendorlib}/Term/VT102.pm
%{perl_vendorlib}/Term/VT102/examples/*
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.910.0-1mdv2010.0
+ Revision: 405544
- rebuild using %%perl_convert_version

* Mon Nov 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-1mdv2009.1
+ Revision: 301686
- update to new version 0.91

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.82-6mdv2009.0
+ Revision: 241964
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.82-4mdv2008.0
+ Revision: 25460
- rebuild

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.82-3mdv2008.0
+ Revision: 23809
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.82-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.82-1mdk
- initial Mandriva package

