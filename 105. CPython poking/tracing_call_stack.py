import dis
import io
import sys
import traceback


def trace(frame, event, args):
    frame.f_trace_opcodes = True
    stack = traceback.extract_stack(frame)
    pad = "   " * len(stack) + "|"
    if event == 'opcode':
        with io.StringIO() as out:
            dis.disco(frame.f_code, frame.f_lasti, file=out)
            lines = out.getvalue().split('\n')
            [print(f"{pad}{l}") for l in lines]
    elif event == 'call':
        print(f"{pad}Calling {frame.f_code}")
    elif event == 'return':
        print(f"{pad}Returning {args}")
    elif event == 'line':
        print(f"{pad}Changing line to {frame.f_lineno}")
    else:
        print(f"{pad}{frame} ({event} - {args})")
    print(f"{pad}----------------------------------")
    return trace


sys.settrace(trace)

# Run some code for a demo
eval('"-".join([letter for letter in "hello"])')
