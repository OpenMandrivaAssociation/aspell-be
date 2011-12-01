%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.01

%define languageenglazy Belarussian
%define languagecode be
%define lc_ctype be_BY

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.50.0
Release:       %mkrel 12
Group:         System/Internationalization
#Source:        ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell5-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}


BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
#%setup -q -n %{name}-%{src_ver}
%setup -q -n aspell5-be-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr %{buildroot}

%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} #doc/*

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README.%{languagecode} Copyright 
#%doc doc/*
%{_libdir}/aspell-*/*


