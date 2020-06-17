import click
import omnipack

# -------- process -------- #


@click.command(help='Kill process with the same command')
@click.argument('cmd')
def kill_multiprocess(cmd):
    omnipack.kill_multiprocess(cmd)


@click.command(help='Kill process with pid')
@click.argument('pid')
def kill_process(pid):
    omnipack.kill_process(pid)


# -------- network -------- #

@click.command(help='Kill port connection')
@click.argument('port')
def kill_port(port):
    omnipack.kill_port(port)


@click.command(help='Check port availability')
@click.argument('port')
def is_port_available(port):
    avai = omnipack.is_port_available(port)
    print(avai)


@click.command(help='Get host of the machine')
def get_host():
    host = omnipack.get_host()
    print(host)


@click.command(help='Get hostname')
def get_hostname():
    hostname = omnipack.get_hostname()
    print(hostname)
