from core.scanner import WiFiScanner

scanner = WiFiScanner()

networks = scanner.scan()

print("\nNearby WiFi Networks\n")

for net in networks:
    print(net)