Summary:	Palm OS resource compiler
Summary(pl.UTF-8):   Kompilator zasobów dla Palm OS
Name:		pilrc
Version:	3.2
Release:	2
License:	GPL
Group:		Development/Building
Source0:	http://dl.sourceforge.net/pilrc/%{name}-%{version}.tar.gz
# Source0-md5:	9a1e114c5fe1f6fa0ffbb742c4d8510e
URL:		http://pilrc.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
Obsoletes:	pilrc-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Palm OS computers keep lots program data inside resources integrated
into the program binary. Pilrc is essential program to create this
resources.

%description -l pl.UTF-8
Programy dla komputerów z Palm OS trzymają wiele danych w tzw.
zasobach wewnątrz pliku z programem. Pilrc jest programem niezbędnym
do tworzenia tych zasobów.

%prep
%setup -q

%build
cd unix
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..
./unix/%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc example
%attr(755,root,root) %{_bindir}/pilrc
%{_datadir}/%{name}
