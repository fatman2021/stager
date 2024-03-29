#! /usr/bin/env python3

# Stage7 - The perfect Gentoo installer
# Copyright (C) 2015, Matthew Marchese
# License coming soon...

# Todo: check for python2 and python3.

# Define global variables
__author__ = 'matthew marchese'
__copyright__ = '2015'  # Enter a span of years
__credits__ = 'people who have helped.'

__license__ = 'coming soon...'
__version__ = '0.0.01'
__status__= 'pre-alpha'

__maintainer__ = 'matthew marchese'
__email__ = 'maffblaster@gentoo.org'

__url__ = 'https://wiki.gentoo.org/wiki/Project:Installer'
__source__ = 'https://github.com/gentoo/stager'

# 0 verbosity: normal output to stdout
# 1 verbosity: be chatty (extra output) (--verbose)
# -1 verbosity: no normal output to stdout (--quiet)
verbosity = 0

import argparse

# Imports all stage7 modules in the modules directory
import modules

# todo Usage: stager --[global-options] subcommand [--subcommand-options <subcommand-arguments>]

parser = argparse.ArgumentParser(prog='stager', add_help=True, formatter_class=argparse.RawDescriptionHelpFormatter, description='stager: the perfect Gentoo installer.',
                                 epilog='\nsubcommands can be abbreviated if not ambiguous:\n\'stager install -h\' can be reduced to \'stager i -h\'\n\nversion ' + __version__ + ' ' + __status__ + '\n'
                                 'copyright (c) ' + __copyright__ + ', ' + __author__ + '\n' + __url__ + '\n' + __source__)
# They are global options, not arguments
for grp in parser._action_groups:
    if grp.title == 'optional arguments':
        grp.title = 'global-options'

parser.add_argument('-V', '--version', action='version', help='print version information and exit.', version=__version__)
parser.add_argument('-v', '--verbose', action='store_true', default=False, help='be chatty: more data to stdout.')
parser.add_argument('-q', '--quiet', action='store_true', default=False, help='be silent: no data to stdout.')

subparser = parser.add_subparsers(title='subcommands', description='', help='type \'stager subcommand --help\' for a list of subcommmand-specific options.')

# Create a parser for the install command
parser_install = subparser.add_parser('install', help='install a new system from a profile.')
parser_install.add_argument('-l', '--logfile', dest='<logfile>', action='store', default='/tmp/install.log', help='path to the log file (defaults to /tmp/install.log)')
parser_install.add_argument('-p', '--profile', dest='<profile>', action='store', help='path the profile.ini file.')

# Create a parser for the backup command
parser_backup = subparser.add_parser('backup', help='create a complete backup of the system.')
parser_backup.add_argument('-c', '--compression-type', dest='COMP_TYPE', choices=['gz', 'bz2', 'xz', 'lzma'], help='select a compression type.')
parser_backup.add_argument('-d', '--destination', dest='', action='store', help='path to the backup destination.')
parser_backup.add_argument('-e', '--exclude', dest='', action='append', help='exclude the following files/directories.')
parser_backup.add_argument('--exclude-list', dest='<exclude.txt>', action='store', help='path to a new line separated text file containing a list of files/directories to exclude.')
parser_backup.add_argument('-n', '--no-compress', dest='extensions', help='do not compress files with the these extensions.')

# Create a parser for the recovery command
parser_recover = subparser.add_parser('recover', help='recover a system from a stage4 tarball.')
parser_recover.add_argument('-d', '--destination', dest='', action='store', help='path to the recovery destination.')
parser_recover.add_argument('-p', '--profile', dest='<profile.ini>', action='store', help='path the profile.ini file.')
parser_recover.add_argument('-s', '--source', dest='', action='store', help='source of the tarball.')

# Create a parser for the serve command
parser_serve = subparser.add_parser('serve', help='start the http ui.')
parser_serve.add_argument('-l', '--logfile', dest='<logfile>', action='store', default='/tmp/install.log', help='path to the log file (defaults to /tmp/install.log)')
parser_serve.add_argument('-P', '--password', action='store', help='sets a password for the http interface.')
parser_serve.add_argument('-p', '--profile', dest='<profile>', action='store', help='populates the http UI with profile.ini data.')
parser_serve.add_argument('--port', action='store', default='80', help='sets the port for the http interface (defaults to 80).')
parser_serve.add_argument('--url', action='store', default='http://localhost/stager', help='sets the url for the http interface (defaults to http://localhost/stager).')

args = parser.parse_args()

parser.parse_args('-h'.split())

#todo option/argument santity tests
