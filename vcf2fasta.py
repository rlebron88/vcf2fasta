import os, argparse, re

class Full_paths(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, os.path.abspath(os.path.expanduser(values)))

def readable_file(filename):
    if not all([os.path.isfile(filename), os.access(filename, os.R_OK)]):
        msg = "{0} is not a readable file".format(filename)
        raise argparse.ArgumentTypeError(msg)
    else:
        return filename

def writable_path(filename):
    if all([os.path.isdir(filename), os.path.isfile(filename) and not os.access(filename, os.W_OK)]):
        raise argparse.ArgumentTypeError('{0} is not a writable path'.format(filename))
    else:
        return filename

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--vcf', required=True, help='VCF file from the sample. ONLY ONE SEQUENCE/CHROMOSOME PER VCF.', action=Full_paths, type=readable_file) 
parser.add_argument('-f', '--fasta', required=True, help='reference FASTA file. DO NOT USE multiFASTA.', action=Full_paths, type=readable_file)
parser.add_argument('-o', '--output', required=True, help='FASTA file from the sample. ONLY ONE SEQUENCE/CHROMOSOME.', action=Full_paths, type=writable_path)
args = parser.parse_args()

# TODO:
# - multiFASTA support
# - '.' as ref support
# - alt == ref support
# - more than one alt support

fasta_handle = open(args.fasta, 'rt')
fasta_handle.readline()
seq = list(re.sub(r'\s+', '', fasta_handle.read()))
fasta_handle.close()

vcf_handle = open(args.vcf, 'rt')
for line in vcf_handle:
    if line[0] != '#':
        line = line.strip().split()
        chrom, start, end, alt = line[0], int(line[1])-1, int(line[1])-1 + len(line[3]), line[4].replace(',X','').replace('X,','').split(',')[0]
        if alt != 'X':
            for pos in range(start, end):
                seq[pos] = ''
            seq[start] = alt
vcf_handle.close()

output_handle = open(args.output, 'wt')
output_handle.write('>{}\n'.format(os.path.basename(args.output).split('.')[0]))
output_handle.write(''.join(seq) + '\n')