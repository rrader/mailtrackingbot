from pathlib import Path

from fabric.api import run, env
from fabric.operations import put
from fabric.tasks import execute

MAILTRACKINGBOT_DIR = Path('/opt/mailtrackingbot')

env.hosts = ['188.166.50.133']
env.user = 'root'


def put_files():
    run('mkdir -p %s' % MAILTRACKINGBOT_DIR)
    put('./app', str(MAILTRACKINGBOT_DIR))
    run('cp -f /opt/secret.ini %s' % (MAILTRACKINGBOT_DIR / 'app/secret.ini'))
    run('cp -f %s %s' % (MAILTRACKINGBOT_DIR / 'app/config/prod/config.ini', MAILTRACKINGBOT_DIR / 'app/config.ini'))


def setup_deps():
    run('apt-get install -y python3-setuptools python3-pip nginx')
    run('pip3 install -U pip setuptools')


def requirements():
    execute(setup_deps)
    run('pip3 install -r %s' % (MAILTRACKINGBOT_DIR / 'app/requirements.txt'))


def deploy():
    execute(put_files)
    execute(requirements)
    run(
        'cp -f %s %s' % (
            MAILTRACKINGBOT_DIR / 'app/deploy/mailtrackingbot.service',
            '/lib/systemd/system/mailtrackingbot.service'
        )
    )
    run('systemctl daemon-reload')
    run('systemctl enable mailtrackingbot')
    run('systemctl restart mailtrackingbot')


def bash():
    run('bash')
