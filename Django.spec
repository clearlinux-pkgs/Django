#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE17DF5C82B4F9D00 (carlton@noumenal.es)
#
Name     : Django
Version  : 3.2.4
Release  : 104
URL      : https://files.pythonhosted.org/packages/27/94/123b3a95e9965819a3d30d36da6fc12ddff83bcfb0099f3e15437347480a/Django-3.2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/27/94/123b3a95e9965819a3d30d36da6fc12ddff83bcfb0099f3e15437347480a/Django-3.2.4.tar.gz
Source1  : https://files.pythonhosted.org/packages/27/94/123b3a95e9965819a3d30d36da6fc12ddff83bcfb0099f3e15437347480a/Django-3.2.4.tar.gz.asc
Summary  : A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause CC-BY-4.0 MIT OFL-1.1
Requires: Django-bin = %{version}-%{release}
Requires: Django-license = %{version}-%{release}
Requires: Django-python = %{version}-%{release}
Requires: Django-python3 = %{version}-%{release}
Requires: argon2-cffi
Requires: asgiref
Requires: bcrypt
Requires: pytz
Requires: sqlparse
BuildRequires : Jinja2-python
BuildRequires : MarkupSafe
BuildRequires : MarkupSafe-python
BuildRequires : Pillow
BuildRequires : PyYAML
BuildRequires : argon2-cffi
BuildRequires : asgiref
BuildRequires : bcrypt
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : docutils
BuildRequires : numpy
BuildRequires : py
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pytest
BuildRequires : python-memcached
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : pytz
BuildRequires : selenium
BuildRequires : six
BuildRequires : sqlparse
BuildRequires : tzdata

%description
Django
        ======
        
        Django is a high-level Python Web framework that encourages rapid development
        and clean, pragmatic design. Thanks for checking it out.
        
        All documentation is in the "``docs``" directory and online at

%package bin
Summary: bin components for the Django package.
Group: Binaries
Requires: Django-license = %{version}-%{release}

%description bin
bin components for the Django package.


%package license
Summary: license components for the Django package.
Group: Default

%description license
license components for the Django package.


%package python
Summary: python components for the Django package.
Group: Default
Requires: Django-python3 = %{version}-%{release}
Provides: django-python

%description python
python components for the Django package.


%package python3
Summary: python3 components for the Django package.
Group: Default
Requires: python3-core
Provides: pypi(django)
Requires: pypi(asgiref)
Requires: pypi(pytz)
Requires: pypi(sqlparse)

%description python3
python3 components for the Django package.


%prep
%setup -q -n Django-3.2.4
cd %{_builddir}/Django-3.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622654340
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Django
cp %{_builddir}/Django-3.2.4/LICENSE %{buildroot}/usr/share/package-licenses/Django/baf11129ce63c4eef654f39a360b31cfc7d1ac67
cp %{_builddir}/Django-3.2.4/django/contrib/admin/static/admin/css/vendor/select2/LICENSE-SELECT2.md %{buildroot}/usr/share/package-licenses/Django/016d84ac0cab22a77e44e7182bb1691d97449696
cp %{_builddir}/Django-3.2.4/django/contrib/admin/static/admin/fonts/LICENSE.txt %{buildroot}/usr/share/package-licenses/Django/47b573e3824cd5e02a1a3ae99e2735b49e0256e4
cp %{_builddir}/Django-3.2.4/django/contrib/admin/static/admin/img/LICENSE %{buildroot}/usr/share/package-licenses/Django/25180b3c1e27c6d700e4e037e53b970fe36b1f3e
cp %{_builddir}/Django-3.2.4/django/contrib/admin/static/admin/js/vendor/jquery/LICENSE.txt %{buildroot}/usr/share/package-licenses/Django/fcf3a2474ae0d8e6ce39e4bc915915e4b4bd32b8
cp %{_builddir}/Django-3.2.4/django/contrib/admin/static/admin/js/vendor/select2/LICENSE.md %{buildroot}/usr/share/package-licenses/Django/016d84ac0cab22a77e44e7182bb1691d97449696
cp %{_builddir}/Django-3.2.4/django/contrib/admin/static/admin/js/vendor/xregexp/LICENSE.txt %{buildroot}/usr/share/package-licenses/Django/49374697c5dbcdfc34349dc1c8566c0bc4759d1f
cp %{_builddir}/Django-3.2.4/django/contrib/gis/gdal/LICENSE %{buildroot}/usr/share/package-licenses/Django/f0fda12a002635b7014205a973222bbc34df78de
cp %{_builddir}/Django-3.2.4/django/contrib/gis/geos/LICENSE %{buildroot}/usr/share/package-licenses/Django/3f9aeadb484dd83ead5656f1bc870e7685607bee
cp %{_builddir}/Django-3.2.4/django/dispatch/license.txt %{buildroot}/usr/share/package-licenses/Django/a1f11ae702923c95226800ca5172b00b3f975386
cp %{_builddir}/Django-3.2.4/docs/_theme/djangodocs/static/fontawesome/LICENSE.txt %{buildroot}/usr/share/package-licenses/Django/c48a7d100730cfd1b71d3830179dbf40fdd9c3c2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/django-admin
/usr/bin/django-admin.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Django/016d84ac0cab22a77e44e7182bb1691d97449696
/usr/share/package-licenses/Django/25180b3c1e27c6d700e4e037e53b970fe36b1f3e
/usr/share/package-licenses/Django/3f9aeadb484dd83ead5656f1bc870e7685607bee
/usr/share/package-licenses/Django/47b573e3824cd5e02a1a3ae99e2735b49e0256e4
/usr/share/package-licenses/Django/49374697c5dbcdfc34349dc1c8566c0bc4759d1f
/usr/share/package-licenses/Django/a1f11ae702923c95226800ca5172b00b3f975386
/usr/share/package-licenses/Django/baf11129ce63c4eef654f39a360b31cfc7d1ac67
/usr/share/package-licenses/Django/c48a7d100730cfd1b71d3830179dbf40fdd9c3c2
/usr/share/package-licenses/Django/f0fda12a002635b7014205a973222bbc34df78de
/usr/share/package-licenses/Django/fcf3a2474ae0d8e6ce39e4bc915915e4b4bd32b8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
