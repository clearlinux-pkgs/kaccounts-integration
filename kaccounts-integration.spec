#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kaccounts-integration
Version  : 21.12.1
Release  : 7
URL      : https://download.kde.org/stable/release-service/21.12.1/src/kaccounts-integration-21.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.1/src/kaccounts-integration-21.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.1/src/kaccounts-integration-21.12.1.tar.xz.sig
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
BuildRequires : qtbase-dev mesa-dev
BuildRequires : signond-dev

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
%setup -q -n kaccounts-integration-21.12.1
cd %{_builddir}/kaccounts-integration-21.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642024363
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make
popd

%install
export SOURCE_DATE_EPOCH=1642024363
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kaccounts-integration
cp %{_builddir}/kaccounts-integration-21.12.1/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kaccounts-integration-21.12.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kaccounts-integration-21.12.1/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kaccounts-integration-21.12.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kaccounts-integration-21.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kaccounts-integration-21.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kaccounts-integration/7d9831e05094ce723947d729c2a46a09d6e90275
pushd clr-build
%make_install
popd
%find_lang kaccounts-integration

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/AccountDetails.qml
/usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/Accounts.qml
/usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/AvailableAccounts.qml
/usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/MessageBoxSheet.qml
/usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/RemoveAccountDialog.qml
/usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/RenameAccountDialog.qml
/usr/share/kpackage/kcms/kcm_kaccounts/metadata.desktop
/usr/share/kpackage/kcms/kcm_kaccounts/metadata.json
/usr/share/kservices5/kcm_kaccounts.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/KAccounts/AccountServiceToggleJob
/usr/include/KAccounts/AccountsModel
/usr/include/KAccounts/ChangeAccountDisplayNameJob
/usr/include/KAccounts/Core
/usr/include/KAccounts/CreateAccountJob
/usr/include/KAccounts/GetCredentialsJob
/usr/include/KAccounts/KAccountsDPlugin
/usr/include/KAccounts/KAccountsUiPlugin
/usr/include/KAccounts/ProvidersModel
/usr/include/KAccounts/RemoveAccountJob
/usr/include/KAccounts/ServicesModel
/usr/include/KAccounts/accountservicetogglejob.h
/usr/include/KAccounts/accountsmodel.h
/usr/include/KAccounts/changeaccountdisplaynamejob.h
/usr/include/KAccounts/core.h
/usr/include/KAccounts/createaccountjob.h
/usr/include/KAccounts/getcredentialsjob.h
/usr/include/KAccounts/kaccounts_export.h
/usr/include/KAccounts/kaccounts_version.h
/usr/include/KAccounts/kaccountsdplugin.h
/usr/include/KAccounts/kaccountsuiplugin.h
/usr/include/KAccounts/providersmodel.h
/usr/include/KAccounts/removeaccountjob.h
/usr/include/KAccounts/servicesmodel.h
/usr/lib64/cmake/KAccounts/KAccountsConfig.cmake
/usr/lib64/cmake/KAccounts/KAccountsConfigVersion.cmake
/usr/lib64/cmake/KAccounts/KAccountsMacros.cmake
/usr/lib64/cmake/KAccounts/KAccountsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KAccounts/KAccountsTargets.cmake
/usr/lib64/libkaccounts.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkaccounts.so.2
/usr/lib64/libkaccounts.so.21.12.1
/usr/lib64/qt5/plugins/kaccounts/daemonplugins/kaccounts_kio_webdav_plugin.so
/usr/lib64/qt5/plugins/kcms/kcm_kaccounts.so
/usr/lib64/qt5/plugins/kf5/kded/kded_accounts.so
/usr/lib64/qt5/qml/org/kde/kaccounts/libkaccountsdeclarativeplugin.so
/usr/lib64/qt5/qml/org/kde/kaccounts/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kaccounts-integration/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kaccounts-integration/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kaccounts-integration/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kaccounts-integration/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kaccounts-integration/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kaccounts-integration.lang
%defattr(-,root,root,-)

