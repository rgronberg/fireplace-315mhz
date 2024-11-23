#! /usr/bin/python3

import csv

def get_pulses(filename):
    # Counters
    threshold = 2.5
    current_level = 0
    steps_at_level = 0

    # CSV values
    increment = 0

    # Output
    raw = []

    with open(filename, 'r') as csv_file:
        # print(file.readline())
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == 'X':
                continue

            if row[0] == 'Sequence':
                increment = float(row[3])
                continue

            new_level = float(row[1])

            # Staying at low level
            if current_level < threshold and new_level < threshold:
                steps_at_level += 1

            # Staying at high level
            elif current_level > threshold and new_level > threshold:
                steps_at_level += 1

            # Rising edge transition
            elif current_level < threshold and new_level > threshold:
                length = int(steps_at_level*increment*1000*1000)
                # print(f'transition at {int(row[0]):4}: {length:4} us low')
                raw.append(-length)
                steps_at_level = 1

            # Falling edge transition
            elif current_level >= threshold and new_level <= threshold:
                length = int(steps_at_level*increment*1000*1000)
                # print(f'transition at {int(row[0]):4}: {length:4} us high')
                raw.append(length)
                steps_at_level = 1

            current_level = new_level

    # print(f'transition at  END: {int(steps_at_level*increment*1000*1000):3} us {"high" if current_level > threshold else "low"}')

    # print(filename)
    print(f'{filename:12}: {raw[1:]}')

"""
get_pulses('singles/up.csv')
get_pulses('singles/upup.csv')
get_pulses('singles/uphold.csv')
get_pulses('singles/down.csv')
get_pulses('singles/downdown.csv')
get_pulses('singles/downhold.csv')
#"""
"""
get_pulses('on.csv')
get_pulses('off.csv')
get_pulses('up.csv')
get_pulses('down.csv')
"""

# On pulses
get_pulses('on/on00.csv')
get_pulses('on/on01.csv')
get_pulses('on/on02.csv')
get_pulses('on/on03.csv')
get_pulses('on/on04.csv')
get_pulses('on/on05.csv')
get_pulses('on/on06.csv')
get_pulses('on/on07.csv')
get_pulses('on/on08.csv')
get_pulses('on/on09.csv')
get_pulses('on/on10.csv')
get_pulses('on/on11.csv')
get_pulses('on/on12.csv')
get_pulses('on/on13.csv')
get_pulses('on/on14.csv')
get_pulses('on/on15.csv')
get_pulses('on/on16.csv')
get_pulses('on/on17.csv')

# Low pulses
get_pulses('low/low00.csv')
get_pulses('low/low01.csv')
get_pulses('low/low02.csv')
get_pulses('low/low03.csv')
get_pulses('low/low04.csv')
get_pulses('low/low05.csv')
get_pulses('low/low06.csv')
get_pulses('low/low07.csv')
get_pulses('low/low08.csv')
get_pulses('low/low09.csv')
get_pulses('low/low10.csv')
get_pulses('low/low11.csv')
get_pulses('low/low12.csv')
get_pulses('low/low13.csv')
get_pulses('low/low14.csv')
get_pulses('low/low15.csv')
get_pulses('low/low16.csv')
get_pulses('low/low17.csv')

# Up pulses
get_pulses('up/up0.csv')
get_pulses('up/up1.csv')
get_pulses('up/up2.csv')
get_pulses('up/up3.csv')
get_pulses('up/up4.csv')
get_pulses('up/up5.csv')
get_pulses('up/up6.csv')
get_pulses('up/up7.csv')
get_pulses('up/up8.csv')

# Down Pulses
get_pulses('down/down0.csv')
get_pulses('down/down1.csv')
get_pulses('down/down2.csv')
get_pulses('down/down3.csv')
get_pulses('down/down4.csv')
get_pulses('down/down5.csv')
get_pulses('down/down6.csv')
get_pulses('down/down7.csv')
get_pulses('down/down8.csv')
