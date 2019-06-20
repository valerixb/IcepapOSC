#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# This file is part of IcepapOCS link:
#        https://github.com/ALBA-Synchrotron/IcepapOCS
#
# Copyright 2017:
#       MAX IV Laboratory, Lund, Sweden
#       CELLS / ALBA Synchrotron, Bellaterra, Spain
#
# Distributed under the terms of the GNU General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
#
# You should have received a copy of the GNU General Public License
# along with IcepapOCS. If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------


from os.path import exists
from os.path import expanduser
from ConfigParser import SafeConfigParser


class Settings:
    """Application settings."""

    def __init__(self):
        """Initializes an instance of class Settings."""
        self.conf_file = expanduser("~") + "/IcepapOSC/settings.ini"
        if not exists(self.conf_file):
            self._create_file()
        self.sample_rate_min = 10  # [milliseconds]
        self.sample_rate_max = 1000  # [milliseconds]
        self.dump_rate_min = 1
        self.dump_rate_max = 100
        self.default_x_axis_length_min = 5  # [Seconds]
        self.default_x_axis_length_max = 3600  # [Seconds]
        self.sample_rate = 0
        self.dump_rate = 0
        self.default_x_axis_len = 0
        self.data_folder = ''
        self._read_file()

    def _create_file(self):
        conf = SafeConfigParser()
        conf.add_section('collector')
        conf.add_section('gui')
        conf.add_section('data')
        conf.set('collector', 'tick_interval', '50')  # [milliseconds]
        conf.set('collector', 'sample_buf_len', '2')
        conf.set('gui', 'default_x_axis_len', '30')  # [Seconds]
        conf.set('data', 'unused', expanduser("~"))
        with open(self.conf_file, 'w') as f:
            conf.write(f)

    def update(self):
        """Called when a setting has been changed."""
        conf = SafeConfigParser()
        conf.read(self.conf_file)
        conf.set('collector', 'tick_interval', str(self.sample_rate))
        conf.set('collector', 'sample_buf_len', str(self.dump_rate))
        conf.set('gui', 'default_x_axis_len', str(self.default_x_axis_len))
        conf.set('data', 'unused', str(self.data_folder))
        with open(self.conf_file, 'w') as f:
            conf.write(f)

    def _read_file(self):
        conf = SafeConfigParser()
        conf.read(self.conf_file)
        self.sample_rate = conf.getint('collector', 'tick_interval')
        self.dump_rate = conf.getint('collector', 'sample_buf_len')
        self.default_x_axis_len = conf.getint('gui', 'default_x_axis_len')
        self.data_folder = conf.get('data', 'unused')
