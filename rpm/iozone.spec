Summary: Filesystem Benchmark
Name: iozone
Version: 3.489
Release: 1
License: Freeware
URL: http://www.iozone.org
Group: Applications/Engineering
Source: %{name}-%{version}.tar.gz

%description
A filesystem benchmark tool. The benchmark generates and measures a variety of
file operations. Iozone has been ported to many machines and runs under many operating systems.

Useful for performing a broad filesystem analysis of a vendors computer
platform. The benchmark tests file I/O performance for the following
operations: Read, write, re-read, re-write, read backwards, read strided,
fread, fwrite, random read, pread ,mmap, aio_read, aio_write.

%prep

%setup -q -n %{name}-%{version}/src/current

%build
%ifarch %{ix86}
    make linux
%else
    %ifarch x86_64
        make linux-AMD64
    %else
        %ifarch ia64
            make linux-ia64
        %else
            %ifarch ppc
                make  linux-powerpc
            %else
                %ifarch ppc64
                    make linux-powerpc64
                %else
                    %ifarch s390
                        make linux-S390
                    %else
                        %ifarch s390x
                            make linux-S390X
                    	%else
                           %ifarch %{arm}
                               make linux-arm
			   %else
			      echo "No idea how to build for your arch..."
			      exit 1
			   %endif
                        %endif
                    %endif
                %endif
            %endif
        %endif
    %endif
%endif

%install
mkdir -p $RPM_BUILD_ROOT/opt/iozone/bin
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/iozone $RPM_BUILD_ROOT/opt/iozone/bin/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/fileop $RPM_BUILD_ROOT/opt/iozone/bin/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/pit_server $RPM_BUILD_ROOT/opt/iozone/bin/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/Generate_Graphs $RPM_BUILD_ROOT/opt/iozone/bin/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/gengnuplot.sh $RPM_BUILD_ROOT/opt/iozone/bin/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/current/gnu3d.dem $RPM_BUILD_ROOT/opt/iozone/bin/

mkdir -p $RPM_BUILD_ROOT/opt/iozone/man/man1
cp $RPM_BUILD_DIR/%{name}-%{version}/docs/iozone.1 $RPM_BUILD_ROOT/opt/iozone/man/man1/

%files
%defattr(-,root,root,-)
/opt/%{name}/bin/
%doc /opt/%{name}/man/
