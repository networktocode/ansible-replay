from __future__ import print_function
import re
import time

from colorama import Fore
import click


class Timer(object):
    def __init__(self, line, task_timer, host_timer):
        self.task_timer = task_timer
        self.host_timer = host_timer
        self.line = line

    def get_sleep(self):
        if 'task' in self.line:
            return self.task_timer
        return self.host_timer

    def is_pause(self):
        if 'task' in self.line:
            return True


class ReplayLine(object):
    def __init__(self):
        self.ok = 'GREEN'
        self.skipping = 'BLUE'
        self.changed = 'YELLOW'
        self.unreachable = 'RED'
        self.failed = 'RED'
        self.other = 'WHITE'
        self.recap = False

    def _is_ok(self):
        return ('ok' in self.line)

    def _is_changed(self):
        return ('changed' in self.line)

    def _is_skipping(self):
        return ('skipping' in self.line)

    def _is_unreachable(self):
        return ('unreachable' in self.line)

    def _is_failed(self):
        return ('failed' in self.line)

    def _set_recap(self):
        if 'recap' in self.line:
            self.recap = True

    def _set_line(self, line):
        self.line = line

    def _get_color(self):
        if self._is_ok():
            return self.ok
        elif self._is_changed():
            return self.changed
        elif self._is_skipping():
            return self.skipping
        elif self._is_unreachable():
            return self.unreachable
        elif self._is_failed():
            return self.failed
        else:
            return self.other

    def _get_recap_colors(self, line):
        if '=' in line:
            name, number = line.split('=')
            if int(number) == 0:
                setattr(self, name, 'WHITE')
            else:
                if name == 'failed':
                    setattr(self, name, 'RED')
                elif name == 'unreachable':
                    setattr(self, name, 'RED')
                elif name == 'changed':
                    setattr(self, name, 'YELLOW')
                elif name == 'ok':
                    setattr(self, name, 'GREEN')

    def set_recap(self):
        if self.failed == 'RED':
            self.other = 'RED'
        elif self.unreachable == 'RED':
            self.other = 'RED'
        elif self.changed == 'YELLOW':
            self.other = 'YELLOW'
        elif self.ok == 'GREEN':
            self.other = 'GREEN'


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
    lines = ansible_file_log.readlines()
    ansible_file_log.close()
    replay_line = ReplayLine()
    for line in lines:
        line = line.strip().lower()
        if not replay_line.recap:
            replay_line._set_line(line)
            replay_line._set_recap()
            color = replay_line._get_color()
            print (getattr(Fore, color) + line)
            timer = Timer(line, task_timer, host_timer)
            time.sleep(timer.get_sleep())
            if task_pause:
                if timer.is_pause():
                    raw_input('')
        else:
            recap_lines = line.split()
            for recap_line in recap_lines:
                replay_line._get_recap_colors(recap_line.strip())
            try:
                _, sp1, sp2, sp3, sp4, sp5, _ = re.split("\S+", line)
                replay_line.set_recap()
                print ("{}{}{}{}{}{}{}{}{}{}{}".format(getattr(Fore, replay_line.other) + recap_lines[0], sp1,
                                                       getattr(Fore, replay_line.other) + recap_lines[1], sp2,
                                                       getattr(Fore, replay_line.ok) + recap_lines[2], sp3,
                                                       getattr(Fore, replay_line.changed) + recap_lines[3], sp5,
                                                       getattr(Fore, replay_line.unreachable) + recap_lines[4], sp5,
                                                       getattr(Fore, replay_line.failed) + recap_lines[5]))
            except:
                pass
