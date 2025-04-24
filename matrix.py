#!/usr/bin/env python3
import itertools
import yaml

matrix = []

def add(version, libtorrent_versions, oses, stability):
    """Add build combinations to the matrix.
    
    Args:
        version (str): Deluge version
        libtorrent_versions (list): List of compatible libtorrent versions
        oses (list): List of target operating systems (must match libtorrent-rasterbar-builds releases)
        stability (str): Stability level (stable, oldstable, next)
    """
    # Map OS names to their release names as used in libtorrent-rasterbar-builds
    os_map = {
        "debian-11": "debian-bullseye",
        "debian-12": "debian-bookworm",
        "ubuntu-22.04": "ubuntu-jammy",
        "ubuntu-24.04": "ubuntu-noble",
    }
    
    for lt, os in itertools.product(libtorrent_versions, oses):
        matrix.append({
            "version": version,
            "libtorrent_version": lt,
            "stability": stability,
            "os": os,
            "libtorrent_os": os_map[os]
        })

# Deluge 2.0.5 - Compatible with libtorrent 2.0.6
# Targets: debian-11 (bullseye), ubuntu-22.04 (jammy)
add("2.0.5", ["2.0.6"], ["debian-11", "ubuntu-22.04"], "oldstable")

# Deluge 2.1.0 - Compatible with libtorrent 2.0.7 through 2.0.10
# Targets: debian-11/12, ubuntu-22.04/24.04
add("2.1.0", 
    ["2.0.7", "2.0.8", "2.0.9", "2.0.10"],
    ["debian-11", "debian-12", "ubuntu-22.04", "ubuntu-24.04"],
    "oldstable")

# Deluge 2.1.1 - Compatible with libtorrent 2.0.11
# Targets: debian-12, ubuntu-24.04
add("2.1.1", 
    ["2.0.11"],
    ["debian-12", "ubuntu-24.04"],
    "stable")

# Deluge 2.1.2.dev0 (development version) - Compatible with libtorrent 2.0.11
# Targets: debian-12, ubuntu-24.04
add("2.1.2.dev0", 
    ["2.0.11"],
    ["debian-12", "ubuntu-24.04"],
    "next")

# Output the matrix in GitHub Actions compatible format
print(yaml.safe_dump({ "include": matrix }, sort_keys=False))
