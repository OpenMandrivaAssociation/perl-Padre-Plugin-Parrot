%define upstream_name    Padre-Plugin-Parrot
%define upstream_version 0.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Experimental Padre plugin that runs on Parrot
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Padre::Wx)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Test::More)
BuildRequires: x11-server-xvfb

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#xvfb-run %make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
