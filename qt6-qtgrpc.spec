#define beta rc
#define snapshot 20200627
%define major 6

%define _qtdir %{_libdir}/qt%{major}

Name:		qt6-qtgrpc
Version:	6.9.1
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qtgrpc-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtgrpc-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Group:		System/Libraries
Summary:	Qt %{major} GRPC module
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	%{_lib}Qt%{major}Core-devel
BuildRequires:	%{_lib}Qt%{major}Gui-devel
BuildRequires:	%{_lib}Qt%{major}Network-devel
BuildRequires:	%{_lib}Qt%{major}Xml-devel
BuildRequires:	%{_lib}Qt%{major}Widgets-devel
BuildRequires:	%{_lib}Qt%{major}SerialPort-devel = %{version}
BuildRequires:	%{_lib}Qt%{major}Sql-devel
BuildRequires:	%{_lib}Qt%{major}Positioning-devel
BuildRequires:	%{_lib}Qt%{major}PositioningQuick-devel
BuildRequires:	%{_lib}Qt%{major}PrintSupport-devel
BuildRequires:	%{_lib}Qt%{major}OpenGL-devel
BuildRequires:	%{_lib}Qt%{major}OpenGLWidgets-devel
BuildRequires:	%{_lib}Qt%{major}DBus-devel
BuildRequires:	qt%{major}-cmake
BuildRequires:	cmake(Qt%{major})
BuildRequires:	cmake(Qt%{major}Quick)
BuildRequires:	cmake(Qt%{major}Qml)
BuildRequires:	cmake(Qt%{major}QmlCore)
BuildRequires:	cmake(Qt%{major}QmlNetwork)
BuildRequires:	cmake(Qt%{major}QmlNetworkplugin)
BuildRequires:	cmake(Qt%{major}QmlModels)
BuildRequires:	cmake(Qt%{major}Test)
BuildRequires:	cmake(Qt%{major}QuickTest)
BuildRequires:	cmake(Qt%{major}QuickShapesPrivate)
BuildRequires:	cmake(Qt%{major}QuickControls2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(gypsy)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(geoclue-2.0)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	pkgconfig(grpc)
BuildRequires:	pkgconfig(libcares)
BuildRequires:	cmake(LLVM)
BuildRequires:	cmake(Clang)
BuildRequires:	cmake(c-ares)
BuildRequires:	%{_lib}gpuruntime
License:	LGPLv3/GPLv3/GPLv2

%patchlist

%description
Qt %{major} GRPC module

%define extra_files_ProtobufQuick \
%{_qtdir}/qml/QtProtobuf

%define extra_devel_files_ProtobufQuick \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6protobufquickplugin*

%define extra_devel_files_Grpc \
%{_qtdir}/libexec/qtgrpcgen \
%{_qtdir}/sbom/*

%define extra_devel_files_Protobuf \
%{_qtdir}/lib/cmake/Qt6/FindWrapProto*.cmake \
%{_qtdir}/libexec/qtprotobufgen

%define extra_files_GrpcQuick \
%{_qtdir}/qml/QtGrpc

%define extra_devel_files_GrpcQuick \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6grpcquickplugin*

%qt6libs Grpc GrpcQuick Protobuf ProtobufQtCoreTypes ProtobufQtGuiTypes ProtobufWellKnownTypes ProtobufQuick

%package examples
Summary:	Example code demonstrating the use of %{name}
Group:		Development/KDE and Qt

%description examples
Example code demonstrating the use of %{name}

%files examples
%{_qtdir}/examples/grpc
%{_qtdir}/examples/protobuf

%prep
%autosetup -p1 -n qtgrpc%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_WILL_INSTALL:BOOL=ON

%build
%ninja_build -C build

%install
%ninja_install -C build
%qt6_postinstall
