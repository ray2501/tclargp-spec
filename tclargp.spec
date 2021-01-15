#
# spec file for package tclargp
#

Name:           tclargp
BuildRequires:  tcl >= 8.4
Requires:       tcl >= 8.4
License:        TCL
Group:          Development/Libraries/Tcl
Version:        0.2
Release:        0
Summary:        Using and parsing optional arguments in tcl procs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            http://www.bawt.tcl3d.org/download.html
Source0:        %{name}-%{version}.tar.gz

%description
The argp package allows simple and flexible 
 - using and parsing optional arguments in tcl procs (like arguments
   given to Tk widgets)
 - using and parsing commandline arguments given to a tcl script

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %buildroot%tcl_noarchdir/%{name}%{version}
cp pkgIndex.tcl %buildroot%tcl_noarchdir/%{name}%{version}
cp argp.tcl %buildroot%tcl_noarchdir/%{name}%{version}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc doc demos README.license README.txt
%tcl_noarchdir

