Name: klive
Version: 20070203
Release: 7
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




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20070203-6mdv2011.0
+ Revision: 619968
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 20070203-5mdv2010.0
+ Revision: 429690
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 20070203-4mdv2009.0
+ Revision: 247775
- rebuild

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 20070203-2mdv2008.1
+ Revision: 170927
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 20070203-1mdv2008.1
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Feb 03 2007 Emmanuel Andry <eandry@mandriva.org> 20070203-1mdv2007.0
+ Revision: 116087
- downloaded latest version
- %%mkrel
- Import klive

* Tue Apr 04 2006 Leonardo Chiquitto Filho <chiquitto@mandriva.com> 20060403-1mdk
- initial release

