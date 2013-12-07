# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/ijqc
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-ijqc
Version:	1.2
Release:	5
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

%description
ijqc.bst is a BibTeX style file to support publication in
Wiley's International Journal of Quantum Chemistry. It is not
in any way officially endorsed by the publisher or editors, and
is provided without any warranty one could ever think of.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/ijqc/ijqc.bst
%doc %{_texmfdistdir}/doc/bibtex/ijqc/README
%doc %{_texmfdistdir}/doc/bibtex/ijqc/makefile
%doc %{_texmfdistdir}/doc/bibtex/ijqc/mybib.bib
%doc %{_texmfdistdir}/doc/bibtex/ijqc/xampl.pdf
%doc %{_texmfdistdir}/doc/bibtex/ijqc/xampl.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 752729
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718707
- texlive-ijqc
- texlive-ijqc
- texlive-ijqc
- texlive-ijqc

