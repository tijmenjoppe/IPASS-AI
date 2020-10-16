#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('galerij.csv', delimiter=';')
    print(df)

    categorie = '2018'
    
    html_string_start = f"<html>\n" \
                        f"<head>\n" \
                        f"\t<title>IPASS AI projecten {categorie}</title>\n" \
                        f"</head>\n" \
                        f"<body>\n" \
                        f"\t<h2>IPASS AI projecten {categorie}</h2>\n"

    html_string_end = "</body>\n</html>\n"
    
    with open(r'galerij.html', 'w') as f:
        f.write(html_string_start)
        f.write('<table>\n')
        f.write('\t<tr>\n')

        i = 0
        while i < len(df):
            f.write("\t\t<td align='center' valign='top'>\n")

            f.write(f"\t\t\t<h3 align='center'>{df.iloc[i]['titel']}</h3>\n")
            f.write(f"\t\t\t<p align='center'>{df.iloc[i]['naam']}</p>\n")
            f.write(f"\t\t\t<a href='{df.iloc[i]['jaar']}/{df.iloc[i]['studentnummer']}.jpg' target='_blank'>\n")
            f.write(f"\t\t\t\t<img src='{df.iloc[i]['jaar']}/{df.iloc[i]['studentnummer']}.jpg' width='300'>\n")
            f.write(f"\t\t\t</a>\n")
            f.write(f"\t\t\t<p align='right'>\n")
            f.write(f"\t\t\t\t<a href='mailto:{df.iloc[i]['email']}'>\n")
            f.write(f"\t\t\t\t\t<img src='img/email.png'>\n")
            f.write(f"\t\t\t\t</a>\n")
            f.write(f"\t\t\t\t<a href='{df.iloc[i]['github']}' target='_blank'>\n")
            f.write(f"\t\t\t\t\t<img src='img/github.png'>\n")
            f.write(f"\t\t\t\t</a>\n")
            f.write(f"\t\t\t</p>\n")
            f.write('\t\t</td>\n')

            # for col in df.columns:
            #     value = df.iloc[i][col]
            #     f.write('<td>'+str(value)+'</td>')

            if i % 3 == 2:
                f.write('\t</tr>\n\t<tr>\n')

            i += 1

        while i % 3 != 0:
            f.write('\t\t<td></td>\n')
            i += 1

        f.write('\t</tr>\n')
        f.write('</table>\n')
        f.write(html_string_end)
