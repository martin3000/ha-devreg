# ha-devreg

This program reads the device registry of home assistant and creates 2 csvs files, one for the device registry and one for a list of device models. The csv files can be opened in a spreadsheet program (libreoffice calc). The extraction is done on device level, not on entity level.
Note that it must be run from the home directory of home assistant. Or you can change the path in the "open" functions to point to the correct directory.
