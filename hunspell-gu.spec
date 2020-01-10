Name: hunspell-gu
Summary: Gujarati hunspell dictionaries
Version: 20061015 
Release: 10%{?dist}
Source: http://downloads.sourceforge.net/project/openofficeorg.mirror/contrib/dictionaries/gu_IN.zip
Group: Applications/Text
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL+
BuildArch: noarch

Requires: hunspell

%description
Gujarati hunspell dictionaries.

%prep
%setup -q -c -n gu-IN

%build
chmod -x *.dic *.aff

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%files
%doc README_gu_IN.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061015-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Parag Nemade <pnemade AT redhat.com> - 20061015-9
- Resolves:rh#848845:-Source URL not working

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061015-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Parag Nemade <pnemade AT redhat.com> - 20061015-7
- spec cleanup 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061015-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 30 2011 Caolán McNamara <caolanm@redhat.com> - 20061015-5
- Resolves: rhbz#734218 remove executable flags

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20061015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 04 2008 Parag <pnemade@redhat.com> - 20061015-1
- Initial Fedora release
