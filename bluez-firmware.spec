Summary:	Bluetooth Firmware data
Summary(pl):	Dane firmware do urz±dzeñ Bluetooth
Name:		bluez-firmware
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	0b424b4248ab5b2018515dac38174ec4
URL:		http://bluez.sourceforge.net/
# /etc/bluetooth dir belongs to bluez-utils, hotplug stuff since 2.10
Requires:	bluez-utils >= 2.10
Obsoletes:	bluez-bluefw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
# XXX: move to something more general (FHS?)?
%dir /lib/firmware
/lib/firmware/BCM*
