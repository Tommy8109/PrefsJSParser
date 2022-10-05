"""

The prefs.js file stores some basic browser settings and
preferences.
It is a text file automatically written to by the user’s actions in the
browser’s GUI.

"""

import datetime
import re
import linecache


class PrefParse():
    def __init__(self):
        self.path_to_file = ""
        self.pref_data = {}
        self.pref_data_formatted = {}
        self.pref_lines = {12: "Install date", 41: "Download directory", 77: "Homepage URL", 123: "Device name",
                           195: "Desktops synced", 196: "Mobiles synced", 205: "Sync bookmarks?",
                           206: "Sync credit cards?", 207: "Sync history?", 208: "Sync passwords?", 209: "prefs",
                           211: "Sync tabs?", 219: "Last sync", 227: "Username"}

    def get_prefJS(self):
        while True:
            self.path_to_file = input("Path to Pref.js file: ")
            try:
                open(self.path_to_file)
                self.parser()
                break

            except FileNotFoundError:
                print(f"{self.path_to_file} could not be found...")

    def parser(self):
        for key, val in self.pref_lines.items():
            line = linecache.getline(self.path_to_file, key)
            self.pref_data.update({val: line})

        for key, val in self.pref_data.items():
            new_val = str(val).split(",")[1]
            regex = re.compile("[^a-zA-Z0-9\+:\\ ’\/\.@]")
            m = regex.sub("", new_val)
            self.pref_data_formatted.update({key: m})

        for key, val in self.pref_data_formatted.items():
            if val == "true":
                self.pref_data_formatted.update({key: "No"})
            elif val == "false":
                self.pref_data_formatted.update({key: "Yes"})

        print("Pref.js values:\n---------------")
        for key, val in self.pref_data_formatted.items():
            print(f"{key} - {val}")


c = PrefParse()
c.get_prefJS()
