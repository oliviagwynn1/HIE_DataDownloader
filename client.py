import requests
import requests
from base64 import b64decode
from checksumdir import dirhash
import re
import subprocess

if __name__ == "__main__":

    device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+)"
                           ".+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    df = subprocess.check_output("system_profiler SPUSBDataType")
    devices = []
    for i in df.split('\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % \
                                  (dinfo.pop('bus'), dinfo.pop('device'))
                devices.append(dinfo)
    print(devices)
