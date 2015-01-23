%define majorminor   1.0
%define gstreamer    gstreamer

Name:        %{gstreamer}%{majorminor}-libav
Version:     1.4.4
Release:     1
Summary:     GStreamer Streaming-media framework plug-in using libav (FFmpeg).
License:     LGPLv2+
Group:       Applications/Multimedia
URL:         http://gstreamer.freedesktop.org/
Source:      http://gstreamer.freedesktop.org/src/gst-libav/gstreamer1.0-libav-%{version}.tar.xz
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: python
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: pkgconfig(orc-0.4) >= 0.4.18
BuildRequires: bzip2-devel
BuildRequires: pkgconfig(zlib)

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related. Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This plugin contains the libav (formerly FFmpeg) codecs, containing codecs for most popular
multimedia formats.

%prep
%setup -q -n %{name}-%{version}/gst-libav

%build
NOCONFIGURE=1 ./autogen.sh

%configure \
  --with-package-name='SailfishOS GStreamer libav Plug-ins' \
  --with-package-origin='http://jolla.com' \
  --disable-static \
  --enable-shared \
  --disable-gtk-doc \
  --enable-gtk-doc-html=no \
  --enable-gtk-doc-pdf=no \
  --enable-orc \
  --enable-lgpl \
  --with-libav-extra-configure="--disable-encoders --disable-muxers --disable-demuxers --disable-decoders --enable-decoder=aac --disable-yasm"

make %{?jobs:-j%jobs}

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-%{majorminor}/libgstlibav.so
