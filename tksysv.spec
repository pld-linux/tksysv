Summary: An X editor for editing runlevel services.
Name: tksysv
Version: 1.0
Release: 6
Copyright: GPL
Group: Applications/System
Source: tksysv-1.0.tar.gz
Requires: tcl tk chkconfig
BuildArchitectures: noarch
Buildroot: /var/tmp/tksysv-root

%description
Tksysv is an X Window System based graphical interface for editing
the services provided by different runlevels.  Tksysv is used to set
which services are stopped and which services are started in the
different runlevels on your system.

Install the tksysv package if you'd like to use a graphical tool for
editing runlevel services.

%prep
%setup

%install
PREFIX=$RPM_BUILD_ROOT ./Install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGELOG COPYING
/usr/lib/tksysv
/usr/X11R6/bin/tksysv
/usr/lib/rhs/control-panel/tksysv.init
/usr/lib/rhs/control-panel/tksysv.gif
/usr/lib/rhs/control-panel/tksysv.xpm
/usr/man/man8/tksysv.8
