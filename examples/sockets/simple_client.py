#!/usr/bin/env python
"""
Simple client that sends program_change messages to server at timed
intervals.

Example:

    python simple_client.py localhost:8080
"""
import sys
import time
import random
import mido

hostname, port = mido.sockets.parse_address(sys.argv[1])
ports = [mido.open_input(name) for name in sys.argv[2:]]

notes = [60, 67, 72, 79, 84, 79, 72, 67, 60]
on = mido.Message('note_on', velocity=100)
off = mido.Message('note_off', velocity=100)

with mido.sockets.connect(hostname, port) as server_port:
    try:
        message = mido.Message('program_change')
        for note in notes:
            on.note = off.note = note

            server_port.send(on)
            time.sleep(0.05)

            server_port.send(off)
            time.sleep(0.1)
    finally:
        server_port.reset()
