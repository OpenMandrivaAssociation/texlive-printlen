# revision 19847
# category Package
# catalog-ctan /macros/latex/contrib/printlen
# catalog-date 2010-09-22 14:58:28 +0200
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-printlen
Version:	1.1a
Release:	1
Summary:	Print lengths using specified units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/printlen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/printlen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/printlen.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
\printlength{length} prints the value of a LaTeX length in the
units specified by \uselengthunit{unit} ('unit' may be any TeX
length unit except for scaled point, viz., any of: pt, pc, in,
mm, cm, bp, dd or cc). When the unit is pt, the printed length
value will include any stretch or shrink; otherwise these are
not printed. The 'unit' argument may also be PT, in which case
length values will be printed in point units but without any
stretch or shrink values.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/printlen/printlen.sty
%doc %{_texmfdistdir}/doc/latex/printlen/printlen-doc.pdf
%doc %{_texmfdistdir}/doc/latex/printlen/printlen-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
