import click

@click.command()
@click.argument('file', type=click.File('r'))
class namegen:
    """A simple CLI tool to generate names."""
    def __init__(self, file):
        self.file = file

    def generate_names(self):
        names = self.file.read().splitlines()
        for name in names:
            click.echo(click.style(name, fg='blue', bold=True)) 