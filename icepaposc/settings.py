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


class Settings:
    """Application settings."""

    def __init__(self, gui, collector):
        """Initializes an instance of class Settings."""

        # Settings held by the collector side.
        self.gui = gui
        self.collector = collector
        self.sample_rate_min = collector.tick_interval_min
        self.sample_rate_max = collector.tick_interval_max
        self.sample_rate = collector.tick_interval
        self.dump_rate_min = collector.sample_buf_len_min
        self.dump_rate_max = collector.sample_buf_len_max
        self.dump_rate = collector.sample_buf_len

        # Settings held by the GUI side.
        self.default_x_axis_length_min = 5  # [Seconds]
        self.default_x_axis_length_max = 3600  # [Seconds]
        self.default_x_axis_length = 30  # [Seconds]

    def announce_update(self):
        self.collector.tick_interval = self.sample_rate
        self.collector.sample_buf_len = self.dump_rate
        self.gui.settings_updated()

    def reactivate_gui_settings_action(self):
        self.gui.enable_action_settings()
