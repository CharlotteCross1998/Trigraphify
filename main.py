import argparse, sys

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input" , required=True, help="Input file")
ap.add_argument("-o", "--output", required=True, help="Output file")
ap.add_argument("-v", "--verbose", required=False, help="Display Verbose Information", default=False)

args = ap.parse_args()

verbose = False

if isinstance(args.verbose, bool):
    verbose = args.verbose
else:
    if args.verbose.lower() in ('yes', 'y', 'true', '1'):
        verbose = True
    elif args.verbose.lower() in ('no', 'n', 'false', '0'):
        pass
    else:
        raise argparse.ArgumentTypeError('Boolean Value Expected [yes/y/true/1 | no/n/false/0]')

pairs = {'#' : '??=', '\\' : '??/', '^' : '??\'', '[' : '??(', ']' : '??)', '|' : '??!', '{' : '??<', '}' : '??>', '~' : '??-'}

output = ""

with open(args.input, 'r') as file:
    lineNumber = 0
    for line in file:
        if verbose:
            print("Parsing line " + str(lineNumber) + ": " + line.replace('\n', ''))
        for pair in pairs:
            if pair in line:
                if verbose:
                    print("Found \"" + pair + "\": Replacing with \"" + pairs[pair] + "\"")
                line = line.replace(pair, pairs[pair])
        lineNumber += 1
        output += line
        
with open(args.output, 'w') as file:
    file.write(output)
