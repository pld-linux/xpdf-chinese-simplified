Summary:	ISO-2022-CN, EUC-CN and GBK encoding support for xpdf
Summary(pl):	Wsparcie kodowania ISO-2022-CN, EUC-CN i GBK dla xpdf
Name:		xpdf-chinese-simplified
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}.tar.gz
URL:		http://www.foolabs.com/xpdf/
Requires:	xpdf
Requires(post,preun):	grep
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.) 
This package provides support files needed to use the Xpdf tools with
Chinese-simplified PDF files.

%description -l pl
Pakiety wspieraj±ce jêzyki Xpdf zawieraj± pliki CMap, kodowania oraz
ró¿ne inne informacje konfiguracyjne niezbêdne b±d¼ przydatne przy
okre¶lonych zestawach znaków. (Nie zawieraj± ¿adnych fontów).
Ten pakiet zawiera pliki potrzebne do u¿ywania narzêdzi Xpdf z
chiñskimi uproszczonymi plikami PDF.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xpdf/CMap-chinese-simplified

install *.unicodeMap $RPM_BUILD_ROOT%{_datadir}/xpdf
install *.cidToUnicode $RPM_BUILD_ROOT%{_datadir}/xpdf
install CMap/* $RPM_BUILD_ROOT%{_datadir}/xpdf/CMap-chinese-simplified

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/xpdfrc ]; then
	echo 'unicodeMap	ISO-2022-CN	/usr/X11R6/share/xpdf/ISO-2022-CN.unicodeMap' >> /etc/xpdfrc
	echo 'unicodeMap	EUC-CN		/usr/X11R6/share/xpdf/EUC-CN.unicodeMap' >> /etc/xpdfrc
	echo 'unicodeMap	GBK		/usr/X11R6/share/xpdf/GBK.unicodeMap' >> /etc/xpdfrc
	echo 'cidToUnicode	Adobe-GB1	/usr/X11R6/share/xpdf/Adobe-GB1.cidToUnicode' >> /etc/xpdfrc
	echo 'cMapDir		Adobe-GB1	/usr/X11R6/share/xpdf/CMap-chinese-simplified' >> /etc/xpdfrc
	echo 'toUnicodeDir			/usr/X11R6/share/xpdf/CMap-chinese-simplified' >> /etc/xpdfrc
	echo 'displayCIDFontX	Adobe-GB1	"-*-fangsong ti-medium-r-normal-*-%s-*-*-*-*-*-gb2312.1980-0" ISO-2022-CN' >> /etc/xpdfrc
else
 if ! grep -q /usr/X11R6/share/xpdf/ISO-2022-CN.unicodeMap /etc/xpdfrc; then
	echo 'unicodeMap	ISO-2022-CN	/usr/X11R6/share/xpdf/ISO-2022-CN.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q /usr/X11R6/share/xpdf/EUC-CN.unicodeMap /etc/xpdfrc; then
	echo 'unicodeMap	EUC-CN		/usr/X11R6/share/xpdf/EUC-CN.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q /usr/X11R6/share/xpdf/GBK.unicodeMap /etc/xpdfrc; then
	echo 'unicodeMap	GBK		/usr/X11R6/share/xpdf/GBK.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q /usr/X11R6/share/xpdf/Adobe-GB1.cidToUnicode /etc/xpdfrc; then
	echo 'cidToUnicode	Adobe-GB1	/usr/X11R6/share/xpdf/Adobe-GB1.cidToUnicode' >> /etc/xpdfrc
 fi
 if ! grep -q /usr/X11R6/share/xpdf/CMap-chinese-simplified /etc/xpdfrc; then
0	echo 'cMapDir		Adobe-GB1	/usr/X11R6/share/xpdf/CMap-chinese-simplified' >> /etc/xpdfrc
	echo 'toUnicodeDir			/usr/X11R6/share/xpdf/CMap-chinese-simplified' >> /etc/xpdfrc
 fi
 if ! grep -q "-*-fangsong ti-medium-r-normal-*-%s-*-*-*-*-*-gb2312.1980-0" /etc/xpdfrc; then
	echo 'displayCIDFontX	Adobe-GB1	"-*-fangsong ti-medium-r-normal-*-%s-*-*-*-*-*-gb2312.1980-0" ISO-2022-CN' >> /etc/xpdfrc
 fi
fi

%preun
grep -v /usr/X11R6/share/xpdf/ISO-2022-CN.unicodeMap /etc/xpdfrc > /etc/xpdfrc.new
grep -v /usr/X11R6/share/xpdf/EUC-CN.unicodeMap /etc/xpdfrc.new > /etc/xpdfrc
grep -v /usr/X11R6/share/xpdf/GBK.unicodeMap /etc/xpdfrc > /etc/xpdfrc.new
grep -v /usr/X11R6/share/xpdf/Adobe-GB1.cidToUnicode /etc/xpdfrc.new > /etc/xpdfrc
grep -v /usr/X11R6/share/xpdf/CMap-chinese-simplified /etc/xpdfrc > /etc/xpdfrc.new
grep -v "-*-fangsong ti-medium-r-normal-*-%s-*-*-*-*-*-gb2312.1980-0" /etc/xpdfrc.new > /etc/xpdfrc
rm -f /etc/xpdfrc.new

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/*
