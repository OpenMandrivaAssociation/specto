Name:		specto
Version:	0.4.1
Release:	1
Summary:	An desktop application that will watch configurable events
Group:		Networking/Other 
License:	GPLv2+
URL:		http://specto.sourceforge.net
Source0:	http://specto.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:	python-devel
BuildRequires:	intltool

Requires:	librsvg2
Requires:	%{mklibname gnome-keyring0}
Requires:	gnome-python
Requires:	gnome-python-extras
Requires:	gnome-python-gconf
Requires:	pygtk2 >= 2.10
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

%build
%{__python} setup.py build
%__rm -f data/icons/*.~?~ data/icons/scalable/*.~?~


%install
%__rm -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}

%__rm -rf %{buildroot}%{_datadir}/doc/%{name}
%__install -d %{buildroot}%{_sysconfdir}/xdg/autostart
%__cp %{buildroot}%{_datadir}/applications/%{name}.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
%__cat <<EOF >>%{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
OnlyShowIn=GNOME;
X-GNOME-Autostart-Phase=Applications
X-GNOME-Autostart-enabled=false
EOF

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%dir %{py_puresitedir}/spectlib
%{py_puresitedir}/spectlib/*.py
%dir %{py_puresitedir}/spectlib/plugins
%{py_puresitedir}/spectlib/plugins/*.py
%dir %{py_puresitedir}/spectlib/tools
%{py_puresitedir}/spectlib/tools/*.py
%{py_puresitedir}/%{name}-%{version}-py*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/indicators/messages/applications/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/uis



%changelog
* Sun May 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.1-1
+ Revision: 799740
- version update 0.4.1

* Thu Nov 04 2010 Luc Menut <lmenut@mandriva.org> 0.3.1-4mdv2011.0
+ Revision: 593471
- fix file list (.egg-info filename)
- rebuild for python 2.7
- drop %%py_requires macro
- use %%pyver macro for .egg-info file

* Tue Jun 01 2010 Luc Menut <lmenut@mandriva.org> 0.3.1-3mdv2010.1
+ Revision: 546869
- can't be noarch because of libgnome-keyring requirement

* Tue Jun 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3.1-2mdv2010.1
+ Revision: 546851
- rebuild for wrong requires in the package in i586 repo

* Sun Aug 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.3.1-1mdv2010.0
+ Revision: 422581
- change layout

  + Luc Menut <lmenut@mandriva.org>
    - import specto

