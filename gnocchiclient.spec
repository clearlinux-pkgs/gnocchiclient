#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnocchiclient
Version  : 2.2.0
Release  : 8
URL      : http://tarballs.openstack.org/python-gnocchiclient/gnocchiclient-2.2.0.tar.gz
Source0  : http://tarballs.openstack.org/python-gnocchiclient/gnocchiclient-2.2.0.tar.gz
Summary  : Python client library for Gnocchi
Group    : Development/Tools
License  : Apache-2.0
Requires: gnocchiclient-bin
Requires: gnocchiclient-python
BuildRequires : PyYAML-python
BuildRequires : Sphinx-python
BuildRequires : cliff-python
BuildRequires : cmd2-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : futurist-python
BuildRequires : gnocchi-python
BuildRequires : keystoneauth1-python
BuildRequires : keystonemiddleware
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyparsing-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : sphinx-bootstrap-theme-python
BuildRequires : tempest-lib-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
=============
gnocchiclient
=============
Python bindings to the OpenStack Gnocchi API

%package bin
Summary: bin components for the gnocchiclient package.
Group: Binaries

%description bin
bin components for the gnocchiclient package.


%package python
Summary: python components for the gnocchiclient package.
Group: Default
Requires: cliff-python
Requires: futurist-python
Requires: keystoneauth1-python
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: tempest-lib-python

%description python
python components for the gnocchiclient package.


%prep
%setup -q -n gnocchiclient-2.2.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnocchi

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
