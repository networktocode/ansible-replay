from __future__ import print_function
import re
import time

from colorama import Fore, Back, Style
import click

colors = {'ok': 'GREEN', 'changed': 'YELLOW',
          'unreachable': 'RED', 'failed': 'RED', 'other': 'WHITE'}

def itemcolor(items):
    result_colors = {'other': 'WHITE'}
    for item in items:
        if "=" in item:
            name, number = item.split('=')
            if int(number) == 0:
                result_colors[name] = 'WHITE'
            else:
                result_colors[name] = colors[name]
    if result_colors['failed'] == 'RED':
        result_colors['other'] = 'RED'
    elif result_colors['unreachable'] == 'RED':
        result_colors['other'] = 'RED'
    elif result_colors['changed'] == 'YELLOW':
        result_colors['other'] = 'YELLOW'
    elif result_colors['ok'] == 'GREEN':
        result_colors['other'] = 'GREEN'

    return result_colors

class ReplayLines:
    def __init__(self, line):
        self.ok =  'GREEN'
        self.skipping =  'BLUE'
        self.change =  'YELLOW'
        self.unreachable = 'RED'
        self.failed = 'RED'
        self.other = 'WHITE'
        self.line = line

    def _isok(self):
        return ('ok' in self.line)

    def _ischanged(self):
        return ('changed' in self.line)

    def _isunreachable(self):
        return ('unreachable' in self.line)

    def _isfailed(self):
        return ('failed' in self.line)

    def color(self):
        if self._isok():
            return self.ok
        elif self._ischanged():
            return self.change
        elif self._isunreachable():
            return self.unreachable
        elif self._isfailed():
            return self.failed
        else:
            return self.other

@click.command()
@click.option('--host-timer', default=0.10,
              help='Hold timer between host')
@click.option('--task-timer', default=0.10,
              help='Hold timer when a task run')
@click.option('--task-pause', is_flag=True,
              help='Pausing when hitting a task')
@click.argument('ansible_file_log', type=click.File('r'),
                required=True)
def replay(host_timer, task_timer, task_pause, ansible_file_log):
    out_file = ansible_file_log.readlines()
    ansible_file_log.close()
    play_recap = False

    for line in out_file:
        line = line.strip()
        replay_line = ReplayLines(line)
        color = replay_line.color()
        print (getattr(Fore, color) + line)

