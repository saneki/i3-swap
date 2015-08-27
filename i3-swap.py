#!/usr/bin/env python3

# Script to swap which workspace is on which monitor (output)
# Might not work as expected if at least one workspace is empty

import i3ipc, time

conn = i3ipc.Connection()
outputs = conn.get_outputs()

# Only include outputs with active: True
outputs = [o for o in outputs if o['active'] is True]

if len(outputs) == 2:
    conn.command('workspace ' + outputs[0]['current_workspace'])
    conn.command('move workspace to output right')

    # Hacky fix for race condition
    time.sleep(0.01)

    conn.command('workspace ' + outputs[1]['current_workspace'])
    conn.command('move workspace to output left')
elif len(outputs) < 2:
    print('Not enough outputs')
else:
    print('Too many outputs')
