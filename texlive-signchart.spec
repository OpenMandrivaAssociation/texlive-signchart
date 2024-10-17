Name:		texlive-signchart
Version:	39707
Release:	2
Summary:	Create beautifully typeset sign charts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/signchart
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/signchart.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/signchart.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/signchart.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows users to easily typeset beautiful looking
sign charts directly into their (La)TeX document.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/signchart
%{_texmfdistdir}/tex/latex/signchart
%doc %{_texmfdistdir}/doc/latex/signchart

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
