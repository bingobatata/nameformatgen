#!/usr/bin/env python3

import click
import os 
import random as rand 


def upper_lower_normal_generator(value):
    for fmt in value:
        yield fmt.lower() 
        yield fmt.upper() 
        yield fmt 

vowleddic = {
    'a': ['@', '4'],
    'e': ['3'],
    'i': ['1', '!'],
    'o': ['0'],
    's': ['5', '$']
}

@click.command()
@click.argument('filename', type=click.File('r'))
@click.option('--output', '-o', type=click.File('w'), default=None, help='Output file to save the name formats')
@click.option('--advanced', '-a', is_flag=True, default=False, help='Generate advanced name formats with random numbers and special characters')
@click.option('--super-advanced', '-s', is_flag=True, default=False, help='Generate super advanced name formats with vowel substitutions')
def generate_name_format(filename, output, advanced, super_advanced):
    result = ''
    """
    generate name formats
    """

    try:
        click.open_file(filename.name, 'r')
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
            f"1{firstname}{lastname}",
            f"{firstname}1{lastname}",
            f"{firstname}{lastname}1",
            f"123{firstname}{lastname}",
            f"{firstname}123{lastname}",
            f"{firstname}{lastname}123",
        ]   

        for _ in upper_lower_normal_generator(formats):
            result += f'{_}\n'
            if advanced or super_advanced:
                for chr in _:
                    if chr.lower() in vowleddic:
                        for replacement in vowleddic[chr.lower()]:
                            advanced_format = _.replace(chr, replacement)
                            result += f'{advanced_format}\n'


            if super_advanced:
                random_number = rand.randint(0, 99)
                random_char = rand.choice('!@#$%^&*()')
                advanced_format = f"{_}{random_number}{random_char}"
                result += f'{advanced_format}\n'
                result += '\n'.join([f'{_}{x}' for x in range(0, 10)]) + '\n'
                result += '\n'.join([f'{x}{_}' for x in range(0, 10)]) + '\n'

        try:
            if output:
                output.write(result)
                result = ''

        except Exception as e:
            click.echo(f"Error writing to output file: {e}", err=True)
            return

    click.echo(result)


if __name__ == '__main__':
    generate_name_format()





