#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Django
Version  : 1.10
Release  : 37
URL      : https://www.djangoproject.com/m/releases/1.10/Django-1.10.tar.gz
Source0  : https://www.djangoproject.com/m/releases/1.10/Django-1.10.tar.gz
Summary  : A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT Python-2.0
Requires: Django-bin
Requires: Django-python
BuildRequires : Django
BuildRequires : Jinja2-python
BuildRequires : MarkupSafe
BuildRequires : MarkupSafe-python
BuildRequires : Pillow
BuildRequires : PyYAML
BuildRequires : bcrypt
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : docutils
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-memcached
BuildRequires : python-mock
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : selenium
BuildRequires : setuptools
BuildRequires : six
BuildRequires : sqlparse
BuildRequires : tzdata
Patch1: CVE-2015-5143.nopatch
Patch2: CVE-2015-5144.nopatch
Patch3: CVE-2016-6186.nopatch

%description
The documentation in this tree is in plain text files and can be viewed using
any text file viewer.

%package bin
Summary: bin components for the Django package.
Group: Binaries

%description bin
bin components for the Django package.


%package python
Summary: python components for the Django package.
Group: Default
Provides: django-python

%description python
python components for the Django package.


%prep
%setup -q -n Django-1.10

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd tests ; PYTHONPATH=..: ./runtests.py -v 2 || : ; popd
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/django-admin
/usr/bin/django-admin.py

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
