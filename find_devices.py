import usb


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
    dev = usb.core.find(idVendor=0x05dc, idProduct=0xa81d)  # fill in your own device, of course
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


if __name__ == "__main__":
    find_devices()
    get_info()