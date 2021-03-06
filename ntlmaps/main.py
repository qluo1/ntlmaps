#! /bin/env python

# This file is part of 'NTLM Authorization Proxy Server'
# Copyright 2001 Dmitry A. Rozmanov <dima@xenon.spb.ru>
# Copyright 2012 Tony Heupel <tony@heupel.net>
#
# NTLM APS is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# NTLM APS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the sofware; see the file COPYING. If not, write to the
# Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#

import os
import sys
import logging
import logging.config

# project
import server
import config
import config_affairs
import command_line

cur_dir = os.path.dirname(os.path.abspath(__file__))

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(module)s:%(lineno)d %(process)d %(threadName)s %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "logfile": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(cur_dir, "..", "ntlmaps.log"),
            "level": LOG_LEVEL,
            "when": "midnight",
            "interval": 1,
            "backupCount": 0,
            "delay": True,
            "formatter": "verbose",
        },
        "console": {
            "level": "WARN",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "": {"handlers": ["logfile", "console"], "level": "DEBUG", "propagate": True}
    },
}
# setup logging
logging.config.dictConfig(LOGGING)


def override_config_with_command_line_options(conf, options):
    if "port" in options:
        conf["GENERAL"]["LISTEN_PORT"] = options["port"]

    if "username" in options:
        conf["NTLM_AUTH"]["USER"] = options["username"]
        # if you are setting a username, then you don't want
        # to use basic auth as NTLM username/password, so
        # force it off
        conf["NTLM_AUTH"]["NTLM_TO_BASIC"] = 0

    if "password" in options:
        conf["NTLM_AUTH"]["PASSWORD"] = options["password"]

    if "domain" in options:
        conf["NTLM_AUTH"]["NT_DOMAIN"] = options["domain"]


def get_config_filename(options):
    # default
    config_file = cur_dir + "/server.cfg"
    print(options)
    if "config_file" in options and options["config_file"] != "":
        config_file = options["config_file"]

    print("config: %s" % config_file)
    if not os.path.exists(config_file):
        raise ValueError("config_file not found: {}".format(config_file))

    return config_file


# --------------------------------------------------------------
# config affairs
# look for default config name in lib/config.py
args = sys.argv
args = args[1:]

options = command_line.parse_command_line(args)

conf = config.read_config(get_config_filename(options))

override_config_with_command_line_options(conf, options)

conf["GENERAL"]["VERSION"] = "0.9.9.0.2"

print(("NTLM authorization Proxy Server v%s" % conf["GENERAL"]["VERSION"]))
print("Copyright (C) 2001-2012 by Tony Heupel, Dmitry Rozmanov, and others.")

config = config_affairs.arrange(conf)

# --------------------------------------------------------------
# let's run it
serv = server.AuthProxyServer(config)
serv.run()
