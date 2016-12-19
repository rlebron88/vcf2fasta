# vcf2fasta
Get a FASTA from a VCF file + reference FASTA file.

**It works with SNVs and indels.**

## Usage
```bash
python vcf2fasta.py -v <VCF file from the sample> -f <reference FASTA file> -o <FASTA file from the sample>
```

## Limitations
- ONLY ONE SEQUENCE/CHROMOSOME PER VCF.
- USE "X" TO REFER TO THE SEQUENCE OF REF IN THE VCF FILE.
- IF THERE IS MORE THAN ONE ALT, THE FIRST IS USED.
- DO NOT USE multiFASTA.
