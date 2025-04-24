# Deluge Builds

Pre-built Deluge BitTorrent client packages for various Linux distributions.

## 🎯 Features

- Pre-compiled binaries ready to use
- Multiple distribution support (Debian/Ubuntu)
- Automated builds via GitHub Actions
- JSON metadata for automated installations
- System-wide installation in `/usr/local`
- Comprehensive dependency management
- Multiple stability channels (stable, oldstable, next)
- Built using pre-compiled libtorrent-rasterbar packages

## 📦 Available Packages

Each release provides packages for different combinations of:
- Deluge versions (2.0.5, 2.1.0, 2.1.1, 2.1.2.dev0)
- libtorrent-rasterbar versions (2.0.6 through 2.0.11)
- Distributions:
  - Debian: 11 (bullseye), 12 (bookworm)
  - Ubuntu: 22.04 (jammy), latest

### Version Matrix

| Deluge Version | libtorrent Version | Distributions | Stability |
|----------------|-------------------|---------------|-----------|
| 2.0.5 | 2.0.6 | debian-11, ubuntu-22.04 | oldstable |
| 2.1.0 | 2.0.7-2.0.10 | debian-11/12, ubuntu-22.04, ubuntu-latest | oldstable |
| 2.1.1 | 2.0.11 | debian-12, ubuntu-latest | stable |
| 2.1.2.dev0 | 2.0.11 | debian-12, ubuntu-latest | next |

## 📋 Installation

### Manual Installation
1. Download the appropriate .deb package for your distribution from the [Releases](../../releases) page
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

### Package Structure
Once installed, the package places:
- Binaries in `/usr/local/bin`
- Libraries in `/usr/local/lib`
- Configuration files in `/etc/deluge`

## 🔧 Build Requirements

To build Deluge, you need:
- build-essential
- python3-dev
- libtorrent-rasterbar (automatically downloaded from MediaEase-binaries/rasterbar-builds)
- openssl
- zlib1g-dev

### Dependencies

The build process automatically:
1. Downloads the appropriate libtorrent-rasterbar packages from MediaEase-binaries/rasterbar-builds
2. Installs the required runtime, development, and Python binding packages
3. Manages all other system dependencies

### Local Building
To manually build a Deluge package:
```bash
./build.sh <VERSION>
# Example: ./build.sh 2.1.1
```

## 📄 Metadata

Each package is accompanied by its JSON metadata file containing:
- Package information
- Checksums
- Dependencies
- Build configuration
- Distribution details

## 🔍 Package Details

The packages are built with:
- Python 3 support
- System-wide installation in `/usr/local`
- Proper dependency management
- Configuration files in `/etc/deluge`
- Automated service management
- Pre-built libtorrent-rasterbar integration

## 📝 License

This repository is licensed under the terms specified in the LICENSE file.

Deluge itself is distributed under the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.html). 
