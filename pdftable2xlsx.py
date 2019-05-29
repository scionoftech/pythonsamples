import click
import glob
from pathlib import Path
import pdfplumber
import pandas as pd
from pandas import ExcelWriter


def to_excel(path, output_path):
    with pdfplumber.open(path) as pdf:
        data = []
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            # print(first_page.chars[0])
            data += page.extract_table()
            # print(data)
        df = pd.DataFrame(data)
        filename = Path(path).name.split('.')
        writer = ExcelWriter(output_path + '\\' + filename[0] + '.xlsx')
        df.to_excel(writer, 'Sheet1', index=False)
        writer.save()


@click.command()
# @click.argument('name')
@click.option('--input_path', '-ip', help='input files path')
@click.option('--output_path', '-op', help='output files path')
def get_files(input_path, output_path):
    """This program generates xlsx files from pdf."""
    for file in glob.glob(input_path + '\\' + "*.pdf"):
        to_excel(file, output_path)


if __name__ == '__main__':
    get_files()
