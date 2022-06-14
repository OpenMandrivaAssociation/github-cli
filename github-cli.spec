%define debug_package %{nil}

Name:		github-cli
Version:	2.11.3
Release:	1
Source0:	https://github.com/cli/cli/archive/refs/tags/v%{version}.tar.gz
# Yes, go sucks...
# No concept of shared libraries, but downloading 1.3 GB worth of dependencies
# is considered perfectly "sane"...
# Dependency tarball generated using
# export GOPATH=/tmp/.godeps
# go mod download
# cd /tmp
# tar cJf godeps-for-gitea-%{version}.tar.xz .godeps
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

%check
make test

%files
%{_bindir}/gh
%{_mandir}/man1/*.1*