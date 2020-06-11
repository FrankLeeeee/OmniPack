from .network import kill_port_connection, get_host, get_hostname
from .process import kill_multiprocess, kill_process

__all__ = ['kill_port_connection', 'get_host', 'get_hostname',
           'kill_multiprocess', 'kill_process']
