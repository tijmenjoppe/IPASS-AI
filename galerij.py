#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd



def generate_gallery(df, category=''):
    cells_per_row = 3
    cell_color = " bgcolor='#F8F8F8'"

    html_string_start = f"<html>\n" \
                        f"<head>\n" \
                        f"\t<title>IPASS AI projecten {category}</title>\n" \
                        f"</head>\n" \
                        f"<body>\n" \
                        f"\t<h2>IPASS AI projecten {category}</h2>\n"

    html_string_end = "</body>\n</html>\n"

    print(f"Creating galery page '{category}.html' with {len(df)} entries...")
    with open(f'{category}.html', 'w') as f:
        # f.write(html_string_start)
        f.write('<table>\n')
        f.write('\t<tr>\n')

        i = 0
        while i < len(df):

            f.write(f"\t\t<td style='padding:16px' align='center' valign='top'{cell_color if i % 2 else ''}>\n")

            #   		<div style="position:relative; overflow: auto; height: 100%;">
            # 				<p>Lorem ipsum dolor sit amet.</p>
            # 				<div style="position:absolute; bottom:0; right:0; background: yellow;">
            # 					This will be positioned at 5,5 relative to the cell
            # 				</div>
            # 			</div>

            f.write(f"\t\t\t<h3 align='center'>{df.iloc[i]['titel']}</h3>\n")
            f.write(f"\t\t\t<p align='center'>{df.iloc[i]['naam']}</p>\n")
            f.write(
                f"\t\t\t<a href='https://github.com/tijmenjoppe/IPASS-AI/raw/main/{df.iloc[i]['jaar']}/{df.iloc[i]['studentnummer']}.jpg' target='_blank'>\n")
            f.write(
                f"\t\t\t\t<img src='https://github.com/tijmenjoppe/IPASS-AI/raw/main/{df.iloc[i]['jaar']}/{df.iloc[i]['studentnummer']}.jpg' width='300' height='424'>\n")
            f.write(f"\t\t\t</a>\n")
            f.write(f"\t\t\t<p align='left'>\n")

            # Only add category if it is available
            if not pd.isnull(df.iloc[i]['categorie']):
                f.write(f"\t\t\t\t{df.iloc[i]['categorie']}\n")

            f.write(f"\t\t\t\t<span style='float:right;'>\n")

            # Only add email if it is available
            if not pd.isnull(df.iloc[i]['email']):
                f.write(f"\t\t\t\t\t<a style='text-decoration: none;' href='mailto:{df.iloc[i]['email']}'>\n")
                f.write(
                    f"\t\t\t\t\t\t<img src='https://canvas.hu.nl/files/1287896/download?download_frd=1' alt='E-mail'>\n")
                # f.write(f"\t\t\t\t\t\t<img src='img/email.png'>\n")
                f.write(f"\t\t\t\t\t</a>\n")

            f.write(f"\t\t\t\t\t<a style='text-decoration: none;' href='{df.iloc[i]['github']}' target='_blank'>\n")
            f.write(
                f"\t\t\t\t\t\t<img src='https://canvas.hu.nl/files/1287897/download?download_frd=1' alt='GitHub'>\n")
            # f.write(f"\t\t\t\t\t\t<img src='img/github.png'>\n")
            f.write(f"\t\t\t\t\t</a>\n")
            f.write(f"\t\t\t\t</span>\n")
            f.write(f"\t\t\t</p>\n")
            f.write('\t\t</td>\n')
            #
            # '''
            # <p><a href="mailto:nan">&nbsp;</a>
            # <a href="mailto:nan"><img src="https://canvas.hu.nl/files/1287896/download?download_frd=1" alt="email.png" /></a><a href="mailto:nan">&nbsp;</a><a href="https://github.com/nielsbijl/IPASS"><img src="https://canvas.hu.nl/files/1287897/download?download_frd=1" alt="github.png" /></a><a href="https://github.com/nielsbijl/IPASS" target="_blank" rel="noopener"> </a></p>
            # '''
            # for col in df.columns:
            #     value = df.iloc[i][col]
            #     f.write('<td>'+str(value)+'</td>')

            if i % cells_per_row == cells_per_row - 1:
                f.write('\t</tr>\n\t<tr>\n')

            i += 1

        while i % cells_per_row != 0:
            f.write('\t\t<td></td>\n')
            i += 1

        f.write('\t</tr>\n')
        f.write('</table>\n')
        f.write(html_string_end)


if __name__ == '__main__':
    df = pd.read_csv('galerij.csv', delimiter=';')
    print(df)

    jaren = df['jaar'].unique()

    for jaar in jaren:
        generate_gallery(df[df['jaar'] == jaar], str(jaar))
