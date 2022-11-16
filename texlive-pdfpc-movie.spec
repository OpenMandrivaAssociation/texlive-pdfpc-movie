Name:		texlive-pdfpc-movie
Version:	48245
Release:	1
Summary:	Pdfpc viewer-compatible hyperlinks to movies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfpc-movie
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpc-movie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpc-movie.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpc-movie.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX2e package provides a command \pdfpcmovie for
embedding (hyperlinking) movies in a way compatible with the
PDF Presenter Console (pdfpc), a GPL2-licensed multi-monitor
PDF presentation viewer application available on GitHub and
shipped with some LINUX distributions such as Debian, Fedora,
and Arch. The package depends on etoolbox, hyperref, and
pgfkeys.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pdfpc-movie
%{_texmfdistdir}/tex/latex/pdfpc-movie
%doc %{_texmfdistdir}/doc/latex/pdfpc-movie

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
