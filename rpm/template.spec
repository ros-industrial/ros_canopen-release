%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-canopen-chain-node
Version:        0.8.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS canopen_chain_node package

License:        LGPLv3
URL:            http://wiki.ros.org/canopen_chain_node
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-canopen-master
Requires:       ros-noetic-diagnostic-updater
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-rosconsole-bridge
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-roslib
Requires:       ros-noetic-socketcan-interface
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-std-srvs
BuildRequires:  ros-noetic-canopen-master
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-diagnostic-updater
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-rosconsole-bridge
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslib
BuildRequires:  ros-noetic-socketcan-interface
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-std-srvs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Base implementation for CANopen chains node with support for management services
and diagnostics

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Sat Aug 22 2020 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.8.4-1
- Autogenerated by Bloom

* Thu May 07 2020 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.8.3-1
- Autogenerated by Bloom

