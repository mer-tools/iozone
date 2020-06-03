Summary: Filesystem Benchmark
Name: iozone
Version: 3.489
Release: 1
License: Freeware
URL: http://www.iozone.org
Source: %{name}-%{version}.tar.gz

%description
A filesystem benchmark tool. The benchmark generates and measures a variety of
file operations. Iozone has been ported to many machines and runs under many operating systems.

Useful for performing a broad filesystem analysis of a vendors computer
platform. The benchmark tests file I/O performance for the following
operations: Read, write, re-read, re-write, read backwards, read strided,
fread, fwrite, random read, pread ,mmap, aio_read, aio_write.

%prep

%autosetup -p1 -n %{name}-%{version}/src/current

%build
echo "Building for %{_arch} arch."
%ifarch %{ix86}
  %make_build linux
%else
  %ifarch %{arm}
    %make_build linux-arm
  %else
    %ifarch aarch64
      %make_build linux-arm
    %else
      echo "No idea how to build for your arch..."
      exit 1
    %endif
  %endif
%endif

%install
mkdir -p $RPM_BUILD_ROOT/opt/%{name}/bin
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/iozone $RPM_BUILD_ROOT/opt/%{name}/bin/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/fileop $RPM_BUILD_ROOT/opt/%{name}/bin/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/pit_server $RPM_BUILD_ROOT/opt/%{name}/bin/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/Generate_Graphs $RPM_BUILD_ROOT/opt/%{name}/bin/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/gengnuplot.sh $RPM_BUILD_ROOT/opt/%{name}/bin/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/gnu3d.dem $RPM_BUILD_ROOT/opt/%{name}/bin/

%files
%defattr(-,root,root,-)
/opt/%{name}/bin/
