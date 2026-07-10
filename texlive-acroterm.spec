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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Yet another package for acronyms: the package offers simple markup of
acronyms and technical terms in the text, giving an index each of terms
and acronyms with their expanded form.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/acroterm
%dir %{_datadir}/texmf-dist/source/latex/acroterm
%dir %{_datadir}/texmf-dist/tex/latex/acroterm
%doc %{_datadir}/texmf-dist/doc/latex/acroterm/README
%doc %{_datadir}/texmf-dist/doc/latex/acroterm/acroterm.pdf
%doc %{_datadir}/texmf-dist/source/latex/acroterm/acroterm.dtx
%doc %{_datadir}/texmf-dist/source/latex/acroterm/acroterm.ins
%{_datadir}/texmf-dist/tex/latex/acroterm/acroterm.sty
