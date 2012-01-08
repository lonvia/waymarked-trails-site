#!/usr/bin/python
# This file is part of Lonvia's Route Maps Project
# Copyright (C) 2011 Sarah Hoffmann
#
# This is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

# common settings for all route maps
from routemap.common.settings import *
from routemap.common.settings import _BASEDIR

# Django settings for MTB map project.
_ = lambda s : s

SECRET_KEY = 'pfy1^7!))-#!ft5_is)5**zn7n$m_hdwa!6ex7)44=r!zxiu4k'
ROOT_URLCONF = 'routemap.mtbmap.urls'

# Project settings
ROUTEMAP_PAGEINFO = {
    "maptopic" : _("MTB"),
    "cssfile" : "mtb_theme.css",
    "bgimage" : "banner_mtb.jpg",
    "iconimg" : "map_mtb.ico"
}

ROUTEMAP_MAX_ROUTES_IN_LIST = 30
ROUTEMAP_SOURCE_SYMBOL_PATH = _BASEDIR + '../static/img/symbols'
ROUTEMAP_COMPILED_SYMBOL_PATH = 'mtbsyms'
ROUTEMAP_UPDATE_TIMESTAMP = _BASEDIR + '/../last_update'
