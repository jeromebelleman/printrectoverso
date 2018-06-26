'''
Join PDFs and open the result in Evince, ready to be printed duplex
'''

import subprocess
from gi.repository import Nautilus, GObject


def printrectoverso(_, files):
    '''
    Run pdfjoin, then Evince
    '''

    subprocess.call(['pdfjoin'] + \
                    [fle.get_location().get_path() for fle in files] + \
                    ['-o', '/tmp/printrectoverso.pdf'])
    subprocess.Popen(['evince', '/tmp/printrectoverso.pdf'])


class PrintRectoVerso(GObject.GObject, Nautilus.MenuProvider):
    '''
    Menu provider
    '''

    def get_file_items(self, _, files): # pylint: disable=arguments-differ
        for fle in files:
            if fle.get_mime_type() != 'application/pdf':
                return

        item = Nautilus.MenuItem(name='Nautilus::printrectoverso',
                                 label='Print Recto/Verso')
        item.connect('activate', printrectoverso, files)
        return item,
