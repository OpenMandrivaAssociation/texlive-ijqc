Name:		texlive-ijqc
Version:	15878
Release:	2
Summary:	BibTeX style file for the Intl. J. Quantum Chem
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/ijqc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ijqc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ijqc.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
