Summary: dbflib - a set of tools to manipulate xbase files
Summary(pl): dbflib - zestaw narzêdzi do obróbki baz danych typu .dbf
Name: libdbf
Version: 1.5
Release: 1
Copyright: non-commercial
Group: Applications/Databases
Group(pl): Aplikacje/Bazy danych
Vendor: PLD
Distribution: PLD
Source: %{name}-%{version}.tar.gz
Patch: %{name}-smallfix.patch
Buildroot: /tmp/%{name}-%{version}-root

%description
libdbf is a set of tools to manipulate xbase files

  dbflst is used to list all the records in the file out to the stdout
  dbfget lists to stdout the specified records
  dbfadd is used to add a record to the end of a .dbf file
  dbfdel allows you to mark as deleted a record in a .dbf file
  dbfpack removes deleted records from the specified .dbf file
  dbfndx lists to stdout contents of .ndx (index) file
  dbftmpl builds the tmpl.dbf
  dbfcreat is used to create a database from a properly structured database
           that uses the field structure defined in tmpl.dbf

%description -l pl
libdbf to zestaw narzêdzi do obróbki baz danych w plikach .dbf

  dbflst wypisuje wszystkie rekordy z pliku na standardowe wyj¶cie
  dbfget wypisuje jedynie wyszczególnione rekordy
  dbfadd jest u¿ywany do dodawania rekordów na koñcu pliku .dbf
  dbfdel pozwala na zaznaczenie rekordów w pliku .dbf jako usuniête.
  dbfpack wyrzuca usuniête rekordy z bazy
  dbfndx wypisuje zawarto¶æ pliku .ndx (indeksu)
  dbftmpl tworzy plik tmpl.dbf
  dbfcreat tworzy now± bazê z bazy utworzonej na podstawie struktury bazy
           tmpl.dbf

%prep
%setup -q
%patch -p0

%build
make CFLAGS="$RPM_OPT_FLAGS -DUCHAR"
mv tmpl dbftmpl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin
install -s dbflst $RPM_BUILD_ROOT/usr/bin
install -s dbfget $RPM_BUILD_ROOT/usr/bin
install -s dbfadd $RPM_BUILD_ROOT/usr/bin
install -s dbfdel $RPM_BUILD_ROOT/usr/bin
install -s dbfndx $RPM_BUILD_ROOT/usr/bin
install -s dbfpack $RPM_BUILD_ROOT/usr/bin
install -s dbfcreat $RPM_BUILD_ROOT/usr/bin
install -s dbftmpl $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) /usr/bin/*
%doc README README.linux

%changelog
* Mon Aug 6 1999 Sebastian Zagrodzki <s.zagrodzki@sith.mimuw.edu.pl>
- initial rpm release
- fixed few warnings
- fixed addition of ".dbf" suffix in dbfcreat.c
