# vcf2fasta
Get a FASTA from a VCF file + reference FASTA file

## Usage
```bash
python vcf2fasta.py -v <VCF file from the sample> -f <reference FASTA file> -o <FASTA file from the sample>
```

## Limitations
- ONLY ONE SEQUENCE/CHROMOSOME PER VCF.
- DO NOT USE multiFASTA.
