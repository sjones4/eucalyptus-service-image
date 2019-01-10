Name:           eucalyptus-service-image
Version:        5.0.100
Release:        0%{?dist}
Summary:        Eucalyptus Service Image

Group:          Applications/System
# License needs to be the *distro's* license (Fedora is GPLv2, for instance)
License:        GPLv2
URL:            https://eucalyptus.cloud/
BuildArch:      noarch

Source0:        %{name}-%{version}.tar.xz

BuildRequires:  /usr/bin/virt-install
BuildRequires:  /usr/bin/virt-sparsify
BuildRequires:  /usr/bin/virt-sysprep
BuildRequires:  python-devel

Requires:       %{name}-tools = %{version}-%{release}

Obsoletes:      eucalyptus-imaging-worker-image < 1.1
Obsoletes:      eucalyptus-load-balancer-image < 1.2
Provides:       eucalyptus-imaging-worker-image
Provides:       eucalyptus-load-balancer-image

# Use fast compression (image already compressed)
%global _binary_payload w1.gzdio

%description
This package contains a machine image for use in Eucalyptus to
instantiate multiple internal services.

%package tools
Summary:      Eucalyptus Service Image Tools

BuildRequires:  python-devel

Requires:       euca2ools >= 3.3
Requires:       eucalyptus-admin-tools >= 4.2
Requires:       python-prettytable
Requires:       tar
Requires:       xz

%description tools
This package contains tools for management of machine images used by
Eucalyptus to instantiate multiple internal services.

%prep
%setup -q


%build
%configure %{?configure_opts}
make


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc IMAGE-LICENSE
# Something else should probably own the service-images dir at some
# point, but we can deal with that later when we have more than one.
/usr/share/eucalyptus/service-images/%{name}-%{version}.tar.xz


%files tools
%defattr(-,root,root,-)
/usr/bin/esi-describe-images
/usr/bin/esi-install-image
/usr/bin/esi-manage-stack
%{python_sitelib}/esitoolsupport*


%changelog
* Fri Jan  4 2019 Steve Jones <steve.jones@appscale.com> - 5.0
- Separate rpm for esi tools

* Wed Nov 14 2018 Steve Jones <steve.jones@appscale.com>
- Add dependencies for tar and xz used for default image install

* Wed Jul 25 2018 Steve Jones <steve.jones@appscale.com> - 5.0
- Version bump (5.0)

* Wed Mar 14 2018 Steve Jones <steve.jones@appscale.com> - 4.4
- Version bump (4.4), now versioned as per eucalyptus

* Tue Nov  8 2016 Garrett Holmstrom <gholms@hpe.com> - 3
- Version bump (3)

* Mon Jul 25 2016 Garrett Holmstrom <gholms@hpe.com> - 2
- Version bump (2)

* Wed Feb 17 2016 Eucalyptus Release Engineering <support@eucalyptus.com>
- remove python 2.7 requirement

* Fri Feb  5 2016 Eucalyptus Release Engineering <support@eucalyptus.com>
- build Centos 7 image; sunset database server

* Mon Sep 28 2015 Eucalyptus Release Engineering <support@eucalyptus.com>
- Pulled in euca2ools 3.3 for euca-generate-environment-config

* Wed Aug 26 2015 Eucalyptus Release Engineering <support@eucalyptus.com>
- Use make instead of custom scripts

* Fri Apr 24 2015 Eucalyptus Release Engineering <support@eucalyptus.com>
- Use esi prefix for tools

* Fri Dec 05 2014 Eucalyptus Release Engineering <support@eucalyptus.com>
- Created
