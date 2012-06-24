Summary:	Finds a program 'which' is in one of the directories on your PATH
Summary(de):	Findet ein Programm in einem der Verzeichnisse in Ihrem PATH
Summary(fr):	Recherche un programme dans l'un des r�pertoires de votre PATH.
Summary(pl):	Program 'which'
Summary(tr):	PATH'de bulunan bir dosyan�n yerini bulmay� sa�layan bir ara�
Name:		which
Version:	2.5
Release:	1
Copyright:	distributable
Group:		Utilities/File
Group(pl):	Narz�dzia/Pliki
Source:		ftp://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.gz
URL:		http://www.xs4all.nl/~carlo17/which/
Buildroot:	/tmp/%{name}-%{version}-root

%description
Give it a program name, and it tells you if it is on your 'PATH'.

For example, 'which ls' would print '/bin/ls', because the ls program,
which is in one of the directories listed in your PATH environment
variable, is located in the /bin directory.

%description -l de
Geben Sie ihm einen Programmnamen, und es sagt Ihnen, ob sich
dieser in Ihrem PATH befindet. 

Beispielsweise w�rde 'which ls' das Ergebnis '/bin/ls' liefern, weil sich
das ls-Programm, das in einem der Verzeichnisse in Ihrer
PATH-Umgebungsvariable abgelegt ist, sich im /bin-Verzeichnis befindet.

%description -l fr
Donnez lui un nom de programme, et il vous dit s'il est dans votre 'PATH'.

Par exemple 'which ls' afficherait '/bin/ls', car le programme ls, qui
se trouve dans un des r�pertoires list�es dans votre variable d'environnement
PATH, est situ� dans le r�pertoire /bin/.

%description -l pl 
Program 'which' pomo�e Ci odszuka� dany program i powie Ci czy masz go w
swojej �cie�ce.

%description -l tr
which bir komut veya program�n PATH'inizde bulunup bulunmad���n� belirtir.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README EXAMPLES ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,EXAMPLES,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri May 21 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.5-1]
- updated Source Url,
- added URL filed.

* Mon May 17 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [2.4-1]
- package is FHS 2.0 compliant,
- spec file based on RH version; rewritten for PLD use by me,
  Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl> 
  and Micha� Kuratczyk <kura@pld.org.pl>,
- pl translation by Wojtek �lusarczyk <wojtek@shadow.eu.org>.
