Name:		specto
Version:	0.3.1
Release:	%mkrel 1
Summary:	An desktop application that will watch configurable events
Group:		Networking/Other 
License:	GPLv2+
URL:		http://specto.sourceforge.net/
Source0:	http://specto.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%py_requires -d

Requires:	bzr
Requires:	librsvg2
Requires:	%{mklibname gnome-keyring0}
Requires:	gnome-python
Requires:	gnome-python-extras
Requires:	gnome-python-gconf
Requires:	pygtk2 >= 2.10
Requires:	pygtk2.0-libglade
Requires:	python-numpy
Requires:	python-libxml2
Requires:	python-dbus
Requires:	python-notify
Requires:	xdg-utils


%description

Specto is a desktop application that will watch configurable events 
(such as website updates, emails, file and folder changes, 
system processes, etc) and then trigger notifications.

Specto can watch a website for updates (or a syndication feed, 
or an image, etc), and notify you when there is activity 
(otherwise, Specto will just stay out of the way).
This changes the way you work, because you can be informed 
of events instead of having to look out for them.

%prep
%setup -q

%install
%__rm -rf %{buildroot}
%{__python} setup.py install --root %{buildroot} --no-compile

%__mv data/doc/{AUTHORS,ChangeLog,VERSION,COPYING} .
%__rm -rf %{buildroot}%{_datadir}/doc/%{name}
%__install -d %{buildroot}%{_sysconfdir}/xdg/autostart
%__cp %{buildroot}%{_datadir}/applications/%{name}.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
%__cat <<EOF >>%{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
OnlyShowIn=GNOME;
X-GNOME-Autostart-Phase=Applications
X-GNOME-Autostart-enabled=false
EOF

%find_lang %{name}


%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog VERSION
%{_bindir}/%{name}
%dir %{py_puresitedir}/spectlib
%{py_puresitedir}/spectlib/*.py
%dir %{py_puresitedir}/spectlib/plugins
%{py_puresitedir}/spectlib/plugins/*.py
%dir %{py_puresitedir}/spectlib/tools
%{py_puresitedir}/spectlib/tools/*.py
%{py_puresitedir}/%{name}-*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade
%{_datadir}/%{name}/icons

