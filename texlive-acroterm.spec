%global tl_name acroterm
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Manage and index acronyms and terms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/acroterm
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acroterm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acroterm.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acroterm.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Yet another package for acronyms: the package offers simple markup of
acronyms and technical terms in the text, giving an index each of terms
and acronyms with their expanded form.

