import time, sys

indent = 0
indent_increase = True # indent starts with increasing

try:
    while True:
        print(' ' * indent, end='') # end = '' means the print statement won't make a new line
        print('********')
        time.sleep(0.1) # pauses for 1/10 of a second

        if indent_increase:
            indent = indent + 1
            if indent == 20:
                indent_increase = False # changes direction of the indent
        else:
            indent = indent - 1 # this is the False case
            if indent == 0:
                indent_increase = True # change direction again
except KeyboardInterrupt:
    sys.exit()