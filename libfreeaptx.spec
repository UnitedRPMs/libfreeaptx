%global commit0 c176b7de9c2017d0fc1877659cea3bb6c330aafa
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           libfreeaptx
Version:        0.1.1
Release:        7%{?dist}
Summary:        Open Source implementation of Audio Processing Technology codec (aptX)

License:        LGPLv2+
URL:            https://github.com/iamthehorker/libfreeaptx
Source0:	https://github.com/iamthehorker/libfreeaptx/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%package        devel
Summary:        Development files for libfreeaptx
Requires:       %{name} = %{version}-%{release}

%package        tools
Summary:        libfreeaptx encoder and decoder utilities
Requires:       %{name} = %{version}-%{release}

%description
This is Open Source implementation of Audio Processing Technology codec (aptX)
derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This codec is
mainly used in Bluetooth A2DP profile.

It provides dynamic linked shared library libfreeaptx.so and simple command line
utilities freeaptxenc and freeaptxdec for encoding and decoding operations.

%description    devel
The libfreeaptx-devel package contains libraries and header files for
developing applications that use libfreeaptx.

%description    tools
The libfreeaptx-tools package contains openaptxenc encoder and openaptxdec decoder
command-line utilities.

%prep
%autosetup -n libfreeaptx-%{commit0}

%build
%make_build STATIC_UTILITIES= LDFLAGS="%{build_ldflags}" CFLAGS="%{optflags}"

%install
%make_install PREFIX= LIBDIR="%{_libdir}" INCDIR="%{_includedir}" BINDIR="%{_bindir}"

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/freeaptx.h
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/freeaptxenc
%{_bindir}/freeaptxdec

%changelog

* Fri Sep 24 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 0.1.1-7
- Initial build
- Compatibility for others third-party repositories
