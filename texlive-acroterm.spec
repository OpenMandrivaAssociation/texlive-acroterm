Name:		texlive-acroterm
Version:	61719
Release:	2
Summary:	Manage and index acronyms and terms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/acroterm
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acroterm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acroterm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acroterm.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
