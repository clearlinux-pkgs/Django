#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Django
Version  : 2.1.4
Release  : 67
URL      : https://files.pythonhosted.org/packages/83/f7/4939b60c4127d5f49ccb570e34f4c59ecc222949220234a88e4f363f1456/Django-2.1.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/83/f7/4939b60c4127d5f49ccb570e34f4c59ecc222949220234a88e4f363f1456/Django-2.1.4.tar.gz
Summary  : A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT Python-2.0
Requires: Django-bin = %{version}-%{release}
Requires: Django-license = %{version}-%{release}
Requires: Django-python = %{version}-%{release}
Requires: Django-python3 = %{version}-%{release}
Requires: bcrypt
Requires: pytz
BuildRequires : Django
BuildRequires : Jinja2-python
BuildRequires : MarkupSafe
BuildRequires : MarkupSafe-python
BuildRequires : Pillow
BuildRequires : PyYAML
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
Patch1: CVE-2019-3498.patch
Patch2: CVE-2019-6975.patch

%description
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

%description python3
python3 components for the Django package.


%prep
%setup -q -n Django-2.1.4
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550011160
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd tests ; PYTHONPATH=..: ./runtests.py -v 2 || : ; popd
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
