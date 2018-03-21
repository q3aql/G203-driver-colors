install :
	cp main.py /usr/bin/g203-driver.py
	cp g203module.py /usr/bin/g203module.py
	chmod +x /usr/bin/g203-driver.py
	cp icons/G203Colors-16.png /usr/share/icons/hicolor/16x16/apps/g203colors.png
	cp icons/G203Colors-24.png /usr/share/icons/hicolor/24x24/apps/g203colors.png
	cp icons/G203Colors-32.png /usr/share/icons/hicolor/32x32/apps/g203colors.png
	cp icons/G203Colors-48.png /usr/share/icons/hicolor/48x48/apps/g203colors.png
	cp icons/G203Colors-128.png /usr/share/icons/hicolor/128x128/apps/g203colors.png
	cp icons/G203Colors-192.png /usr/share/icons/hicolor/192x192/apps/g203colors.png
	cp g203-driver.desktop /usr/share/applications/g203-driver.desktop
	gtk-update-icon-cache -q /usr/share/icons/hicolor/
	systemctl daemon-reload
uninstall :
	rm /usr/bin/g203-driver.py
	rm /usr/bin/g203module.py
	rm /usr/share/icons/hicolor/16x16/apps/g203colors.png
	rm /usr/share/icons/hicolor/24x24/apps/g203colors.png
	rm /usr/share/icons/hicolor/32x32/apps/g203colors.png
	rm /usr/share/icons/hicolor/48x48/apps/g203colors.png
	rm /usr/share/icons/hicolor/128x128/apps/g203colors.png
	rm /usr/share/icons/hicolor/192x192/apps/g203colors.png
	rm /usr/share/applications/g203-driver.desktop
	gtk-update-icon-cache -q /usr/share/icons/hicolor/
	systemctl daemon-reload
