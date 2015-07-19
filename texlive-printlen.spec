# revision 19847
# category Package
# catalog-ctan /macros/latex/contrib/printlen
# catalog-date 2010-09-22 14:58:28 +0200
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-printlen
Version:	1.1a
Release:	10
Summary:	Print lengths using specified units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/printlen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/printlen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/printlen.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-2
+ Revision: 755066
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-1
+ Revision: 719300
- texlive-printlen
- texlive-printlen
- texlive-printlen
- texlive-printlen

