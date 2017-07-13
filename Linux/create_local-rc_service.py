#!/usr/bin/env python
import os, subprocess

targeted= """[Unit]
Description=/etc/rc.local Compatibility
ConditionFileIsExecutable=/usr/local/sbin/rc.local

[Service]
Type=oneshot
ExecStart=/usr/local/sbin/rc.local
TimeoutSec=0
StandardOutput=tty
RemainAfterExit=yes
SysVStartPriority=99

[Install]
WantedBy=multi-user.target"""

filename = '/etc/systemd/system/rc-local.service'
target = open(filename, 'w')
target.write(targeted)

target.close()

filename2 = '/usr/local/sbin/rc.local'
target2 = open(filename2, 'w')
target2.write('#!/bin/bash\n/usr/local/sbin/alertmailer.py >> /dev/null 2>&1 &\n')
target2.close()

subprocess.call(['systemctl', 'enable', 'rc-local.service'])
subprocess.call(['chmod', 'a+x', '/usr/local/sbin/rc.local'])
subprocess.call(['cp', 'alertmailer.py', '/usr/local/sbin/alertmailer.py'])
