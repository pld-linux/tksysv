Summary:	An X editor for editing runlevel services
Summary(pl):	Narzêdzie pod X do edycji serwisów uruchamianych przy starcie
Name:		tksysv
Version:	1.0
Release:	6
License:	GPL
Group:		X11/Applications/System
Source0:	%{name}-%{version}.tar.gz
Requires:	tcl tk chkconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define		_libdir		/usr/lib

%description
Tksysv is an X Window System based graphical interface for editing the
services provided by different runlevels. Tksysv is used to set which
services are stopped and which services are started in the different
runlevels on your system.

Install the tksysv package if you'd like to use a graphical tool for
editing runlevel services.

%description -l pl
Tksysv jest bazuj±cym na X Window System graficznym interfejsem do
wyboru serwisów, które maj± byæ uruchamiane przy starcie w
poszczególnych runlevelach.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
PREFIX=$RPM_BUILD_ROOT ./Install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%{_libdir}/tksysv
%{_bindir}/tksysv
%{_libdir}/rhs/control-panel/tksysv.init
%{_libdir}/rhs/control-panel/tksysv.gif
%{_libdir}/rhs/control-panel/tksysv.xpm
%{_mandir}/man8/tksysv.8*
