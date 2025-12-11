import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--name', help='Ім\'я користувача для привітання.')
def say(name):
    """Ця команда вітає користувача, якщо ім'я не починається на 'p'."""
    if not name:
        click.echo("Будь ласка, введіть ім'я через --name")
        return


    if name.lower().startswith('p'):
        click.echo("Ім’я не підходить")
    else:
        click.echo(f"{name}")


cli.add_command(say)

if __name__ == '__main__':
    cli()
