#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAFFE75DDE8508E12 (pbrezina@redhat.com)
#
Name     : sssd
Version  : 2.4.1
Release  : 29
URL      : https://github.com/SSSD/sssd/releases/download/2.4.1/sssd-2.4.1.tar.gz
Source0  : https://github.com/SSSD/sssd/releases/download/2.4.1/sssd-2.4.1.tar.gz
Source1  : https://github.com/SSSD/sssd/releases/download/2.4.1/sssd-2.4.1.tar.gz.asc
Summary  : SSSD implementation of Samba wbclient API
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: sssd-bin = %{version}-%{release}
Requires: sssd-data = %{version}-%{release}
Requires: sssd-lib = %{version}-%{release}
Requires: sssd-libexec = %{version}-%{release}
Requires: sssd-license = %{version}-%{release}
Requires: sssd-locales = %{version}-%{release}
Requires: sssd-python = %{version}-%{release}
Requires: sssd-python3 = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : bind-utils
BuildRequires : buildreq-distutils3
BuildRequires : c-ares-dev
BuildRequires : cyrus-sasl-dev
BuildRequires : ding-libs-dev
BuildRequires : e2fsprogs-dev
BuildRequires : gdm-dev
BuildRequires : jansson-dev
BuildRequires : keyutils-dev
BuildRequires : krb5-dev
BuildRequires : ldb-dev
BuildRequires : libnl-dev
BuildRequires : nfs-utils-dev
BuildRequires : openldap-dev
BuildRequires : pcre-dev
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(p11-kit-1)
BuildRequires : popt-dev
BuildRequires : python3-dev
BuildRequires : samba-dev
BuildRequires : tdb-dev
BuildRequires : tevent-dev
BuildRequires : valgrind

%description
Continuous integration
======================
The executables and modules in this directory implement continuous integration
(CI) tests, which can be run to verify SSSD code quality and validity.

%package bin
Summary: bin components for the sssd package.
Group: Binaries
Requires: sssd-data = %{version}-%{release}
Requires: sssd-libexec = %{version}-%{release}
Requires: sssd-license = %{version}-%{release}

%description bin
bin components for the sssd package.


%package data
Summary: data components for the sssd package.
Group: Data

%description data
data components for the sssd package.


%package dev
Summary: dev components for the sssd package.
Group: Development
Requires: sssd-lib = %{version}-%{release}
Requires: sssd-bin = %{version}-%{release}
Requires: sssd-data = %{version}-%{release}
Provides: sssd-devel = %{version}-%{release}
Requires: sssd = %{version}-%{release}

%description dev
dev components for the sssd package.


%package lib
Summary: lib components for the sssd package.
Group: Libraries
Requires: sssd-data = %{version}-%{release}
Requires: sssd-libexec = %{version}-%{release}
Requires: sssd-license = %{version}-%{release}

%description lib
lib components for the sssd package.


%package libexec
Summary: libexec components for the sssd package.
Group: Default
Requires: sssd-license = %{version}-%{release}

%description libexec
libexec components for the sssd package.


%package license
Summary: license components for the sssd package.
Group: Default

%description license
license components for the sssd package.


%package locales
Summary: locales components for the sssd package.
Group: Default

%description locales
locales components for the sssd package.


%package python
Summary: python components for the sssd package.
Group: Default
Requires: sssd-python3 = %{version}-%{release}

%description python
python components for the sssd package.


%package python3
Summary: python3 components for the sssd package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sssd package.


%prep
%setup -q -n sssd-2.4.1
cd %{_builddir}/sssd-2.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612854157
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --disable-cifs-idmap-plugin \
--with-samba \
--without-libwbclient \
--without-manpages \
--without-python2-bindings \
--without-selinux \
--without-semanage
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1612854157
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sssd
cp %{_builddir}/sssd-2.4.1/COPYING %{buildroot}/usr/share/package-licenses/sssd/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/sssd-2.4.1/src/sss_client/COPYING %{buildroot}/usr/share/package-licenses/sssd/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/sssd-2.4.1/src/sss_client/COPYING.LESSER %{buildroot}/usr/share/package-licenses/sssd/978773e74b4cfcbe611ae1217754f259ad37ac96
%make_install
%find_lang sssd

%files
%defattr(-,root,root,-)
/usr/lib64/sssd/conf/sssd.conf

%files bin
%defattr(-,root,root,-)
/usr/bin/sss_cache
/usr/bin/sss_debuglevel
/usr/bin/sss_obfuscate
/usr/bin/sss_override
/usr/bin/sss_seed
/usr/bin/sss_ssh_authorizedkeys
/usr/bin/sss_ssh_knownhostsproxy
/usr/bin/sssctl
/usr/bin/sssd

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.freedesktop.sssd.infopipe.service
/usr/share/dbus-1/system.d/org.freedesktop.sssd.infopipe.conf
/usr/share/sssd-kcm/kcm_default_ccache
/usr/share/sssd/cfg_rules.ini
/usr/share/sssd/sssd.api.conf
/usr/share/sssd/sssd.api.d/sssd-ad.conf
/usr/share/sssd/sssd.api.d/sssd-files.conf
/usr/share/sssd/sssd.api.d/sssd-ipa.conf
/usr/share/sssd/sssd.api.d/sssd-krb5.conf
/usr/share/sssd/sssd.api.d/sssd-ldap.conf
/usr/share/sssd/sssd.api.d/sssd-local.conf
/usr/share/sssd/sssd.api.d/sssd-proxy.conf
/usr/share/sssd/sssd.api.d/sssd-simple.conf

%files dev
%defattr(-,root,root,-)
/usr/include/ipa_hbac.h
/usr/include/sss_certmap.h
/usr/include/sss_idmap.h
/usr/include/sss_nss_idmap.h
/usr/include/sss_sifp.h
/usr/include/sss_sifp_dbus.h
/usr/lib64/libipa_hbac.so
/usr/lib64/libsss_certmap.so
/usr/lib64/libsss_idmap.so
/usr/lib64/libsss_nss_idmap.so
/usr/lib64/libsss_simpleifp.so
/usr/lib64/libsss_sudo.so
/usr/lib64/pkgconfig/ipa_hbac.pc
/usr/lib64/pkgconfig/sss_certmap.pc
/usr/lib64/pkgconfig/sss_idmap.pc
/usr/lib64/pkgconfig/sss_nss_idmap.pc
/usr/lib64/pkgconfig/sss_simpleifp.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/krb5/plugins/authdata/sssd_pac_plugin.so
/usr/lib64/krb5/plugins/libkrb5/sssd_krb5_locator_plugin.so
/usr/lib64/ldb/modules/ldb/memberof.so
/usr/lib64/libipa_hbac.so.0
/usr/lib64/libipa_hbac.so.0.1.0
/usr/lib64/libnfsidmap/sss.so
/usr/lib64/libnss_sss.so.2
/usr/lib64/libsss_certmap.so.0
/usr/lib64/libsss_certmap.so.0.2.0
/usr/lib64/libsss_idmap.so.0
/usr/lib64/libsss_idmap.so.0.5.1
/usr/lib64/libsss_nss_idmap.so.0
/usr/lib64/libsss_nss_idmap.so.0.5.0
/usr/lib64/libsss_simpleifp.so.0
/usr/lib64/libsss_simpleifp.so.0.1.1
/usr/lib64/samba/idmap/sss.so
/usr/lib64/security/pam_sss.so
/usr/lib64/security/pam_sss_gss.so
/usr/lib64/sssd/libifp_iface.so
/usr/lib64/sssd/libifp_iface_sync.so
/usr/lib64/sssd/libsss_ad.so
/usr/lib64/sssd/libsss_cert.so
/usr/lib64/sssd/libsss_child.so
/usr/lib64/sssd/libsss_crypt.so
/usr/lib64/sssd/libsss_debug.so
/usr/lib64/sssd/libsss_files.so
/usr/lib64/sssd/libsss_iface.so
/usr/lib64/sssd/libsss_iface_sync.so
/usr/lib64/sssd/libsss_ipa.so
/usr/lib64/sssd/libsss_krb5.so
/usr/lib64/sssd/libsss_krb5_common.so
/usr/lib64/sssd/libsss_ldap.so
/usr/lib64/sssd/libsss_ldap_common.so
/usr/lib64/sssd/libsss_proxy.so
/usr/lib64/sssd/libsss_sbus.so
/usr/lib64/sssd/libsss_sbus_sync.so
/usr/lib64/sssd/libsss_secrets.so
/usr/lib64/sssd/libsss_semanage.so
/usr/lib64/sssd/libsss_simple.so
/usr/lib64/sssd/libsss_util.so
/usr/lib64/sssd/modules/libsss_autofs.so
/usr/lib64/sssd/modules/sssd_krb5_localauth_plugin.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/sssd/gpo_child
/usr/libexec/sssd/krb5_child
/usr/libexec/sssd/ldap_child
/usr/libexec/sssd/p11_child
/usr/libexec/sssd/proxy_child
/usr/libexec/sssd/sss_signal
/usr/libexec/sssd/sssd_autofs
/usr/libexec/sssd/sssd_be
/usr/libexec/sssd/sssd_ifp
/usr/libexec/sssd/sssd_kcm
/usr/libexec/sssd/sssd_nss
/usr/libexec/sssd/sssd_pac
/usr/libexec/sssd/sssd_pam
/usr/libexec/sssd/sssd_ssh
/usr/libexec/sssd/sssd_sudo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sssd/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/sssd/978773e74b4cfcbe611ae1217754f259ad37ac96

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f sssd.lang
%defattr(-,root,root,-)

