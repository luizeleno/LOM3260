import os
import re
import datetime

data = datetime.date.today()
timestamp = data.strftime("%d/%m/%y")

for root, dirs, files in os.walk("."):
    for file in files:
        name, extension = os.path.splitext(file)
        if extension == '.md':
            filepath = os.path.join(root, file)
            f = open(filepath, 'r')
            text = f.read()
            f.close()
            print(filepath)
            if re.search('timestamp', text):
                pass
            else:
                sub = re.search('---(.*?)---', text, re.DOTALL).group(1)
                sub = '---' + sub
                sub += f'timestamp: {timestamp}\n'
                sub += '---'
                sub = re.sub('---(.*?)---', sub, text, flags=re.DOTALL)
                f = open(filepath, 'w')
                print(sub, file=f)
                f.close()
