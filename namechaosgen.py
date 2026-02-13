#!/usr/bin/env python3

import click
import random


def upper_lower_normal_generator(value):
    for fmt in value:
        yield fmt.lower()
        yield fmt.upper()
        yield fmt


vowel_dict = {
    'a': ['@', '4'],
    'e': ['3'],
    'i': ['1', '!'],
    'o': ['0'],
    's': ['5', '$']
}


@click.command()
@click.argument('filename', type=click.File('r'))
@click.option('--output', '-o', type=click.File('w'), default=None, help='Output file to save the name formats(default: None)')
@click.option('--advanced', '-a', is_flag=True, default=False, help='Generate advanced name formats with random numbers and special characters(default: False)')
@click.option('--super-advanced', '-s', is_flag=True, default=False, help='Generate super advanced name formats with vowel substitutions(default: False)')
@click.option('--echo/--no-echo', '-d/-nd', default=True, help='Do not print the generated name formats to the console(default: True)(use --no-echo to disable)')
@click.version_option(version='1.0.0', prog_name='namechaosgen')
def generate_name_format(filename, output, advanced, super_advanced, echo):
    """Generate name formats from a file containing names."""
    all_results = []

    for line in filename:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) != 2:
            click.echo(f"Skipping invalid line: '{line}' (expected 2 words)", err=True)
            continue

        firstname, lastname = parts
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

        line_results = []

        for fmt in upper_lower_normal_generator(formats):
            line_results.append(fmt)

            if advanced or super_advanced:
                for char in fmt:
                    if char.lower() in vowel_dict:
                        for replacement in vowel_dict[char.lower()]:
                            advanced_format = fmt.replace(char, replacement)
                            line_results.append(advanced_format)

            if super_advanced:
                random_number = random.randint(0, 99)
                random_char = random.choice('!@#$%^&*()')
                line_results.append(f"{fmt}{random_number}{random_char}")
                line_results.extend([f'{fmt}{x}' for x in range(10)])
                line_results.extend([f'{x}{fmt}' for x in range(10)])

        all_results.extend(line_results)

    result = '\n'.join(all_results)

    if output:
        try:
            output.write(result)
        except Exception as e:
            click.echo(f"Error writing to output file: {e}", err=True)
            return

    if echo:
        click.echo(result)


if __name__ == '__main__':
    generate_name_format()