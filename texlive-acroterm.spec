# revision 20498
# category Package
# catalog-ctan /macros/latex/contrib/acroterm
# catalog-date 2010-11-19 20:33:28 +0100
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-acroterm
Version:	0.1
Release:	1
Summary:	Manage and index acronyms and terms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/acroterm
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acroterm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acroterm.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acroterm.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Yet another package for acronyms: the package offers simple
markup of acronyms and technical terms in the text, giving an
index each of terms and acronyms with their expanded form.

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
%{_texmfdistdir}/tex/latex/acroterm/acroterm.sty
%doc %{_texmfdistdir}/doc/latex/acroterm/README
%doc %{_texmfdistdir}/doc/latex/acroterm/acroterm.pdf
#- source
%doc %{_texmfdistdir}/source/latex/acroterm/acroterm.dtx
%doc %{_texmfdistdir}/source/latex/acroterm/acroterm.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
