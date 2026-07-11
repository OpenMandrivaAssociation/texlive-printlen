%global tl_name printlen
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	Print lengths using specified units
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/printlen
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/printlen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/printlen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
\printlength{length} prints the value of a LaTeX length in the units
specified by \uselengthunit{unit} ('unit' may be any TeX length unit
except for scaled point, viz., any of: pt, pc, in, mm, cm, bp, dd or
cc). When the unit is pt, the printed length value will include any
stretch or shrink; otherwise these are not printed. The 'unit' argument
may also be PT, in which case length values will be printed in point
units but without any stretch or shrink values.

