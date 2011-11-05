# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/ijqc
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-ijqc
Version:	1.2
Release:	1
Summary:	BibTeX style file for the Intl. J. Quantum Chem
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/ijqc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ijqc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ijqc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
ijqc.bst is a BibTeX style file to support publication in
Wiley's International Journal of Quantum Chemistry. It is not
in any way officially endorsed by the publisher or editors, and
is provided without any warranty one could ever think of.

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
%{_texmfdistdir}/bibtex/bst/ijqc/ijqc.bst
%doc %{_texmfdistdir}/doc/bibtex/ijqc/README
%doc %{_texmfdistdir}/doc/bibtex/ijqc/makefile
%doc %{_texmfdistdir}/doc/bibtex/ijqc/mybib.bib
%doc %{_texmfdistdir}/doc/bibtex/ijqc/xampl.pdf
%doc %{_texmfdistdir}/doc/bibtex/ijqc/xampl.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
