Summary:	Displays where a particular program in your path is located
Summary(de):	Zeigt an, wo sich ein Programm befindet
Summary(es):	Localiza un programa que está en uno de los directorios de su PATH
Summary(fr):	Recherche un programme dans l'un des répertoires de votre PATH
Summary(pl):	Pokazuje pod jak± ¶cie¿k± jest zlokalizowany program
Summary(pt_BR):	Localiza um programa que está em um dos diretórios de seu PATH
Summary(ru):	ðÏËÁÚÙ×ÁÅÔ, × ËÁËÏÍ ÉÚ ËÁÔÁÌÏÇÏ× × PATH ÎÁÈÏÄÉÔÓÑ ÐÒÏÇÒÁÍÍÁ
Summary(tr):	PATH'de bulunan bir dosyanýn yerini bulmayý saðlayan bir araç
Summary(uk):	ðÏËÁÚÕ¤, × ÑËÏÍÕ Ú ËÁÔÁÌÏÇ¦× × PATH ÚÎÁÈÏÄÉÔØÓÑ ÐÒÏÇÒÁÍÁ
Name:		which
Version:	2.16
Release:	5
License:	GPL
Group:		Applications/File
Source0:	http://www.xs4all.nl/~carlo17/which/%{name}-%{version}.tar.gz
# Source0-md5:	830b83af48347a9a3520f561e47cbc9b
Source1:	%{name}.csh
Source2:	%{name}.sh
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	8c6cfc55ca1046a2812eafd17d29561c
URL:		http://www.xs4all.nl/~carlo17/which/
Requires:	setup >= 2.4.6-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%description -l es
Tu le das un nombre de programa, y el te dirá si está en su 'PATH'.
Por ejemplo, 'which ls' podría imprimir '/bin/ls', porque el programa
ls, que está en uno de los directorios listados en la variable de
ambiente PATH, está localizado en el directorio /bin.

%description -l de
Der which-Befehl zeigt den ganzen Pfadname eines angegebenen
Programms, wenn es sich im PATH befindet.

%description -l fr
La commande which affiche le chemin complet d'un programme spécifié,
si ce programme est dans votre PATH.

%description -l pl
Program 'which' pomo¿e Ci odszukaæ dany program i powie Ci czy masz go
w swojej ¶cie¿ce.

%description -l pt_BR
Dê a ele um nome de programa, e ele lhe dirá se está no seu 'PATH'.
Por exemplo, 'which ls' poderia imprimir '/bin/ls', porque o programa
ls, que está em um dos diretórios listados na variável de ambiente
PATH, está localizado no diretório /bin.

%description -l ru
ëÏÍÁÎÄÁ 'which' ÐÏËÁÚÙ×ÁÅÔ ÐÏÌÎÙÊ ÐÕÔØ Ë ÕËÁÚÁÎÎÏÊ ÐÒÏÇÒÁÍÍÅ, ÅÓÌÉ ÜÔÁ
ÐÒÏÇÒÁÍÍÁ ÅÓÔØ × ×ÁÛÅÍ ÐÕÔÉ ÐÏÉÓËÁ ÐÒÏÇÒÁÍÍ, PATH.

%description -l tr
which bir komut veya programýn PATH'inizde bulunup bulunmadýðýný
belirtir.

%description -l uk
ëÏÍÁÎÄÁ 'which' ÐÏËÁÚÕ¤ ÐÏ×ÎÉÊ ÛÌÑÈ ÄÏ ×ËÁÚÁÎÏ§ ÐÒÏÇÒÁÍÉ, ÑËÝÏ ÃÑ
ÐÒÏÇÒÁÍÁ ¤ × ×ÁÛÏÍÕ ÛÌÑÈÕ ÐÏÛÕËÕ ÐÒÏÇÒÁÍ, PATH.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/shrc.d
bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog EXAMPLES NEWS README*
%attr(755,root,root) %{_bindir}/*
/etc/shrc.d/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/*
