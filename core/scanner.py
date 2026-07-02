import pywifi
from pywifi import const
import time


class WiFiScanner:

    def __init__(self):
        self.wifi = pywifi.PyWiFi()

        interfaces = self.wifi.interfaces()

        if len(interfaces) == 0:
            raise Exception("No WiFi adapter found!")

        self.iface = interfaces[0]

    def scan(self):
        self.iface.scan()

        time.sleep(3)

        results = self.iface.scan_results()

        networks = []

        for network in results:

            security = "Open"

            if network.akm:
                if const.AKM_TYPE_WPA2PSK in network.akm:
                    security = "WPA2"

                elif const.AKM_TYPE_WPAPSK in network.akm:
                    security = "WPA"

                else:
                    security = "Secured"

            networks.append({
                "ssid": network.ssid,
                "signal": network.signal,
                "channel": network.freq,
                "security": security
            })

        return networks