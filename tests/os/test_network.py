import powerpack


def test_get_hostname():
    hostname = powerpack.get_hostname()
    assert isinstance(hostname, str)


def test_get_host():
    host = powerpack.get_host()
    assert isinstance(host, str)
    assert len(host.split('.')) == 4


def test_is_port_available():
    avai = powerpack.is_port_available(80)
    assert avai == True
