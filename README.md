# Clean Up ProtonVPN connections

Utility for deleting all active ProtonVPN connections on your Linux system.

Whenever a ProtonVPN connection attempt is abruptly interrupted by the user (for example, via Ctrl-C), [network access may be inadvertently blocked](https://bbs.archlinux.org/viewtopic.php?id=267513) due to ProtonVPN's IPv6 leak protection. This utility restores network access by deleting all dangling ProtonVPN connections.

> [!WARNING]
> This script deletes all active connections with names starting with "Proton VPN", "ProtonVPN" or "pvpn-".

## Requirements

- Linux only
- Python 2.7+/3.1+

## Usage

```bash
python cleanup.py
```

## License

[The Unlicense](/LICENSE)
