%define real_name Term-VT102

Summary:	Term::VT102 - a class to emulate a DEC VT102 terminal
Name:		perl-%{real_name}
Version:	0.82
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/Term/VT102
%dir %{perl_vendorlib}/Term/VT102/examples
%{perl_vendorlib}/Term/VT102.pm
%{perl_vendorlib}/Term/VT102/examples/*
%{_mandir}/*/*

