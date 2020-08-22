#!C:\Users\HP\PycharmProjects\coremusicplayergui\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'stagger==1.0.0','console_scripts','stagger'
__requires__ = 'stagger==1.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('stagger==1.0.0', 'console_scripts', 'stagger')()
    )
