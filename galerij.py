#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def generate_gallery(df, category=''):
    base_domain = 'https://tijmenjoppe.github.io/IPASS-AI'

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

    filename = category.replace(' ', '_').lower() + '.html'
    if category == '':
        filename = 'ipass.html'

    print(f"Creating galery page '{filename}' with {len(df)} entries...")
    with open(filename, 'w') as f:
        # f.write(html_string_start)
        f.write('<table>\n')
        f.write('  <tr>\n')

        i = 0
        while i < len(df):
            f.write(
                f"    <td style='padding:16px; width:{cell_width}px; overflow:hidden;' align='center' valign='top'{cell_color if i % 2 else ''}>\n")
            f.write(f"      <h3 align='center'>{df.iloc[i]['titel']}</h3>\n")
            f.write(f"      <p align='center'>door {df.iloc[i]['naam']}</p>\n")
            f.write(
                f"      <a href='{base_domain}/{df.iloc[i]['jaar']}/{df.iloc[i]['studentnummer']}.jpg' target='_blank'>\n")
            f.write(
                f"        <img style='width:100%; height:auto;' src='{base_domain}/{df.iloc[i]['jaar']}/{df.iloc[i]['studentnummer']}.jpg'>\n")
            f.write(f"      </a>\n")
            f.write(f"      <p align='left'>\n")

            # Add categories
            if not pd.isnull(df.iloc[i]['categorie']):
                tags = [c.strip() for c in df.iloc[i]['categorie'].split('|')]
                f.write(f"        ")
                for tag in tags:
                    f.write(f"<a href='{base_domain}/{tag.replace(' ', '_').lower()}.html'>{tag}</a>")

                    if tag == tags[-1]:
                        f.write(f"\n")
                    else:
                        f.write(f" | ")

            f.write(f"        <span style='float:right;'>\n")

            # Only add link to video if it is available
            if df.iloc[i]['video'] == 'ja':
                f.write(f"          <a style='text-decoration:none;' href='{base_domain}/{df.iloc[i]['jaar']}/{df.iloc[i]['studentnummer']}.mp4' target='_blank'>\n")
                f.write(f"            <img src='{base_domain}/img/video.png' alt='Video'>\n")
                f.write(f"          </a>\n")

            # Add email
            email = df.iloc[i]['email']
            if pd.isnull(df.iloc[i]['email']):  # Generate email if it is unavailable
                email = '.'.join(df.iloc[i]['naam'].split(' ', 1)).lower().replace(' ', '') + '@student.hu.nl'
            f.write(f"          <a style='text-decoration:none;' href='mailto:{email}'>\n")
            f.write(f"            <img src='{base_domain}/img/email.png' alt='E-mail'>\n")
            f.write(f"          </a>\n")

            # Only add link to GitHub if it is available
            if not pd.isnull(df.iloc[i]['github']):
                f.write(f"          <a style='text-decoration:none;' href='{df.iloc[i]['github']}' target='_blank'>\n")
                f.write(f"            <img src='{base_domain}/img/github.png' alt='GitHub'>\n")
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


def generate_json(df, category=''):
    base_domain = 'https://tijmenjoppe.github.io/IPASS-AI'

    filename = category.replace(' ', '_').lower() + '.html'
    if category == '':
        filename = 'ipass-ai.json'

    print(f"Creating JSON-file '{filename}' with {len(df)} entries...")
    first_enty = True
    with open(filename, 'w') as f:
        i = 0
        f.write('{\n\t"ipass-ai": [\n')

        while i < len(df):
            if i > 0:
                f.write(',\n')

            f.write('\t\t{\n')
            f.write(f'\t\t\t"image": "{base_domain}/{df.iloc[i]["jaar"]}/{df.iloc[i]["studentnummer"]}.jpg",\n')
            f.write(f'\t\t\t"caption": "{df.iloc[i]["titel"]}",\n')
            f.write(f'\t\t\t"student": "{df.iloc[i]["naam"]}",\n')
            f.write(f'\t\t\t"year": "{df.iloc[i]["jaar"]}",\n')

            # Add email
            email = df.iloc[i]['email']
            if pd.isnull(df.iloc[i]['email']):  # Generate email if it is unavailable
                email = '.'.join(df.iloc[i]['naam'].split(' ', 1)).lower().replace(' ', '') + '@student.hu.nl'
            f.write(f'\t\t\t"email": "{email}"\n')
            f.write('\t\t}')

            i += 1

        f.write('\n\t]\n}\n')


def generate_slideshow(df, category=''):
    base_domain = 'https://tijmenjoppe.github.io/IPASS-AI'

    html_string_start = '''<html>
	<head>
		<link rel="stylesheet" href="css/simple-slideshow-styles.css"/>
	</head>
	<body>
        <!-- Source: https://github.com/leemark/better-simple-slideshow -->
		<div class="bss-slides num1" tabindex="1" autofocus="autofocus">
'''

    html_string_end = '''       </div>
	</body>
	<script src="js/better-simple-slideshow.js"></script>

<script>
var options = {
            auto : {
                speed : 15000,
                pauseOnHover : false
            },
            fullScreen : true,
        };
makeBSS('.bss-slides', options);
</script>

</html>
'''

    filename = category.replace(' ', '_').lower() + '_slideshow.html'
    if category == '':
        filename = 'ipass_slideshow.html'

    print(f"Creating slideshow '{filename}' with {len(df)} entries...")
    with open(filename, 'w') as f:
        f.write(html_string_start)

        i = 0
        while i < len(df):
            # Add email
            email = df.iloc[i]['email']
            if pd.isnull(df.iloc[i]['email']):  # Generate email if it is unavailable
                email = '.'.join(df.iloc[i]['naam'].split(' ', 1)).lower().replace(' ', '') + '@student.hu.nl'

            f.write(f'\t\t\t<figure>\n')
            f.write(f'\t\t\t\t<img style="height:100%;" src="{base_domain}/{df.iloc[i]["jaar"]}/{df.iloc[i]["studentnummer"]}.jpg"/>\n')
            f.write(f'\t\t\t\t<figcaption>{df.iloc[i]["titel"]} door <a href="mailto:{email}">{df.iloc[i]["naam"]}</a></figcaption>\n')
            f.write(f'\t\t\t</figure>\n')

            i += 1

        f.write(html_string_end)


if __name__ == '__main__':
    df = pd.read_csv('galerij.csv', delimiter=';')
    print(f"Read 'galerij.csv': {df.shape[0]} rows, {df.shape[1]} cols.")

    df = df[df['poster'] == 'ja']
    print(f"{df.shape[0]} rows left after dropping projects without poster.")

    # Sort by year, then by student id
    df = df.sort_values(['jaar', 'studentnummer'])

    with open("index.html", 'w') as index_file:
        # Create page with all project posters
        print("Creating overview page...")
        index_file.write("<h1>IPASS AI</h1>\n\n")
        index_file.write("<a href='ipass.html'>Alle projecten</a> (<a href='ipass_slideshow.html'>slideshow</a>)\n\n")
        generate_gallery(df)
        generate_slideshow(df)
        generate_json(df)

        # Create page for each year
        print("\nCreating pages grouped by year...")
        index_file.write("<h2>Projecten per jaar</h2>\n\n<ul>\n")
        jaren = df['jaar'].unique()
        for jaar in jaren:
            generate_gallery(df[df['jaar'] == jaar], str(jaar))
            generate_slideshow(df[df['jaar'] == jaar], str(jaar))
            index_file.write(f"   <li><a href='{str(jaar) + '.html'}'>{jaar}</a> (<a href='{str(jaar) + '_slideshow.html'}'>slideshow</a>)</li>\n")

        # Create page for each category/tag
        print("\nCreating pages grouped by tag...")
        index_file.write("</ul>\n\n<h2>Projecten per onderwerp</h2>\n\n<ul>\n")

        # Extract all tags from category column (multiple tags are delimited with an '|')
        categories = df['categorie'].dropna().unique()
        tags = set()
        for category in categories:
            tags |= set([tag.strip() for tag in category.split('|')])

        tags = sorted(tags)
        print(f"{len(tags)} categories: {tags}")

        for tag in tags:
            generate_gallery(df[df['categorie'].str.contains(tag, na=False)], tag)
            pagename = tag.replace(' ', '_').lower() + '.html'
            index_file.write(f"   <li><a href='{pagename}'>{tag}</a></li>\n")

        index_file.write("</ul>\n")
