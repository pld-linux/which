Summary:	Displays where a particular program in your path is located
Summary(de):	Zeigt an, wo sich ein Programm befindet
Summary(fr):	Recherche un programme dans l'un des répertoires de votre PATH
Summary(pl):	Pokazuje pod jak± ¶cie¿k± jest zlokalizowany program
Summary(tr):	PATH'de bulunan bir dosyanýn yerini bulmayý saðlayan bir araç
Name:		which
Version:	2.11
Release:	2
License:	GPL
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source0:	ftp://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.gz
Source1:	which.csh
Source2:	which.sh
URL:		http://www.xs4all.nl/~carlo17/which/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The which command shows the full pathname of a specified program, if the
specified program is in your PATH.

%description -l de
Der which-Befehl zeigt den ganzen Pfadname eines angegebenen Programms,
wenn es sich im PATH befindet.

%description -l fr
La commande which affiche le chemin complet d'un programme spécifié, si ce
programme est dans votre PATH.

%description -l pl 
Program 'which' pomo¿e Ci odszukaæ dany program i powie Ci czy masz go w
swojej ¶cie¿ce.

%description -l tr
which bir komut veya programýn PATH'inizde bulunup bulunmadýðýný belirtir.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/profile.d

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README EXAMPLES NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,EXAMPLES,NEWS,AUTHORS}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /etc/profile.d/*
%{_mandir}/man1/*
