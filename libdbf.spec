Summary:	A set of tools to manipulate xbase files
Summary(pl.UTF-8):	Zestaw narzędzi do obróbki baz danych typu .dbf
Name:		libdbf
Version:	1.5
Release:	4
License:	non-commercial
Group:		Applications/Databases
Source0:	ftp://ftp.pwr.wroc.pl/pub/linux/libs/db/%{name}.tar.gz
# Source0-md5:	318f4f639421e0996e316f12d9f3862e
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-creat.patch
Patch2:		%{name}-rlen.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdbf is a set of tools to manipulate xbase files - using them you
can list records from existing .dbf file, add and delete records,
convert text database to XBase, create indexes and many more...

%description -l pl.UTF-8
libdbf to zestaw narzędzi do obróbki baz danych w plikach .dbf - przy
ich użyciu możesz obejrzeć spis rekordów pochodzących z istniejącego
pliku .dbf, dodawać i usuwać rekordy, zmienić tekstową bazę danych na
format XBase, tworzyć indeksy i wiele innych rzeczy...

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install dbflst dbfget dbfadd dbfdel dbfndx dbfpack dbfcreat \
	$RPM_BUILD_ROOT%{_bindir}
install tmpl $RPM_BUILD_ROOT%{_bindir}/dbftmpl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.linux
%attr(755,root,root) %{_bindir}/*
