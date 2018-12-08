import usb
import os


def find_devices():
    busses = usb.busses()
    for bus in busses:
        devices = bus.devices
        for dev in devices:
            print("Device:", dev.filename)
            print("  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor))
            print("  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct))
            print("Manufacturer:", dev.iManufacturer)
            print("Serial:", dev.iSerialNumber)
            print("Product:", dev.iProduct)
    return


def get_info():
    dev = usb.core.find(idVendor=0x0425, idProduct=0x03fc)
    if dev is None:
        print('Our device is not connected')
    else:
        if dev._manufacturer is None:
            dev._manufacturer = usb.util.get_string(dev, dev.iManufacturer)
        print(str(dev._manufacturer))
        if dev._product is None:
            dev._product = usb.util.get_string(dev, dev.iProduct)
        print(str(dev._product))
    return


def find_num_files(dir):
    num_files = 0
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in [f for f in filenames if f.endswith(".BIN")]:
            # print(os.path.join(dirpath, filename))
            num_files += 1
    print(num_files)
    return


if __name__ == "__main__":
    # find_devices()
    get_info()
    dir = '/Volumes/MV1'
    find_num_files(dir)
