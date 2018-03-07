"""

Usage:
    manage.py runserver
    manage.py -t
    manage.py -t <test_name>
    manage.py -s <script>


"""

import os
import subprocess
from docopt import docopt

import scripts


if __name__ == '__main__':
    argments = docopt(__doc__)

    if argments['runserver']:
        exec('from scripts import runserver')

    if argments['-t']:
        arg = argments['<test_name>']
        files = [f[:-3] for f in os.listdir('tests') if f[0] != '_']
        if arg is None:
            os.system('nosetests tests/*.py --with-coverage'
                      '--cover-package=blog --cover-xml')
        elif arg in files:
            popen = subprocess.Popen(['nosetests', 'tests/%s.py' % arg,
                                      '--with-coverage',
                                      '--cover-package=blog', '--cover-xml'],
                                     stderr=subprocess.STDOUT)
        else:
            print('\nThere is not mpdule name "%s" with -t.' % arg)
            print('Please input anything such as:\n')
            for f in files:
                print('- %s' % f)
            print('\n')

    if argments['-s']:
        arg = argments['<script>']
        try:
            exec('from scripts import %s as test' % arg)
        except ImportError as e:
            files = [f[:-3] for f in os.listdir('scripts') if f[0] != '_']
            print('\nThere is not mpdule name "%s" with -t.' % arg)
            print('Please input anything such as:\n')
            for f in files:
                print('- %s' % f)
            print('\n')
