#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.3
%define		qtver		5.15.2
%define		kaname		skladnik
Summary:	A Japanese warehouse keeper sokoban game by KDE
Name:		ka6-%{kaname}
Version:	25.08.3
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	f3fd33d85bc83ae6d9cb2496590ce169
URL:		http://apps.kde.org/skladnik
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	ka6-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= 5.53.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf6-kcrash-devel >= 5.30.0
BuildRequires:	kf6-kdbusaddons-devel >= 6.0.0
BuildRequires:	kf6-ki18n-devel >= 5.30.0
BuildRequires:	kf6-kio-devel >= 5.30.0
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf6-kxmlgui-devel >= 5.30.0
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skladnik - a Japanese warehouse keeper sokoban game by KDE.

%description -l pl.UTF-8
Skladnik jest implementacją japońskiej gry "sokoban", w którą grali
magazynierzy.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ka5-%{kaname}-devel < %{version}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.


%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/skladnik
%{_desktopdir}/org.kde.skladnik.desktop
%{_iconsdir}/hicolor/*x*/apps/skladnik.png
%lang(ca) %{_mandir}/ca/man6/skladnik.6*
%lang(es) %{_mandir}/es/man6/skladnik.6*
%lang(it) %{_mandir}/it/man6/skladnik.6*
%{_mandir}/man6/skladnik.6*
%lang(nl) %{_mandir}/nl/man6/skladnik.6*
%lang(sl) %{_mandir}/sl/man6/skladnik.6*
%lang(uk) %{_mandir}/uk/man6/skladnik.6*
%{_datadir}/metainfo/org.kde.skladnik.metainfo.xml
%{_datadir}/skladnik
