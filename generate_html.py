from pathlib import Path
import clipboard
import datetime
import sys

working_dir = Path(__file__).absolute().parent

embedding = clipboard.paste()

prefix = """<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>


"""

ending = """

</body>
</html>
"""

data = prefix + embedding + ending

# data
current_time = datetime.datetime.now()
date_format = '%Y-%m-%d-%H-%M-%S-%f'
timestr = current_time.strftime(date_format)


out_html = f"{timestr}.html"

with open(out_html, 'w') as f:
    f.write(data)

iframe_str = '{{iframe: https://htmlpreview.github.io/?https://github.com/wshuyi/my-public-loom-videos/blob/main/' + out_html +'}}'
clipboard.copy(iframe_str)