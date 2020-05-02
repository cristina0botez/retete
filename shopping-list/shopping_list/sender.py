from bluetooth import find_service
from PyOBEX.client import Client


def send_contents_to_device(device_address,
                            contents,
                            target_file='shopping_list.txt'):
    service_matches = find_service(name='OBEX Object Push',
                                   address=device_address)
    if len(service_matches) == 0:
        raise NoServiceException(f"OBEX Object Push service not available for "
                                 f"device with address {device_address}.")
    first_match = service_matches[0]
    port = first_match["port"]
    name = first_match["name"]
    host = first_match["host"]
    client = Client(host, port)
    client.connect()
    try:
        client.put(target_file, contents)
    finally:
        client.disconnect()


class NoServiceException(Exception):
    pass
