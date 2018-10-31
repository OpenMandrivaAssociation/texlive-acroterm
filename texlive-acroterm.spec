# revision 20498
# category Package
# catalog-ctan /macros/latex/contrib/acroterm
# catalog-date 2010-11-19 20:33:28 +0100
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-acroterm
Version:	0.1
Release:	11
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

%description
Yet another package for acronyms: the package offers simple
markup of acronyms and technical terms in the text, giving an
index each of terms and acronyms with their expanded form.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/acroterm/acroterm.sty
%doc %{_texmfdistdir}/doc/latex/acroterm/README
%doc %{_texmfdistdir}/doc/latex/acroterm/acroterm.pdf
#- source
%doc %{_texmfdistdir}/source/latex/acroterm/acroterm.dtx
%doc %{_texmfdistdir}/source/latex/acroterm/acroterm.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 749082
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 717790
- texlive-acroterm
- texlive-acroterm
- texlive-acroterm
- texlive-acroterm
- texlive-acroterm

