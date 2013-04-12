from fabric.api import env, local, settings, hide
from fabric.operations import run, put
from fabric.contrib.files import append

#env.hosts = ['infongdev001.ehbackupdev.schlund.de']
env.hosts = ["infongtst00"+str(x)+".ehbackuptest.schlund.de" for x in range(1,10)]


def scp_put(src, dst):
    with hide('running', 'output'):
        local('scp ' + src + ' {user}@{host}:'.format(**env) + dst, capture=True)

def copy_aliases():
    scp_put('/home/florin/.bash_aliases', '/root/.bash_aliases')
    append('/root/.bashrc', '\n. ~/.bash_aliases')
