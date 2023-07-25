%define debug_package %{nil}
# Tests don't work inside abf because they need
# connectivity to github.com
# Probably best to do a --with-tests build when
# updating though...
%bcond_with tests

Name:		github-cli
Version:	2.32.1
Release:	1
Source0:	https://github.com/cli/cli/archive/refs/tags/v%{version}.tar.gz
# Yes, go sucks...
# No concept of shared libraries, but downloading 1.3 GB worth of dependencies
# is considered perfectly "sane"...
# Dependency tarball generated using
# export GOPATH=/tmp/.godeps
# go mod download
# cd /tmp
# tar cJf godeps-for-github-cli-%{version}.tar.xz .godeps
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
export GOPATH="`pwd`/.godeps"
export GOPROXY="file://`pwd`/.godeps"
%make_build prefix=%{_prefix}

%install
export GOPATH="`pwd`/.godeps"
export GOPROXY="file://`pwd`/.godeps"
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
