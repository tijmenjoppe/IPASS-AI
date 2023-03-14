rem Convert PDF to JPG

REM magick mogrify -verbose -format jpg -resize 3200x3200 -quality 95 -density 600 -background white -alpha remove 2018/*.pdf
REM magick mogrify -verbose -format jpg -resize 3200x3200 -quality 95 -density 600 -background white -alpha remove 2019/*.pdf
REM magick mogrify -verbose -format jpg -resize 3200x3200 -quality 95 -density 600 -background white -alpha remove 2020/*.pdf
magick mogrify -verbose -format jpg -resize 3200x3200 -quality 95 -density 600 -background white -alpha remove 2021/*.pdf

rem magick mogrify -verbose -density 600 -resize 3200x3200 -strip -interlace Plane -gaussian-blur 0.05 -quality 85 -format jpg *.pdf


rem Convert PNG to JPG

REM magick mogrify -verbose -format jpg -resize 3200x3200 -background white -alpha remove -alpha off -quality 95 2018/*.png
REM magick mogrify -verbose -format jpg -resize 3200x3200 -background white -alpha remove -alpha off -quality 95 2019/*.png
REM magick mogrify -verbose -format jpg -resize 3200x3200 -background white -alpha remove -alpha off -quality 95 2020/*.png
magick mogrify -verbose -format jpg -resize 3200x3200 -background white -alpha remove -alpha off -quality 95 2021/*.png

pause
