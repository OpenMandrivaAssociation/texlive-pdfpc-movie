%global tl_name pdfpc-movie
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Pdfpc viewer-compatible hyperlinks to movies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfpc-movie
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpc-movie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpc-movie.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfpc-movie.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX2e package provides a command \pdfpcmovie for embedding
(hyperlinking) movies in a way compatible with the PDF Presenter Console
(pdfpc), a GPL2-licensed multi-monitor PDF presentation viewer
application available on GitHub and shipped with some LINUX
distributions such as Debian, Fedora, and Arch. The package depends on
etoolbox, hyperref, and pgfkeys.

