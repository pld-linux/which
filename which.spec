Summary:	Displays where a particular program in your path is located
Summary(de):	Zeigt an, wo sich ein Programm befindet
Summary(es):	Localiza un programa que est� en uno de los directorios de su PATH
Summary(fr):	Recherche un programme dans l'un des r�pertoires de votre PATH
Summary(pl):	Pokazuje pod jak� �cie�k� jest zlokalizowany program
Summary(pt_BR):	Localiza um programa que est� em um dos diret�rios de seu PATH
Summary(tr):	PATH'de bulunan bir dosyan�n yerini bulmay� sa�layan bir ara�
Name:		which
Version:	2.13
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://www.xs4all.nl/~carlo17/which/%{name}-%{version}.tar.gz
Source1:	%{name}.csh
Source2:	%{name}.sh
Source3:	%{name}-non-english-man-pages.tar.bz2
URL:		http://www.xs4all.nl/~carlo17/which/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%description -l es
Tu le das un nombre de programa, y el te dir� si est� en su 'PATH'.
Por ejemplo, 'which ls' podr�a imprimir '/bin/ls', porque el programa
ls, que est� en uno de los directorios listados en la variable de
ambiente PATH, est� localizado en el directorio /bin.

%description -l de
Der which-Befehl zeigt den ganzen Pfadname eines angegebenen
Programms, wenn es sich im PATH befindet.

%description -l fr
La commande which affiche le chemin complet d'un programme sp�cifi�,
si ce programme est dans votre PATH.

%description -l pl 
Program 'which' pomo�e Ci odszuka� dany program i powie Ci czy masz go
w swojej �cie�ce.

%description -l pt_BR
D� a ele um nome de programa, e ele lhe dir� se est� no seu 'PATH'.
Por exemplo, 'which ls' poderia imprimir '/bin/ls', porque o programa
ls, que est� em um dos diret�rios listados na vari�vel de ambiente
PATH, est� localizado no diret�rio /bin.

%description -l tr
which bir komut veya program�n PATH'inizde bulunup bulunmad���n�
belirtir.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/profile.d

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d
bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf README EXAMPLES NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /etc/profile.d/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
