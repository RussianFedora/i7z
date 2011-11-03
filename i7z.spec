%global svnrevision 70

Name:           i7z
Version:        0.28.svn%{svnrevision}
Release:        1%{?dist}.R
Summary:        A better i7 (and now i3, i5) reporting tool

License:        GPLv2+
URL:            http://code.google.com/p/i7z/
Source0:        %{name}-%{version}.svn%{svnrevision}.tar.xz

BuildRequires:  ncurses-devel

%description
Better i7 (and now i3, i5) reporting tool

%prep
%setup -q -n %{name}-%{version}.svn%{svnrevision}
sed -i -e 's|/usr/sbin|%{buildroot}/usr/sbin|' Makefile


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/sbin
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%doc README.txt



%changelog
* Thu Nov 03 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.28-1.svn70.R
- Initial build
