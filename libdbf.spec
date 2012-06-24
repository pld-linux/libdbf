Summary:	A set of tools to manipulate xbase files
Summary(pl):	Zestaw narz�dzi do obr�bki baz danych typu .dbf
Name:		libdbf
Version:	1.5
Release:	1
License:	non-commercial
Group:		Applications/Databases
Group(pl):	Aplikacje/Bazy danych
Source0:	ftp://ftp.pwr.wroc.pl/pub/linux/libs/db/%{name}.tar.gz
Patch0:		%{name}-PLD.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
libdbf is a set of tools to manipulate xbase files - using them you can
list records from existing .dbf file, add and delete records, convert text
database to XBase, create indexes and many more...

%description -l pl
libdbf to zestaw narz�dzi do obr�bki baz danych w plikach .dbf - przy ich
u�yciu mo�esz obejrze� spis rekord�w pochodz�cych z istniej�cego pliku
.dbf, dodawa� i usuwa� rekordy, zmieni� tekstow� baz� danych na format
XBase, tworzy� indeksy i wiele innych rzeczy...

%prep
%setup -q
%patch -p0

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install dbflst dbfget dbfadd dbfdel dbfndx dbfpack dbfcreat \
	$RPM_BUILD_ROOT%{_bindir}
install tmpl $RPM_BUILD_ROOT%{_bindir}/dbftmpl

gzip -9nf README README.linux

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz
