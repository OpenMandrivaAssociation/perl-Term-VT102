%define upstream_name    Term-VT102
%define upstream_version 0.91
Name:		perl-%{upstream_name}
Version:	0.91
Release:	1

Summary:	Term::VT102 - a class to emulate a DEC VT102 terminal
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/A/AJ/AJWOOD/Term-VT102-0.91.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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


