%define name	hawknl

%define major 1.6

%define libname	%mklibname %name %major
%define develname %mklibname -d %name
%define sdevelname %mklibname -d -s %name

Name:		%name
Version:	1.68
Release:	%mkrel 5
URL:		http://www.hawksoft.com/hawknl/
Summary:	Hawk Network Library
Source:		HawkNL168src.zip
Patch0:		hawknl_makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}
License:	LGPLv2+
Group:		System/Libraries
%description
HawkNL is a free, open source, game oriented network API released under
the GNU Library General Public License (LGPL). HawkNL (NL) is a fairly
low level API, a wrapper over Berkeley/Unix Sockets and Winsock. But NL
also provides other features including support for many OSs, groups of
sockets, socket statistics, high accuracy timer, CRC functions, macros
to read and write data to packets with endian conversion, and support
for multiple network transports.

%package -n %libname
Summary:	Hawk Network Library
Group:		System/Libraries
%description -n %libname
HawkNL is a free, open source, game oriented network API released under
the GNU Library General Public License (LGPL). HawkNL (NL) is a fairly
low level API, a wrapper over Berkeley/Unix Sockets and Winsock. But NL
also provides other features including support for many OSs, groups of
sockets, socket statistics, high accuracy timer, CRC functions, macros
to read and write data to packets with endian conversion, and support
for multiple network transports.

%package -n %develname
Summary:	Hawk Network Library development files
Group:		System/Libraries
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
%description -n %develname
Developement files for %libname

%package -n %sdevelname
Summary:	Hawk Network Library (static library)
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}
%description -n %sdevelname
Hawk static library.

%prep
%setup -q -n HawkNL%{version}
%patch0 -p1

%build
%make -f makefile.linux
%{__chmod} -R go-w samples

%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_includedir} %{buildroot}%{_libdir}
cd src
%{__make} -f makefile.linux INCDIR=%{buildroot}%{_includedir} LIBDIR=%{buildroot}%{_libdir} install

%clean
%{__rm} -Rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%doc src/readme.txt src/NLchanges.txt
%{_libdir}/libNL.so.%{major}*
%{_libdir}/libNL.so.1
%{_libdir}/NL.so.%major

%files -n %develname
%doc samples
%{_includedir}/nl.h
%{_libdir}/NL.so
%{_libdir}/libNL.so

%files -n %sdevelname
%{_libdir}/libNL.a



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.68-5mdv2011.0
+ Revision: 619356
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.68-4mdv2010.0
+ Revision: 429389
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.68-3mdv2009.0
+ Revision: 240831
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Aug 18 2007 Nicolas Vigier <nvigier@mandriva.com> 1.68-1mdv2008.0
+ Revision: 65403
- Import hawknl

