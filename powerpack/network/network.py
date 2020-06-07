import socket


def get_hostname():
    """
    Fetch the hostname of the machine
    """
    try:
        hostname = socket.gethostname()
    except:
        hostname = "Unknown"
    return hostname


def get_host():
    """
    Fetch the host of the machine
    """
    try:
        host = socket.gethostbyname(get_hostname())
    except:
        host = '-1'

    return host
