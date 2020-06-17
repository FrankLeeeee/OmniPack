import omnipack
import pytest


def test_get_hostname():
    hostname = omnipack.get_hostname()
    assert isinstance(hostname, str)


def test_get_host():
    host = omnipack.get_host()
    assert isinstance(host, str)
    assert len(host.split('.')) == 4


def test_is_port_available():
    avai = omnipack.is_port_available(8000)
    assert avai == True
