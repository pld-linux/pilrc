Summary:	Palm OS resource compiler
Summary(pl):	kompilator zasobów dla Palm OS
Name:		pilrc
Version:	2.9
Release:	0.1
License:	GPL
Group:		-
Source0:	http://www.ardiri.com/download/files/palm/%{name}_src.tgz
Patch0:		pilrc-make.patch
URL:		http://www.ardiri.com/index.php?redir=palm&cat=pilrc
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package gtk
Summary:	Palm OS resource compiler (gtk+ version)
Summary(pl):	kompilator zasobów dla Palm OS (wersja gtk+)
Group:		-

%description gtk

%description gtk -l pl

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc example
%attr(755,root,root) %{_bindir}/pilrc

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pilrcui
