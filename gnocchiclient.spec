#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnocchiclient
Version  : 7.0.5
Release  : 19
URL      : https://files.pythonhosted.org/packages/9d/c8/1a254fb7128ed90d5b8f29d1f06fe18319d6c9ce83068379020394c52e98/gnocchiclient-7.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/c8/1a254fb7128ed90d5b8f29d1f06fe18319d6c9ce83068379020394c52e98/gnocchiclient-7.0.5.tar.gz
Summary  : Python client library for Gnocchi
Group    : Development/Tools
License  : Apache-2.0
Requires: gnocchiclient-bin = %{version}-%{release}
Requires: gnocchiclient-license = %{version}-%{release}
Requires: gnocchiclient-python = %{version}-%{release}
Requires: gnocchiclient-python3 = %{version}-%{release}
Requires: cliff
Requires: debtcollector
Requires: futurist
Requires: iso8601
Requires: keystoneauth1
Requires: monotonic
Requires: pbr
Requires: python-dateutil
Requires: six
Requires: ujson
BuildRequires : buildreq-distutils3
BuildRequires : cliff
BuildRequires : debtcollector
BuildRequires : futurist
BuildRequires : iso8601
BuildRequires : keystoneauth1
BuildRequires : monotonic
BuildRequires : pbr
BuildRequires : python-dateutil
BuildRequires : six
BuildRequires : ujson

%description
=============
gnocchiclient
=============

.. image:: https://travis-ci.org/gnocchixyz/python-gnocchiclient.png?branch=master
    :target: https://travis-ci.org/gnocchixyz/python-gnocchiclient
    :alt: Build Status

.. image:: https://badge.fury.io/py/gnocchiclient.svg
    :target: https://badge.fury.io/py/gnocchiclient

Python bindings to the Gnocchi API

This is a client for Gnocchi API. There's :doc:`a Python API <api>` (the
:mod:`gnocchiclient` module), and a :doc:`command-line script <shell>`
(installed as :program:`gnocchi`). Each implements the entire Gnocchi API.

* Free software: Apache license
* Documentation: http://gnocchi.xyz/gnocchiclient
* Source: https://github.com/gnocchixyz/python-gnocchiclient
* Bugs: https://github.com/gnocchixyz/python-gnocchiclient/issues

%package bin
Summary: bin components for the gnocchiclient package.
Group: Binaries
Requires: gnocchiclient-license = %{version}-%{release}

%description bin
bin components for the gnocchiclient package.


%package license
Summary: license components for the gnocchiclient package.
Group: Default

%description license
license components for the gnocchiclient package.


%package python
Summary: python components for the gnocchiclient package.
Group: Default
Requires: gnocchiclient-python3 = %{version}-%{release}

%description python
python components for the gnocchiclient package.


%package python3
Summary: python3 components for the gnocchiclient package.
Group: Default
Requires: python3-core
Provides: pypi(gnocchiclient)

%description python3
python3 components for the gnocchiclient package.


%prep
%setup -q -n gnocchiclient-7.0.5
cd %{_builddir}/gnocchiclient-7.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582930946
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnocchiclient
cp %{_builddir}/gnocchiclient-7.0.5/LICENSE %{buildroot}/usr/share/package-licenses/gnocchiclient/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnocchi

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnocchiclient/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
