#
Summary:	Palm OS resource compiler
Summary(pl):	Kompilator zasobów dla Palm OS
Name:		pilrc
Version:	3.2
Release:	1
License:	GPL
Group:		Development/Building
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9a1e114c5fe1f6fa0ffbb742c4d8510e
URL:		http://%{name}.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Palm OS computers keep lots program data inside resources integrated
into the program binary. Pilrc is essential program to create this
resources.

%description -l pl
Programy dla komputerów z Palm OS trzymaj± wiele danych w tzw.
zasobach wewn±trz pliku z programem. Pilrc jest programem niezbêdnym
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
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc example
%attr(755,root,root) %{_bindir}/pilrc
%{_datadir}/%{name}
