# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>
import subprocess
import sys


def clean_up():
    protonvpn_connection_names = [
        connection_name
        for connection_name in (
            subprocess.check_output(
                [
                    "nmcli",
                    "-g",
                    "NAME",
                    "connection",
                    "show",
                    "--active",
                ]
            )
            .decode("utf-8")
            .splitlines()
        )
        if connection_name.startswith("Proton VPN")
        or connection_name.startswith("ProtonVPN")
        or connection_name.startswith("pvpn-")
    ]
    if not protonvpn_connection_names:
        sys.stderr.write("Operation aborted. No Proton VPN connection names found.\n")
        return

    for connection_name in protonvpn_connection_names:
        sys.stderr.write("%s\n" % connection_name)
    sys.stderr.write(
        "Delete the above %d connection%s? (y/N) "
        % (
            len(protonvpn_connection_names),
            "s" if len(protonvpn_connection_names) > 1 else "",
        )
    )

    response = input().strip().lower()
    if response != "y":
        sys.stderr.write("Operation aborted by user. No connections deleted.\n")
        return

    for connection_name in protonvpn_connection_names:
        try:
            subprocess.check_output(["nmcli", "connection", "delete", connection_name])
        except subprocess.CalledProcessError:
            sys.stderr.write("Failed to delete connection '%s'\n" % connection_name)
        else:
            sys.stdout.write("Deleted connection '%s'\n" % connection_name)


if __name__ == "__main__":
    clean_up()
