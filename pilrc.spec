Summary:	palm resource compiler
Summary(pl):	palm resource compiler
Name:		pilrc
Version:	2.9
Release:	0.1
License:	GPL
Group:		-
Source0:	http://www.ardiri.com/download/files/palm/%{name}_src.tgz
URL:		http://www.ardiri.com/index.php?redir=palm&cat=pilrc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q

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
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
