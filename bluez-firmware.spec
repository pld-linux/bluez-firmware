Summary:	Bluetooth Firmware data
Summary(pl):	Dane firmware do urz±dzeñ Bluetooth
Name:		bluez-firmware
Version:	1.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	2f1c2d939108c865dd07bae3e819c573
URL:		http://bluez.sourceforge.net/
# /etc/bluetooth dir belongs to bluez-utils, hotplug stuff since 2.10
Requires:	bluez-utils >= 2.10
Obsoletes:	bluez-bluefw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir	/lib

%description
Bluetooth Firmware data.

%description -l pl
Dane firmware do urz±dzeñ Bluetooth.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_libdir}/firmware/BCM*
