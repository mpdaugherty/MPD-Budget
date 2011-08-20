import os
import posixpath
from fabric.api import *

env.hosts = ['budget.mpdaugherty.com']
env.user = 'ubuntu'
env.key_filename = ['/Users/mpdaugherty/.ssh/mpd-aws-key.pem']

BUDGET_ROOT = posixpath.normpath(posixpath.join(__file__.replace('\\', '/'), '../../')) + '/'

def deploy():
    put(BUDGET_ROOT+'code')
    run('[ -d /var/www/mpdaugherty-budget ] || mkdir /var/www/mpdaugherty-budget')
    with cd('/var/www/mpdaugherty-budget'):
        run('[ -d env ] || virtualenv --no-site-packages env')
        run('[ -d logs ] || ( mkdir logs && chmod g+w logs )')
        run('rm -rf code')
        run('cp ~/code code')
        with prefix('source env/bin/activate'):
            run('pip install -r code/requirements.txt')
            run('python code/budget/manage.py syncdb')
            run('python code/budget/manage.py migrate budgeting')
        sudo('cp code/config/apache.prod.conf /etc/apache2/sites-available/mpd-budget')
#        sudo('ln -s /etc/apache2/sites-enabled/mpd-budget /etc/apache2/sites-available/mpd-budget')
        sudo('/etc/init.d/apache2 restart')
