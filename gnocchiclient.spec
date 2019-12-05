#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnocchiclient
Version  : 7.0.5
Release  : 17
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
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
=============
gnocchiclient
=============
.. image:: https://travis-ci.org/gnocchixyz/python-gnocchiclient.png?branch=master
:target: https://travis-ci.org/gnocchixyz/python-gnocchiclient
:alt: Build Status

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

%description python3
python3 components for the gnocchiclient package.


%prep
%setup -q -n gnocchiclient-7.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552140833
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnocchiclient
cp LICENSE %{buildroot}/usr/share/package-licenses/gnocchiclient/LICENSE
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
/usr/share/package-licenses/gnocchiclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
