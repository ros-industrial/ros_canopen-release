Name:           ros-indigo-canopen-402
Version:        0.6.3
Release:        0%{?dist}
Summary:        ROS canopen_402 package

Group:          Development/Libraries
License:        LGPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-canopen-master
Requires:       ros-indigo-class-loader
BuildRequires:  ros-indigo-canopen-master
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-class-loader

%description
This implements the CANopen device profile for drives and motion control. CiA(r)
402

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Jul 03 2015 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.6.3-0
- Autogenerated by Bloom

* Thu Dec 18 2014 Thiago de Freitas <tdf@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

