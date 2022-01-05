#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Printf-style format-strings for user-defined string conversion
Summary(pl.UTF-8):	Łańcuchy formatujące w stylu printf do konwersji zdefiniowanych przez użytkownika
Name:		ocaml-ppx_custom_printf
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_custom_printf/tags
Source0:	https://github.com/janestreet/ppx_custom_printf/archive/v%{version}/ppx_custom_printf-%{version}.tar.gz
# Source0-md5:	18518b0464d61d165f4c73475d648ccb
URL:		https://github.com/janestreet/ppx_custom_printf
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_sexp_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_conv-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.18.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
ppx_custom_printf is a ppx rewriter that allows the use of
user-defined string conversion functions in format strings (that is,
strings passed to printf, sprintf, etc.).

This package contains files needed to run bytecode executables using
ppx_custom_printf library.

%description -l pl.UTF-8
ppx_custom_printf to moduł przepisujący ppx pozwalający na używanie
zdefiniowanych przez użytkownika funkcji konwertujących łańcuchy
znaków w łańcuchach formatujących (tzn. łańcuchach przekazywanych do
funkcji printf, sprintf itp.).

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_custom_printf.

%package devel
Summary:	Printf-style format-strings for user-defined string conversion - development part
Summary(pl.UTF-8):	Łańcuchy formatujące w stylu printf do konwersji zdefiniowanych przez użytkownika - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_sexp_conv-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.18.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_custom_printf library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_custom_printf.

%prep
%setup -q -n ppx_custom_printf-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_custom_printf/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_custom_printf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_custom_printf
%attr(755,root,root) %{_libdir}/ocaml/ppx_custom_printf/ppx.exe
%{_libdir}/ocaml/ppx_custom_printf/META
%{_libdir}/ocaml/ppx_custom_printf/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_custom_printf/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_custom_printf/*.cmi
%{_libdir}/ocaml/ppx_custom_printf/*.cmt
%{_libdir}/ocaml/ppx_custom_printf/*.cmti
%{_libdir}/ocaml/ppx_custom_printf/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_custom_printf/ppx_custom_printf.a
%{_libdir}/ocaml/ppx_custom_printf/*.cmx
%{_libdir}/ocaml/ppx_custom_printf/*.cmxa
%endif
%{_libdir}/ocaml/ppx_custom_printf/dune-package
%{_libdir}/ocaml/ppx_custom_printf/opam
