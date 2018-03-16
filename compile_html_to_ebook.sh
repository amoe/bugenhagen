#! /bin/sh


header='<html>
   <body>
     <h1>Table of Contents</h1>
     <p style="text-indent:0pt">
'

footer='</p>
   </body>
</html>'


item_format='<a href="%s">%s</a><br/>'

echo "$header"

for file; do
    printf "$item_format" "$file" "$file"
done

echo "$footer"

