Summary:	Displays where a particular program in your path is located
Summary(de.UTF-8):	Zeigt an, wo sich ein Programm befindet
Summary(es.UTF-8):	Localiza un programa que está en uno de los directorios de su PATH
Summary(fr.UTF-8):	Recherche un programme dans l'un des répertoires de votre PATH
Summary(pl.UTF-8):	Pokazuje pod jaką ścieżką jest zlokalizowany program
Summary(pt_BR.UTF-8):	Localiza um programa que está em um dos diretórios de seu PATH
Summary(ru.UTF-8):	Показывает, в каком из каталогов в PATH находится программа
Summary(tr.UTF-8):	PATH'de bulunan bir dosyanın yerini bulmayı sağlayan bir araç
Summary(uk.UTF-8):	Показує, в якому з каталогів в PATH знаходиться програма
Name:		which
Version:	2.23
Release:	1
License:	GPL v3+
Group:		Applications/File
Source0:	https://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.gz
# Source0-md5:	1963b85914132d78373f02a84cdb3c86
Source1:	%{name}.csh
Source2:	%{name}.sh
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	8c6cfc55ca1046a2812eafd17d29561c
Patch0:		%{name}-info.patch
URL:		https://savannah.gnu.org/projects/which/
# for (static) -liberty
BuildRequires:	binutils-devel
BuildRequires:	texinfo
BuildRequires:	rpmbuild(macros) >= 2.043
Requires:	setup >= 2.4.6-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%description -l es.UTF-8
Tu le das un nombre de programa, y el te dirá si está en su 'PATH'.
Por ejemplo, 'which ls' podría imprimir '/bin/ls', porque el programa
ls, que está en uno de los directorios listados en la variable de
ambiente PATH, está localizado en el directorio /bin.

%description -l de.UTF-8
Der which-Befehl zeigt den ganzen Pfadname eines angegebenen
Programms, wenn es sich im PATH befindet.

%description -l fr.UTF-8
La commande which affiche le chemin complet d'un programme spécifié,
si ce programme est dans votre PATH.

%description -l pl.UTF-8
Program 'which' pomoże Ci odszukać dany program i powie Ci czy masz go
w swojej ścieżce.

%description -l pt_BR.UTF-8
Dê a ele um nome de programa, e ele lhe dirá se está no seu 'PATH'.
Por exemplo, 'which ls' poderia imprimir '/bin/ls', porque o programa
ls, que está em um dos diretórios listados na variável de ambiente
PATH, está localizado no diretório /bin.

%description -l ru.UTF-8
Команда 'which' показывает полный путь к указанной программе, если эта
программа есть в вашем пути поиска программ, PATH.

%description -l tr.UTF-8
which bir komut veya programın PATH'inizde bulunup bulunmadığını
belirtir.

%description -l uk.UTF-8
Команда 'which' показує повний шлях до вказаної програми, якщо ця
програма є в вашому шляху пошуку програм, PATH.

%prep
%setup -q
%patch -P0 -p1

%build
# cwm4/aclocal/CW_OPG_CXXFLAGS.m4 uses `[[ .. =~ regex ]]` bashism
%define configureshell /bin/bash
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/shrc.d

bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.which-non-english-man-pages

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS EXAMPLES NEWS README*
%attr(755,root,root) %{_bindir}/which
%config(noreplace) %verify(not md5 mtime size) /etc/shrc.d/which.csh
%config(noreplace) %verify(not md5 mtime size) /etc/shrc.d/which.sh
%{_mandir}/man1/which.1*
%lang(fi) %{_mandir}/fi/man1/which.1*
%lang(fr) %{_mandir}/fr/man1/which.1*
%lang(hu) %{_mandir}/hu/man1/which.1*
%lang(it) %{_mandir}/it/man1/which.1*
%lang(pl) %{_mandir}/pl/man1/which.1*
%{_infodir}/which.info*
