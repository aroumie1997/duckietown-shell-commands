from __future__ import print_function

import os
import subprocess
import sys
from os.path import join, realpath, dirname

from dt_shell import DTCommandAbs, dtslogger


class DTCommand(DTCommandAbs):

    @staticmethod
    def command(shell, args):
        script_file = join(dirname(realpath(__file__)), 'start_hatchery.sh')

        script_cmd = '/bin/sh %s' % script_file
        print('Running %s' % script_cmd)

        env = {}
        env.update(os.environ)
        V = 'DOCKER_HOST'
        if V in env:
            msg = 'I will ignore %s in the environment because we want to run things on the laptop.' % V
            dtslogger.info(msg)
            env.pop(V)

        ret = subprocess.call(script_cmd, shell=True, stdin=sys.stdin, stderr=sys.stderr, stdout=sys.stdout, env=env)
        # process.communicate()
        if ret == 0:
            print('Done!')
        else:
            msg = ('An error occurred while starting the GUI tools container, please check and try again (%s).' % ret)
            raise Exception(msg)
