import click
import os 


def upper_lower_normal_generator(value):
    for fmt in value:
        yield fmt.lower() 
        yield fmt.upper() 
        yield fmt 

@click.command()
@click.argument('filename', type=click.File('r'))
@click.option('--output', '-o', type=click.File('w'), default=None, help='Output file to save the name formats')
def generate_name_format(filename, output):
    """
    generate name formats
    """

    try:
        filename.open()
    except Exception as e:
        click.echo(f"Error opening file: {e}", err=True)
        return
    
    for line in filename:
        firstname, lastname = line.strip().split() 
        formats = [
            f"{firstname}.{lastname}",
            f"{firstname}_{lastname}",
            f"{firstname[0]}{lastname}",
            f"{firstname}{lastname[0]}",
            f"{lastname}.{firstname}",
            f"{lastname}_{firstname}",
            f"{lastname[0]}{firstname}",
            f"{lastname}{firstname[0]}",
        ]   

        if output:
            try:
                for fmt in upper_lower_normal_generator(formats):
                    output.write(fmt + '\n')
            
            except Exception as e:
                click.echo(f"Error {e}", err=True)
                for fmt in upper_lower_normal_generator(formats):
                    click.echo(fmt)

        elif output is None:
            for fmt in upper_lower_normal_generator(formats):
                click.echo(fmt)



if __name__ == '__main__':
    generate_name_format()





