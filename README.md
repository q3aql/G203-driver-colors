# G213Colors
A application to change the key colors on a Logitech G213 Prodigy Gaming Keyboard using [SebiTimeWaster](https://github.com/SebiTimeWaster)'s [G213Colors](https://github.com/SebiTimeWaster/G213Colors).

## Supported devices

* G213 keyboard
* G203 mouse

## What it does
G213Colors lets you set the color(s) and certain effects of the illuminated keys on a G213 keyboard and G203 mouse under Linux.

Since Logitech is mostly ignoring the Linux market with their "Logitech Gaming Software" but i also wanted to use my expensive new keyboard also under linux without tolerating the color cycling animation all the time. So i searched on the internet and added a gui to [SebiTimeWaster's project](https://github.com/SebiTimeWaster/G213Colors) for comfortable usage.

G213Colors was built and tested under Linux for the G213 keyboard and G203 mouse specifically, but after some adaptation it could potentially be run under other OS'es and used for other Logitech devices as well.

If you have any Logitech keyboard or mouse that is not supported feel free to open an issue and/or contact me via Email: git(AT)eiselecloud(DOT)de

The "Wave" color effect that is available with the Logitech software could not be replicated since it is completely generated in the software by updating the colors every x ms (In contrast to the other effects which run on the keyboard itself). You could generate this effect with a script, but since G213Colors has to detach the kernel driver from one of the G213's interfaces to send data out the multimedia keys would most likely stop working. Unfortunately this is a side effect of the linux driver structure.

## Installation
Clone this project with git and run `sudo make install`

### Prerequisites
* [Python](https://www.python.org/) 3.x (which is usually already installed)
* [PyUSB](https://github.com/walac/pyusb) (please see their instructions on how to install)
* [PyGObject](https://wiki.gnome.org/action/show/Projects/PyGObject)

Please ignore the pcap directory, [SebiTimeWaster](https://github.com/SebiTimeWaster) added the pcap files he used for reverse engineering just in case someone wants to work with them. They can be opened with [Wireshark](https://en.wikipedia.org/wiki/Wireshark).

## Usage

### Automatic
You can find the app in your menu after installation.

### Manually
Just call the main.py script:

```Bash
sudo python main.py
```
G213Colors needs to be run as root as long as your user doesn't have access privileges for that USB device ([How to do this](http://stackoverflow.com/a/32022908/2948666), please use "046d" as idVendor and "c336" as idProduct).

### Restoring previous state
After rebooting your pc you can restore the pre-reboot state by running the app with parameter -t

```Bash
sudo g213colors-gui -t
```

You can also do this automatically at reboot by enabling the systemd service.

```Bash
sudo systemctl enable g213colors.service
```

## Known issues
* Field 4 and 5 are not controllable in segments mode
* Restoring segments mode setting does not work

## ToDo
* fix issues :D

## Changelog
Changelog v0.1:
* Initial checkin

Changelog v0.2:
* Added segments/field support
* removed color button events

Changelog v0.3:
* Added more intergration with linux systems (by [JeroenED](https://github.com/JeroenED))

Changelog v0.4:
* Added support for G203 mouse
