Name: klive
Version: 20070203
Release: %mkrel 5
Group: Development/Kernel
Summary: Script to gather information about kernel usage
License: GPL
URL: http://klive.cpushare.com/
Source: %{name}-%{version}.tar.bz2
Source1: klive.init
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires: python
Requires: python-twisted

%description
This program aims to provide kernel live feedback about the usage of every
different Linux Kernel version.
It is a client-server model that feeds some kernel related information from
volunteer clients into a klive server. The server statistically treats and
shows the data in some nice web tables.
The KLive system is used by any volunteer Linux users that wish to contribute
and provide statistical information about kernel versions usage. Ultimately,
this information helps in the kernel development process. 

You can access the collected statistics at http://klive.cpushare.com.

%prep
%setup -q

%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install -m644 klive.tac -D $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/klive.tac
install -c -m 0700 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/klive

%clean
rm -rf %{buildroot}

%post
%_post_service klive

%preun
%_preun_service klive

%files
%defattr(-,root,root)
%attr(700,root,root) %dir %{_localstatedir}/lib/%{name}
%attr(644,root,root) %{_localstatedir}/lib/%{name}/klive.tac
%attr(700,root,root) %{_sysconfdir}/rc.d/init.d/klive


