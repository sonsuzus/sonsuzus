from ppadb.client import Client as AdbClient
import sys

client = AdbClient(host="127.0.0.1", port=5037)
device = client.devices()[0]

pkg_name = sys.argv[1]
device.shell('pm uninstall -k --user 0 {}'.format(pkg_name))
device.shell('pm uninstall -k {}'.format(pkg_name))

