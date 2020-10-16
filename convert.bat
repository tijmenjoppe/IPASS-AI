rem Convert PDF to JPG

magick mogrify -verbose -format jpg -resize 3200x3200 -quality 95 -density 600 2018/*.pdf

rem magick mogrify -verbose -density 600 -resize 3200x3200 -strip -interlace Plane -gaussian-blur 0.05 -quality 85 -format jpg *.pdf


rem Convert PNG to JPG

magick mogrify -verbose -format jpg -resize 3200x3200 -quality 95 2018/*.png

pause