# G203 Prodigy Driver
A application to change the colors on a Logitech G203 Prodigy Gaming Mouse.

## Supported devices

* G203 mouse

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
You can call the `main.py` script like this:

```Bash
python main.py
```

G203 Prodigy Driver needs to be run as root as long as long as your user doesn't have access privileges for the USB device.
In order to run the program without root privileges you have to create a [udev rule](https://wiki.archlinux.org/index.php/udev#About_udev_rules) for your device and add your user to the plugdev group. See [how this is done on stackexchange](https://stackoverflow.com/a/48477830/7809404). `idVendor` is *046d* for Logitech. `idProduct` depends on your device. Use `lsusb | grep Logitech` to determine the Id.

### Restoring previous state
After rebooting your pc you can restore the pre-reboot state by running the app with parameter -t

```Bash
sudo g203-driver.py -t
```

## Known issues


## ToDo


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

Changelog v0.5:
* Finally fixed incontrollable segments bug (with the help of [Oncecreated](https://github.com/oncecreated))
