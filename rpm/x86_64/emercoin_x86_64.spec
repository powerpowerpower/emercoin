Name:           emercoin
Version:        0.7.5
Release:        1%{?dist}
Summary:        Emercoin wallet
Vendor:         emercoin
Packager:       jussi
Group:		Networking/Other
License:	GPL
URL:		https://emercoin.com
Source:		https://github.com/%{name}/%{name}/releases/download/v%{version}emc/%{name}-%{version}-%{_arch}-linux-gnu.tar.gz
BuildArch:	x86_64 
Requires:	openssl
Requires:	miniupnpc
Requires:	qt5-qtbase
Requires:	protobuf
Requires:	qrencode
Requires:	libevent >= 2.1.8

%description
Emercoin is a blockchain platform that allows the creation of software, services and solutions. 

%prep
cd %{_builddir}
rm -rf %{name}-%{version}
tar -xvvf %{_sourcedir}/%{name}-%{version}-%{_arch}-linux-gnu.tar.gz
cd %{name}-%{version}
cd %{_builddir}/%{name}-%{version}

%pre
/usr/sbin/groupadd -r emercoin >/dev/null 2>&1 || :
/usr/sbin/useradd -r -d "/usr/local/emercoin" -m -g emercoin -c "emercoin user" -s /bin/false emercoin >/dev/null || :
/usr/sbin/usermod -a -G emercoin root 

%install 
%__install -D %{_builddir}/%{name}-%{version}/bin/emercoind %{buildroot}%_bindir/emercoind
%__install -D %{_builddir}/%{name}-%{version}/bin/emercoin-qt %{buildroot}%_bindir/emercoin-qt
%__install -D %{_builddir}/%{name}-%{version}/bin/emercoin-tx %{buildroot}%_bindir/emercoin-tx
%__install -D %{_builddir}/%{name}-%{version}/bin/emercoin-cli %{buildroot}%_bindir/emercoin-cli
%__install -D %{_builddir}/%{name}-%{version}/share/man/man1/bitcoind.1 %{buildroot}%_mandir/man1/bitcoind.1
%__install -D %{_builddir}/%{name}-%{version}/share/man/man1/bitcoin-qt.1 %{buildroot}%_mandir/man1/bitcoin-qt.1
%__install -D %{_builddir}/%{name}-%{version}/share/man/man1/bitcoin-tx.1 %{buildroot}%_mandir/man1/bitcoin-tx.1
%__install -D %{_builddir}/%{name}-%{version}/share/man/man1/bitcoin-cli.1 %{buildroot}%_mandir/man1/bitcoin-cli.1
%__install -D %{_builddir}/%{name}-%{version}/include/emercoinconsensus.h %{buildroot}%_includedir/emercoinconsensus.h
%__install -D %{_builddir}/%{name}-%{version}/lib/libemercoinconsensus.so %{buildroot}%_libdir/libemercoinconsensus.so
%__install -D %{_builddir}/%{name}-%{version}/lib/libemercoinconsensus.so.0 %{buildroot}%_libdir/libemercoinconsensus.so.0
%__install -D %{_builddir}/%{name}-%{version}/lib/libemercoinconsensus.so.0.0.0 %{buildroot}%_libdir/libemercoinconsensus.so.0.0.0

%postun
/usr/sbin/groupdel -f emercoin >/dev/null 2>&1 || :
/usr/sbin/userdel -f emercoin >/dev/null 2>&1 

%files
%attr(6771,emercoin,emercoin) %_bindir/emercoin-cli
%attr(771,emercoin,emercoin) %_bindir/emercoin-qt
%attr(6771,emercoin,emercoin) %_bindir/emercoin-tx
%attr(6771,emercoin,emercoin) %_bindir/emercoind
%attr(444,emercoin,emercoin) %_includedir/emercoinconsensus.h
%_libdir/libemercoinconsensus.so
%_libdir/libemercoinconsensus.so.0
%attr(6770,emercoin,emercoin) %_libdir/libemercoinconsensus.so.0.0.0
%attr(444,emercoin,emercoin) %_mandir/man1/bitcoin-cli.1.gz
%attr(444,emercoin,emercoin) %_mandir/man1/bitcoin-qt.1.gz	
%attr(444,emercoin,emercoin) %_mandir/man1/bitcoin-tx.1.gz
%attr(444,emercoin,emercoin) %_mandir/man1/bitcoind.1.gz


%changelog
    * Wed Feb 17 2019 Emercoin (Emercoin Team) <juhanimelnikov@airmail.cc> %{_os}
- this file was created
