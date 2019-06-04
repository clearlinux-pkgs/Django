#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE17DF5C82B4F9D00 (carlton@noumenal.es)
#
Name     : Django
Version  : 2.2.2
Release  : 71
URL      : https://files.pythonhosted.org/packages/56/2e/c0495314c0bdcf19d9b888a98ff16a4c58a90dd77ed741f4dbab2cbf7efe/Django-2.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/56/2e/c0495314c0bdcf19d9b888a98ff16a4c58a90dd77ed741f4dbab2cbf7efe/Django-2.2.2.tar.gz
Source99 : https://files.pythonhosted.org/packages/56/2e/c0495314c0bdcf19d9b888a98ff16a4c58a90dd77ed741f4dbab2cbf7efe/Django-2.2.2.tar.gz.asc
Summary  : A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT Python-2.0
Requires: Django-bin = %{version}-%{release}
Requires: Django-license = %{version}-%{release}
Requires: Django-python = %{version}-%{release}
Requires: Django-python3 = %{version}-%{release}
Requires: bcrypt
Requires: pytz
Requires: sqlparse
BuildRequires : Django
BuildRequires : Jinja2-python
BuildRequires : MarkupSafe
BuildRequires : MarkupSafe-python
BuildRequires : Pillow
BuildRequires : PyYAML
BuildRequires : argon2_cffi
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
The documentation in this tree is in plain text files and can be viewed using
any text file viewer.

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

%description python3
python3 components for the Django package.


%prep
%setup -q -n Django-2.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559667192
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Django
cp LICENSE %{buildroot}/usr/share/package-licenses/Django/LICENSE
cp LICENSE.python %{buildroot}/usr/share/package-licenses/Django/LICENSE.python
cp django/contrib/admin/static/admin/css/vendor/select2/LICENSE-SELECT2.md %{buildroot}/usr/share/package-licenses/Django/django_contrib_admin_static_admin_css_vendor_select2_LICENSE-SELECT2.md
cp django/contrib/admin/static/admin/fonts/LICENSE.txt %{buildroot}/usr/share/package-licenses/Django/django_contrib_admin_static_admin_fonts_LICENSE.txt
cp django/contrib/admin/static/admin/img/LICENSE %{buildroot}/usr/share/package-licenses/Django/django_contrib_admin_static_admin_img_LICENSE
cp django/contrib/admin/static/admin/js/vendor/jquery/LICENSE.txt %{buildroot}/usr/share/package-licenses/Django/django_contrib_admin_static_admin_js_vendor_jquery_LICENSE.txt
cp django/contrib/admin/static/admin/js/vendor/select2/LICENSE.md %{buildroot}/usr/share/package-licenses/Django/django_contrib_admin_static_admin_js_vendor_select2_LICENSE.md
cp django/contrib/admin/static/admin/js/vendor/xregexp/LICENSE.txt %{buildroot}/usr/share/package-licenses/Django/django_contrib_admin_static_admin_js_vendor_xregexp_LICENSE.txt
cp django/contrib/gis/gdal/LICENSE %{buildroot}/usr/share/package-licenses/Django/django_contrib_gis_gdal_LICENSE
cp django/contrib/gis/geos/LICENSE %{buildroot}/usr/share/package-licenses/Django/django_contrib_gis_geos_LICENSE
cp django/dispatch/license.txt %{buildroot}/usr/share/package-licenses/Django/django_dispatch_license.txt
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
/usr/share/package-licenses/Django/LICENSE
/usr/share/package-licenses/Django/LICENSE.python
/usr/share/package-licenses/Django/django_contrib_admin_static_admin_css_vendor_select2_LICENSE-SELECT2.md
/usr/share/package-licenses/Django/django_contrib_admin_static_admin_fonts_LICENSE.txt
/usr/share/package-licenses/Django/django_contrib_admin_static_admin_img_LICENSE
/usr/share/package-licenses/Django/django_contrib_admin_static_admin_js_vendor_jquery_LICENSE.txt
/usr/share/package-licenses/Django/django_contrib_admin_static_admin_js_vendor_select2_LICENSE.md
/usr/share/package-licenses/Django/django_contrib_admin_static_admin_js_vendor_xregexp_LICENSE.txt
/usr/share/package-licenses/Django/django_contrib_gis_gdal_LICENSE
/usr/share/package-licenses/Django/django_contrib_gis_geos_LICENSE
/usr/share/package-licenses/Django/django_dispatch_license.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
