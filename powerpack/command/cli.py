import sys
import click
from .aliased_group import AliasedGroup
from powerpack import __version__


__all__ = ['cli']
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(cls=AliasedGroup, context_settings=CONTEXT_SETTINGS, help='Powerpack')
@click.version_option(version=__version__)
def cli():
    pass


if __name__ == '__main__':
    cli()
