Name:       twm
Version:    1.0.12
Release:    1%{?dist}
Summary:    Tab Window Manager for the X Window System
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/app/%{name}
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  byacc
BuildRequires:  make
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17

%description
twm is a window manager for the X Window System.  It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointer-driven
keyboard focus, and user-specified key and pointer button bindings.

%package doc
Summary:    Documentation for %{name}
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}

%files doc
%license COPYING
%{_mandir}/man1/%{name}.1*
