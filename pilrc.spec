# TODO:
# - add desktop and icon file for pilrcui.
#
Summary:	Palm OS resource compiler
Summary(pl):	Kompilator zasobów dla Palm OS
Name:		pilrc
Version:	2.9
Release:	1
License:	GPL
Group:		Development/Building
Source0:	http://www.ardiri.com/download/files/palm/%{name}_src.tgz
Patch0:		pilrc-make.patch
URL:		http://www.ardiri.com/index.php?redir=palm&cat=pilrc
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

%package gtk
Summary:	Palm OS resource compiler (gtk+ version)
Summary(pl):	Kompilator zasobów dla Palm OS (wersja gtk+)
Group:		X11/Development/Tools

%description gtk
Version of pilrc with UI utilising GTK+.

%description gtk -l pl
Wersja pilrc pracuj±ca w ¶rodowisku graficznym GTK+.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pilrcui
