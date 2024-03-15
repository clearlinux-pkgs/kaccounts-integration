#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: 3d985eb
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kaccounts-integration
Version  : 24.02.0
Release  : 34
URL      : https://download.kde.org/stable/release-service/24.02.0/src/kaccounts-integration-24.02.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.0/src/kaccounts-integration-24.02.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.0/src/kaccounts-integration-24.02.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0
Requires: kaccounts-integration-data = %{version}-%{release}
Requires: kaccounts-integration-lib = %{version}-%{release}
Requires: kaccounts-integration-license = %{version}-%{release}
Requires: kaccounts-integration-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libaccounts-glib-dev
BuildRequires : libaccounts-qt-dev
BuildRequires : qcoro6-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : signond-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Setting up accounts-sso
Accounts-SSO is the framework we are using to store secrets (tokens, passwords)
and for storing Accounts (small pieces of information containing a name,
a provider, etc).

%package data
Summary: data components for the kaccounts-integration package.
Group: Data

%description data
data components for the kaccounts-integration package.


%package dev
Summary: dev components for the kaccounts-integration package.
Group: Development
Requires: kaccounts-integration-lib = %{version}-%{release}
Requires: kaccounts-integration-data = %{version}-%{release}
Provides: kaccounts-integration-devel = %{version}-%{release}
Requires: kaccounts-integration = %{version}-%{release}

%description dev
dev components for the kaccounts-integration package.


%package lib
Summary: lib components for the kaccounts-integration package.
Group: Libraries
Requires: kaccounts-integration-data = %{version}-%{release}
Requires: kaccounts-integration-license = %{version}-%{release}

%description lib
lib components for the kaccounts-integration package.


%package license
Summary: license components for the kaccounts-integration package.
Group: Default

%description license
license components for the kaccounts-integration package.


%package locales
Summary: locales components for the kaccounts-integration package.
Group: Default

%description locales
locales components for the kaccounts-integration package.


%prep
%setup -q -n kaccounts-integration-24.02.0
cd %{_builddir}/kaccounts-integration-24.02.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710538892
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6
make
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6
make
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710538892
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kaccounts-integration
cp %{_builddir}/kaccounts-integration-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kaccounts-integration-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kaccounts-integration-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kaccounts-integration-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kaccounts-integration-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kaccounts-integration-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kaccounts-integration
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/qml/org/kde/kaccounts/kaccountsdeclarativeplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kaccounts/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kaccounts/qmldir

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_kaccounts.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/KAccounts6/KAccounts/AccountServiceToggleJob
/usr/include/KAccounts6/KAccounts/AccountsModel
/usr/include/KAccounts6/KAccounts/ChangeAccountDisplayNameJob
/usr/include/KAccounts6/KAccounts/Core
/usr/include/KAccounts6/KAccounts/CreateAccountJob
/usr/include/KAccounts6/KAccounts/GetCredentialsJob
/usr/include/KAccounts6/KAccounts/KAccountsDPlugin
/usr/include/KAccounts6/KAccounts/KAccountsUiPlugin
/usr/include/KAccounts6/KAccounts/ProvidersModel
/usr/include/KAccounts6/KAccounts/RemoveAccountJob
/usr/include/KAccounts6/KAccounts/ServicesModel
/usr/include/KAccounts6/kaccounts/accountservicetogglejob.h
/usr/include/KAccounts6/kaccounts/accountsmodel.h
/usr/include/KAccounts6/kaccounts/changeaccountdisplaynamejob.h
/usr/include/KAccounts6/kaccounts/core.h
/usr/include/KAccounts6/kaccounts/createaccountjob.h
/usr/include/KAccounts6/kaccounts/getcredentialsjob.h
/usr/include/KAccounts6/kaccounts/kaccountsdplugin.h
/usr/include/KAccounts6/kaccounts/kaccountsuiplugin.h
/usr/include/KAccounts6/kaccounts/providersmodel.h
/usr/include/KAccounts6/kaccounts/removeaccountjob.h
/usr/include/KAccounts6/kaccounts/servicesmodel.h
/usr/include/KAccounts6/kaccounts_export.h
/usr/include/KAccounts6/kaccounts_version.h
/usr/lib64/cmake/KAccounts6/KAccounts6Config.cmake
/usr/lib64/cmake/KAccounts6/KAccounts6ConfigVersion.cmake
/usr/lib64/cmake/KAccounts6/KAccounts6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KAccounts6/KAccounts6Targets.cmake
/usr/lib64/cmake/KAccounts6/KAccountsMacros.cmake
/usr/lib64/libkaccounts6.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkaccounts6.so.24.02.0
/V3/usr/lib64/qt6/plugins/kaccounts/daemonplugins/kaccounts_kio_webdav_plugin.so
/V3/usr/lib64/qt6/plugins/kf6/kded/kded_accounts.so
/V3/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_kaccounts.so
/V3/usr/lib64/qt6/qml/org/kde/kaccounts/libkaccountsdeclarativeplugin.so
/usr/lib64/libkaccounts6.so.2
/usr/lib64/libkaccounts6.so.24.02.0
/usr/lib64/qt6/plugins/kaccounts/daemonplugins/kaccounts_kio_webdav_plugin.so
/usr/lib64/qt6/plugins/kf6/kded/kded_accounts.so
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_kaccounts.so
/usr/lib64/qt6/qml/org/kde/kaccounts/libkaccountsdeclarativeplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kaccounts-integration/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kaccounts-integration/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kaccounts-integration/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kaccounts-integration/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kaccounts-integration/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kaccounts-integration.lang
%defattr(-,root,root,-)

