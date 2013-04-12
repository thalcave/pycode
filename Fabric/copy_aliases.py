from fabric.api import env
from fabric.operations import run, put

#env.hosts = ['infongdev001.ehbackupdev.schlund.de']
env.hosts = ['infongtst006.ehbackuptest.schlund.de']

def copy_aliases():
    put('/home/florin/.bash_aliases', '/root/.bash_aliases')
