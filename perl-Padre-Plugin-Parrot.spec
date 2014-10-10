%define upstream_name    Padre-Plugin-Parrot
%define upstream_version 0.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Experimental Padre plugin that runs on Parrot
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Padre::Wx)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Test::More)
BuildRequires:	x11-server-xvfb

BuildArch:	noarch

%description
Experimental Padre plugin that runs on Parrot.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
#xvfb-run ./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.310.0-2mdv2011.0
+ Revision: 656954
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 623019
- new version

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.260.0-2mdv2011.0
+ Revision: 614529
- the mass rebuild of 2010.1 packages

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.1
+ Revision: 466507
- skipping tests: buildsystem fails due to missing DISPLAY, although they
  are wrapped in a xvfb-run command... and yet the perl tests do success
  nevertheless, which is strange.
- update to 0.26
- running tests in a virtual frame-buffer
- adding missing buildrequires
- import perl-Padre-Plugin-Parrot


* Tue Jan 13 2009 cpan2dist 0.16-1mdv
- initial mdv release, generated with cpan2dist

