Name:		texlive-printlen
Version:	19847
Release:	1
Summary:	Print lengths using specified units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/printlen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/printlen.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/printlen.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
\printlength{length} prints the value of a LaTeX length in the
units specified by \uselengthunit{unit} ('unit' may be any TeX
length unit except for scaled point, viz., any of: pt, pc, in,
mm, cm, bp, dd or cc). When the unit is pt, the printed length
value will include any stretch or shrink; otherwise these are
not printed. The 'unit' argument may also be PT, in which case
length values will be printed in point units but without any
stretch or shrink values.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/printlen/printlen.sty
%doc %{_texmfdistdir}/doc/latex/printlen/printlen-doc.pdf
%doc %{_texmfdistdir}/doc/latex/printlen/printlen-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
