%global svnrevision 81

Name:           i7z
Version:        0.28.svn%{svnrevision}
Release:        1%{?dist}.R
Summary:        A better i7 (and now i3, i5) reporting tool
Summary(ru):    Средство анализа работы процессоров Intel i3, i5, i7

License:        GPLv2+
URL:            http://code.google.com/p/i7z/
Source0:        %{name}-0.28.svn%{svnrevision}.tar.xz
Source100:      README.RFRemix

BuildRequires:  ncurses-devel

%description
Better i7 (and now i3, i5) reporting tool

%description -l ru
Позволяет просматривать состояние и частоту работы ядер
процессоров Intel i3, i5, i7

%prep
%setup -q -n %{name}-0.28.svn%{svnrevision}
sed -i -e 's|/usr/sbin|%{buildroot}/usr/sbin|' Makefile


%build
make %{?_smp_mflags}
cp %{SOURCE100} .


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/sbin
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%doc README.txt README.RFRemix


%changelog
* Tue Jan 24 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.28.svn81-1.R
- Update to new svn revision

* Wed Dec 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.28.svn78-1.R
- Update to new svn revision

* Tue Nov 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.28.svn71-1.R
- Update to new svn revision
- Added description in russian language


* Thu Nov 03 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 0.28-1.svn70.R
- Initial build
