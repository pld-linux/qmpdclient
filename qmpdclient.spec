Summary:	QMPDClient is an easy to use MPD client written in Qt 4
Summary(hu.UTF-8):	QMPDClient egy könnyen használható Qt4-alapú MPD kliens
Name:		qmpdclient
Version:	1.0.9
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://havtknut.tihlde.org/qmpdclient/files/%{name}-%{version}.tar.gz
# Source0-md5:	775d9a01b64408ba58997c089c0ed0d5
URL:		http://havtknut.tihlde.org/qmpdclient
BuildRequires:	QtGui-devel
BuildRequires:	libpng-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
Suggests:	mpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QMPDClient is an easy to use MPD client written in Qt 4.

%description -l hu.UTF-8
QMPDClient egy könnyen használható Qt4-alapú MPD kliens

%prep
%setup -q
sed -i "s@usr/local@usr@g" qmpdclient.pro

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}
for i in 16 22 48 64; do
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps
install icons/%{name}${i}.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps/qmpdclient.png
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc AUTHORS Changelog README THANKSTO
%{_datadir}/icons/hicolor/*/apps/*.png
