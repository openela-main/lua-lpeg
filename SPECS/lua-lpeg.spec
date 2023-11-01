
%{!?luaver: %global luaver %(test -x /usr/bin/lua && lua -e "print(string.sub(_VERSION, 5))" || echo 5.3)}
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-lpeg
Version:        1.0.1
Release:        6%{?dist}
Summary:        Parsing Expression Grammars for Lua

Group:          Development/Libraries
License:        MIT
URL:            http://www.inf.puc-rio.br/~roberto/lpeg/
Source0:        http://www.inf.puc-rio.br/~roberto/lpeg/lpeg-%{version}.tar.gz
%if 0%{?el5}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%endif

BuildRequires:  lua-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
Requires:       lua(abi) = %{luaver}
%else
Requires:       lua >= %{luaver}
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1630592
Patch0: 0001-Enable-execshield-ldflags.patch

%description
LPeg is a new pattern-matching library for Lua, based on Parsing Expression
Grammars (PEGs).

%prep
%autosetup -p1 -n lpeg-%{version}

%build
make %{?_smp_mflags} COPT="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{lualibdir}
%{__mkdir_p} %{buildroot}%{luapkgdir}
%{__install} -p lpeg.so %{buildroot}%{lualibdir}/lpeg.so.%{version}
%{__ln_s} lpeg.so.%{version} %{buildroot}%{lualibdir}/lpeg.so
%{__install} -p -m 0644 re.lua %{buildroot}%{luapkgdir}


%check
lua test.lua


%if 0%{?rhel}
%clean
%{__rm} -rf %{buildroot}
%endif


%files
%defattr(-,root,root,-)
%doc HISTORY lpeg.html re.html lpeg-128.gif test.lua
%{lualibdir}/*
%{luapkgdir}/*


%changelog
* Fri Sep 21 2018 Bastien Nocera <bnocera@redhat.com> - 1.0.1-6
+ lua-lpeg-1.0.1-6
- Enable execshield protection
- Resolves: #1630592

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 26 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 0.12.1-1
- update to 0.12.1
- rebuild for lua 5.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 0.12-1
- update to 0.12, lua 5.2

* Wed Apr  3 2013 Michel Alexandre Salim <michel@verity.localdomain> - 0.11-1
- Update to 0.11

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Michel Salim <salimma@fedoraproject.org> - 0.10.2-1
- Update to 0.10.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Tim Niemueller <tim@niemueller.de> - 0.9-1
- Update to 0.9

* Fri Jun 13 2008 Tim Niemueller <tim@niemueller.de> - 0.8.1-2
- Consistent macro usage, moved sed/chmod to prep

* Thu Jun 12 2008 Tim Niemueller <tim@niemueller.de> - 0.8.1-1
- Initial package

