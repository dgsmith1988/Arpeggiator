import argparse
from string import Template

def generate_routing(number):
    mask = 1 << (number.bit_length() - 1)
    lowest_slot = 1
    new_routing = []
    while mask > 0:
        if (mask & number) == mask:
            new_routing.append(lowest_slot)
            lowest_slot += 1
        else:
            new_routing.append(0)
        mask >>= 1
    return new_routing

def convert_routing_to_mtrxctrl_message(routing_arg):
    mtrxctrl_messages = []
    number_of_outputs = len(routing_arg)
    s = Template('$col $row 1')
    for i in range(0, number_of_outputs):
        if routing_arg[i] != 0:
            mtrxctrl_messages.append(s.substitute(col=str(routing_arg[i]-1), row=str(i)))
        else:
            mtrxctrl_messages.append(s.substitute(col=str(number_of_outputs), row=str(i)))
    return mtrxctrl_messages

parser = argparse.ArgumentParser()
parser.add_argument("number_of_notes", type=int, help="number of notes in the arpeggiator which can be toggled")
parser.add_argument("output_file", help="output .txt file to store the lookup table in")
args = parser.parse_args()

# the first solution will be all zeros
lookup_table = [[0] * args.number_of_notes]

for i in range(1, 2 ** args.number_of_notes):
    routing = generate_routing(i)
    while len(routing) != args.number_of_notes:
        routing.insert(0, 0)
    lookup_table.append(routing)

routing_messages = []
for routing in (lookup_table):
    print(routing, ' = ', convert_routing_to_mtrxctrl_message(routing))
    routing_messages.append(convert_routing_to_mtrxctrl_message(routing))

# save the files to a text document
f = open(args.output_file, 'w')
i = 0
for message in routing_messages:
    f.write(str(i)+',')
    i += 1
    for routing in message:
        f.write(' ' + routing)
    f.write(";\n")

f.close()