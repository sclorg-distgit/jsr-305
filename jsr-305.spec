%global pkg_name jsr-305
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        0
Release:        0.18.20090319svn.9%{?dist}
Summary:        Correctness annotations for Java code

# The majority of code is BSD-licensed, but some Java sources
# are licensed under CC-BY license, see: $ grep -r Creative .
License:        BSD and CC-BY
URL:            http://jsr-305.googlecode.com/
BuildArch:      noarch

# There has been no official release yet.  This is a snapshot of the Subversion
# repository as of 19 Mar 2009.  Use the following commands to generate the
# tarball:
#   svn export -r 49 http://jsr-305.googlecode.com/svn/trunk jsr-305
#   tar -cvf jsr-305-0.4.20090319.tar jsr-305
#   xz jsr-305-0.4.20090319.tar
Source0:        jsr-305-0.4.20090319.tar.xz
# File containing URL to CC-BY license text
Source1:        NOTICE-CC-BY.txt

BuildRequires:  %{?scl_prefix_java_common}maven-local

%package javadoc
Summary:        Javadoc documentation for %{pkg_name}

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
cp %{SOURCE1} NOTICE-CC-BY

%mvn_file :ri %{pkg_name}
%mvn_alias :ri com.google.code.findbugs:jsr305
%mvn_package ":{proposedAnnotations,tcl}" __noinstall

# do not build sampleUses module - it causes Javadoc generation to fail
%pom_disable_module sampleUses
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc ri/LICENSE NOTICE-CC-BY sampleUses

%files javadoc -f .mfiles-javadoc
%doc ri/LICENSE NOTICE-CC-BY

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 0-0.18.20090319svn.9
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 0-0.18.20090319svn.8
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0-0.18.20090319svn.7
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0-0.18.20090319svn.6
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.18.20090319svn.5
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.18.20090319svn.4
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.18.20090319svn.3
- Mass rebuild 2014-02-18

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.18.20090319svn.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.18.20090319svn.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0-0.18.20090319svn
- Mass rebuild 2013-12-27

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.17.20090319svn
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.16.20090319svn
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Jun 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.15.20090319svn
- Update to current packaging guidelines

* Tue Jun 18 2013 Michal Srb <msrb@redhat.com> - 0-0.14.20090319svn
- Install license file with javadoc subpackage (Resolves: rhbz#975411)
- Add file containing link to CC-BY license text

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.13.20090319svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0-0.12.20090319svn
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0-0.11.20090319svn
- Add CC-BY to license tag
- Resolves: rhbz#876648

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20090319svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Richard Fearn <richardfearn@gmail.com> - 0-0.9.20090319svn
- Do not build sampleUses module as it causes Javadoc generation to fail

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20090319svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0-0.7.20090319svn
- Use maven3 to build
- Fix depmap
- Fix Jave BRs

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20090319svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 26 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0-0.5.20090319svn
- Fix pom filename (Resolves rhbz#655811)
- Remove tomcat5 BR (not needed anymore)
- Use new maven plugin names
- Remove gcj support
- Few tweaks according to new guidelines
- Make jars and javadocs versionless

* Thu Jan 14 2010 Jerry James <loganjerry@gmail.com> - 0-0.4.20090319svn
- Update to 19 Mar 2009 snapshot
- Compress with xz instead of bzip2
- BR tomcat5, a horrible workaround to solve bz 538868

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20090203svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar  4 2009 Jerry James <loganjerry@gmail.com> - 0-0.3.20090203svn
- Explicitly require OpenJDK to build

* Sat Feb 28 2009 Jerry James <loganjerry@gmail.com> - 0-0.2.20090203svn
- Update to 03 Feb 2009 snapshot

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20080824svn.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20080824svn.1
- Cleaned up summary

* Mon Sep  8 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20080824svn
- Update to 24 Aug 2008 snapshot

* Mon Aug  4 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20080721svn
- Update to 21 Jul 2008 snapshot

* Mon Jun 30 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20080613svn
- Update to 13 Jun 2008 snapshot
- Fix broken URLs
- Include instructions on regenerating the tarball
- Conditionalize the gcj bits

* Mon Jun  2 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20080527svn
- Update to 27 May 2008 snapshot

* Mon May 12 2008 Jerry James <loganjerry@gmail.com> - 0-0.1.20071105svn
- Initial RPM
