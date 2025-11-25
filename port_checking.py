import socket

def is_port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    Check if a specific port on a host is open.

    :param host: The hostname or IP address to check.
    :param port: The port number to check.
    :param timeout: Timeout in seconds for the connection attempt.
    :return: True if the port is open, False otherwise.
    """
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_obj.settimeout(timeout)
    socket_result = socket_obj.connect_ex((host, port))
    socket_obj.close()
    return socket_result == 0

# Example usage
host = 'localhost'
port = [80, 443, 8080]

for p in port:
    if is_port_open(host, p):
        print(f"Port {p} on {host} is open.")
    else:
        print(f"Port {p} on {host} is closed.")