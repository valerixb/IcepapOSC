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

import sys
from PyQt4 import QtGui
from widgets import OscillaWindow


def main(host, port):
    app = QtGui.QApplication(sys.argv)
    oscilla_window = OscillaWindow(host, port)
    oscilla_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        print('Usage: oscilla <host> <port>')
        print('Example: oscilla w-kitslab-icepap-11 5000')
