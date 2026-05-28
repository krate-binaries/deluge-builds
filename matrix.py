#!/usr/bin/env python3
import yaml

BOOST_VERSION = "1.91.0"

matrix = [
    {"version": "2.1.1", "libtorrent_version": "2.0.11", "boost_version": BOOST_VERSION, "os": "debian-13", "codename": "trixie"},
    {"version": "2.2.0", "libtorrent_version": "2.0.11", "boost_version": BOOST_VERSION, "os": "debian-13", "codename": "trixie"},
]

print(yaml.safe_dump({"include": matrix}, sort_keys=False))
