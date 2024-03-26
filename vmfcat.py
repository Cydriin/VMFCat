<<<<<<< HEAD
=======
#!/usr/bin/env python
>>>>>>> 933a3d67a02755010a5deb0093354e910846c0fe
# Copyright (C) 2015 Jonathan Racicot
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http:#www.gnu.org/licenses/>.
# </copyright>
# <author>Jonathan Racicot</author>
# <email>infectedpacket@gmail.com</email>
# <date>2015-08-10</date>
# <url>https://github.com/infectedpacket</url>
# <summary>Python script skeleton.</summary>
<<<<<<< HEAD
# //////////////////////////////////////////////////////////

# //////////////////////////////////////////////////////////
# Program Information

from UI import *
=======
#//////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////
# Program Information
#
>>>>>>> 933a3d67a02755010a5deb0093354e910846c0fe
PROGRAM_NAME = "vmfcat"
PROGRAM_DESC = ""
PROGRAM_USAGE = "%(prog)s [-i] [-h|--help] (OPTIONS)"

<<<<<<< HEAD
__version_info__ = ('0', '1', '0')
__version__ = '.'.join(__version_info__)

# //////////////////////////////////////////////////////////

# //////////////////////////////////////////////////////////
# Imports Statements
# //////////////////////////////////////////////////////////

=======
__version_info__ = ('0','1','0')
__version__ = '.'.join(__version_info__)

#//////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////
# Imports Statements
from UI import *
#//////////////////////////////////////////////////////////
>>>>>>> 933a3d67a02755010a5deb0093354e910846c0fe

def banner():
    print("Copyright (C) 2015  Jonathan Racicot <jonathan.racicot@rmc.ca>")
    print(
<<<<<<< HEAD
        """
    This program comes with ABSOLUTELY NO WARRANTY. This is
    free software, and you are welcome to redistribute it
    under certain conditions. See the GNU General Public
    License v3 for more information.
=======
    """
    This program comes with ABSOLUTELY NO WARRANTY. This is
    free software, and you are welcome to redistribute it
    under certain conditions. See the GNU General Public
    License v3 for more information. 
>>>>>>> 933a3d67a02755010a5deb0093354e910846c0fe
    """)


def main(args):
<<<<<<< HEAD
    if (args.interactive):
        shell = VmfShell()
        shell.start()
    else:
        # TODO manage command shell creation
        pass


if __name__ == "__main__":
    banner()
    main(parser.parse_args(namespace=Params))
=======
	if (args.interactive):
		shell = VmfShell()
		shell.start()
	else:
		#TODO manage command shell creation
		pass
if __name__ == "__main__":
	banner()
	main(parser.parse_args(namespace=Params))
>>>>>>> 933a3d67a02755010a5deb0093354e910846c0fe
