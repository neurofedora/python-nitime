%global modname nitime

Name:           python-%{modname}
Version:        0.5
Release:        1%{?dist}
Summary:        Timeseries analysis for neuroscience data

License:        BSD
URL:            http://nipy.org/nitime
Source0:        https://github.com/nipy/nitime/archive/rel/%{version}/%{modname}-%{version}.tar.gz
Patch0:         python-nitime-0.5-unbundle-six.patch
# https://github.com/nipy/nitime/pull/134
Patch1:         0001-test_viz-import-networkx-instead-of-nx.patch
BuildRequires:  git-core

%description
Nitime contains a core of numerical algorithms for time-series analysis both in
the time and spectral domains, a set of container objects to represent
time-series, and auxiliary objects that expose a high level interface to the
numerical machinery and make common analysis tasks easy to express with compact
and semantically clear code.

%package -n     python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python-setuptools Cython
BuildRequires:  numpy
# Test deps
BuildRequires:  python-nose
BuildRequires:  numpy scipy python-matplotlib
BuildRequires:  python-networkx
Requires:       numpy scipy python-matplotlib
Requires:       python-six
Recommends:     python-networkx

%description -n python2-%{modname}
Nitime contains a core of numerical algorithms for time-series analysis both in
the time and spectral domains, a set of container objects to represent
time-series, and auxiliary objects that expose a high level interface to the
numerical machinery and make common analysis tasks easy to express with compact
and semantically clear code.

Python 2 version.

%package -n     python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools python3-Cython
BuildRequires:  python3-numpy
# Test deps
BuildRequires:  python3-nose
BuildRequires:  python3-numpy python3-scipy python3-matplotlib
BuildRequires:  python3-networkx
Requires:       python3-numpy python3-scipy python3-matplotlib
Requires:       python3-six
Recommends:     python3-networkx

%description -n python3-%{modname}
Nitime contains a core of numerical algorithms for time-series analysis both in
the time and spectral domains, a set of container objects to represent
time-series, and auxiliary objects that expose a high level interface to the
numerical machinery and make common analysis tasks easy to express with compact
and semantically clear code.

Python 3 version.

%prep
%autosetup -n %{modname}-rel-%{version} -S git
rm -vf %{modname}/six.py
sed -i -e "s/import nx/import networkx/" %{modname}/tests/test_viz.py

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests-%{python2_version} -v || :
nosetests-%{python3_version} -v || :

%files -n python2-%{modname}
%license LICENSE
%doc README.txt THANKS
%{python2_sitearch}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%doc README.txt THANKS
%{python3_sitearch}/%{modname}*

%changelog
* Fri Oct 30 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.5-1
- Initial package
