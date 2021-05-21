#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Font-AFM
Version  : 1.20
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/G/GA/GAAS/Font-AFM-1.20.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GAAS/Font-AFM-1.20.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfont-afm-perl/libfont-afm-perl_1.20-2.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Font-AFM-license = %{version}-%{release}
Requires: perl-Font-AFM-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Font::AFM - Interface to Adobe Font Metrics files
SYNOPSIS
use Font::AFM;
$h = new Font::AFM "Helvetica";
$copyright = $h->Notice;
$w = $h->Wx->{"aring"};
$w = $h->stringwidth("Gisle", 10);
$h->dump;  # for debugging

%package dev
Summary: dev components for the perl-Font-AFM package.
Group: Development
Provides: perl-Font-AFM-devel = %{version}-%{release}
Requires: perl-Font-AFM = %{version}-%{release}

%description dev
dev components for the perl-Font-AFM package.


%package license
Summary: license components for the perl-Font-AFM package.
Group: Default

%description license
license components for the perl-Font-AFM package.


%package perl
Summary: perl components for the perl-Font-AFM package.
Group: Default
Requires: perl-Font-AFM = %{version}-%{release}

%description perl
perl components for the perl-Font-AFM package.


%prep
%setup -q -n Font-AFM-1.20
cd %{_builddir}
tar xf %{_sourcedir}/libfont-afm-perl_1.20-2.debian.tar.xz
cd %{_builddir}/Font-AFM-1.20
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Font-AFM-1.20/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Font-AFM
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Font-AFM/8d0370206d541d05ace71cebad0e36ae764c709e
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Font::AFM.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Font-AFM/8d0370206d541d05ace71cebad0e36ae764c709e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Font/AFM.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/Courier.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/CourierBold.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/CourierBoldOblique.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/CourierOblique.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/Helvetica.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/HelveticaBold.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/HelveticaBoldOblique.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/HelveticaOblique.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/TimesBold.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/TimesBoldItalic.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/TimesItalic.pm
/usr/lib/perl5/vendor_perl/5.34.0/Font/Metrics/TimesRoman.pm
