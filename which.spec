Summary:     Finds a program 'which' is in one of the directories on your PATH
Summary(de): Findet ein Programm in einem der Verzeichnisse in Ihrem PATH
Summary(fr): Recherche un programme dans l'un des répertoires de votre PATH.
Summary(pl): Program 'witch'
Summary(tr): PATH'de bulunan bir dosyanýn yerini bulmayý saðlayan bir araç
Name:        which
Version:     1.0
Release:     9
Copyright:   distributable
Group:       Utilities/File
Source:      ftp://sunsite.unc.edu/pub/Linux/distributions/slackware/source/a/bin/%{name}.tar.gz
Buildroot:   /tmp/%{name}-%{version}-root

%description
Give it a program name, and it tells you if it is on your 'PATH'.

For example, 'which ls' would print '/bin/ls', because the ls program,
which is in one of the directories listed in your PATH environment
variable, is located in the /bin directory.

%description -l de
Geben Sie ihm einen Programmnamen, und es sagt Ihnen, ob sich
dieser in Ihrem PATH befindet. 

Beispielsweise würde 'which ls' das Ergebnis '/bin/ls' liefern, weil
sich das ls-Programm, das in einem der Verzeichnisse in Ihrer
PATH-Umgebungsvariable abgelegt ist, sich im /bin-Verzeichnis
befindet.

%description -l fr
Donnez lui un nom de programme, et il vous dit s'il est dans votre 'PATH'.

Par exemple 'which ls' afficherait '/bin/ls', car le programme ls, qui
se trouve dans un des répertoires listées dans votre variable d'environnement
PATH, est situé dans le répertoire /bin/.

%description -l pl 
Program 'witch' pomo¿e Ci odszukaæ dany program i powie Ci czy masz go w
swojej ¶cie¿ce.

%description -l tr
which bir komut veya programýn PATH'inizde bulunup bulunmadýðýný belirtir.

%prep
%setup -q -n %{name}

%build
make DESTDIR="/usr/bin" CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

install which.1 $RPM_BUILD_ROOT/usr/man/man1/which.1
install -s which $RPM_BUILD_ROOT/usr/bin/which

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/bin/which
%attr(644, root,  man) /usr/man/man1/which.1

%changelog
* Wed Oct 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-9]
- added using $RPM_OPT_FLAGS during compile.

* Thu Jul 23 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- added pl translation.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc
