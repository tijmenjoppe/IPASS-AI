#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def generate_gallery(df, category=''):
    cells_per_row = 3
    cell_color = " bgcolor='#F8F8F8'"
    cell_width = 300

    html_string_start = f"<html>\n" \
                        f"<head>\n" \
                        f"  <title>IPASS AI projecten {category}</title>\n" \
                        f"</head>\n" \
                        f"<body>\n" \
                        f"  <h2>IPASS AI projecten {category}</h2>\n"

    html_string_end = "</body>\n</html>\n"

    print(f"Creating galery page '{category.replace(' ', '_')}.html' with {len(df)} entries...")
    with open(f"{category.replace(' ', '_')}.html", 'w') as f:
        # f.write(html_string_start)
        f.write('<table>\n')
        f.write('  <tr>\n')

        i = 0
        while i < len(df):
            f.write(f"    <td style='padding:16px; width:{cell_width}px; overflow:hidden;' align='center' valign='top'{cell_color if i % 2 else ''}>\n")
            f.write(f"      <h3 align='center'>{df.iloc[i]['titel']}</h3>\n")
            f.write(f"      <p align='center'>door {df.iloc[i]['naam']}</p>\n")
            f.write(f"      <a href='https://github.com/tijmenjoppe/IPASS-AI/raw/main/{df.iloc[i]['jaar']}/{df.iloc[i]['studentnummer']}.jpg' target='_blank'>\n")
            f.write(f"        <img style='width:100%; height:auto;' src='https://github.com/tijmenjoppe/IPASS-AI/raw/main/{df.iloc[i]['jaar']}/{df.iloc[i]['studentnummer']}.jpg'>\n")
            f.write(f"      </a>\n")
            f.write(f"      <p align='left'>\n")

            # Only add category if it is available
            if not pd.isnull(df.iloc[i]['categorie']):
                f.write(f"        {df.iloc[i]['categorie']}\n")

            f.write(f"        <span style='float:right;'>\n")

            # Only add email if it is available
            if not pd.isnull(df.iloc[i]['email']):
                f.write(f"          <a style='text-decoration:none;' href='mailto:{df.iloc[i]['email']}'>\n")
                f.write(f"            <img src='https://canvas.hu.nl/files/1287896/download?download_frd=1' alt='E-mail'>\n")
                f.write(f"          </a>\n")

            f.write(f"          <a style='text-decoration:none;' href='{df.iloc[i]['github']}' target='_blank'>\n")
            f.write(f"            <img src='https://canvas.hu.nl/files/1287897/download?download_frd=1' alt='GitHub'>\n")
            f.write(f"          </a>\n")
            f.write(f"        </span>\n")
            f.write(f"      </p>\n")
            f.write('    </td>\n')

            if i % cells_per_row == cells_per_row - 1:
                f.write('  </tr>\n  <tr>\n')

            i += 1

        while i % cells_per_row != 0:
            f.write('    <td></td>\n')
            i += 1

        f.write('  </tr>\n')
        f.write('</table>\n')
        # f.write(html_string_end)


if __name__ == '__main__':
    df = pd.read_csv('galerij.csv', delimiter=';')
    print(f"Read 'galerij.csv': {df.shape[0]} rows, {df.shape[1]} cols.")

    jaren = df['jaar'].unique()
    for jaar in jaren:
        generate_gallery(df[df['jaar'] == jaar], str(jaar))

    tags = df['categorie'].dropna().unique()
    for tag in tags:
        generate_gallery(df[df['categorie'] == tag], tag)
