%define debug_package %{nil}
# Tests don't work inside abf because they need
# connectivity to github.com
# Probably best to do a --with-tests build when
# updating though...
%bcond_with tests

Name:		github-cli
Version:	2.70.0
Release:	1
Source0:	https://github.com/cli/cli/archive/refs/tags/v%{version}.tar.gz
# Sadly go has no concept of shared libraries
# Dependency tarball generated using
# go mod vendor
# tar cJf ../../../godeps-for-github-cli-%{version}.tar.xz vendor
Source1:	godeps-for-github-cli-%{version}.tar.xz
Url:		https://github.com/cli/cli
BuildRequires:	golang make
Summary:	CLI tools for working with github repositories
Group:		Development/Tools
License:	MIT

%description
CLI tools for working with github repositories

%prep
%autosetup -p1 -n cli-%{version} -a 1

%build
%make_build prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

%if %{with tests}
%check
make test
%endif

%files
%{_bindir}/gh
%{_mandir}/man1/*.1*
%{_datadir}/bash-completion/completions/gh
%{_datadir}/fish/vendor_completions.d/gh.fish
%{_datadir}/zsh/site-functions/_gh
