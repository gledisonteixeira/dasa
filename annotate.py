import pandas as pd
import sys
import vcf

def annotate_vcf(input_vcf, output_csv):
    vcf_reader = vcf.Reader(open(input_vcf, 'r'))
    
    variants = []
    for record in vcf_reader:
        for alt in record.ALT:
            variant_info = {
                "CHROM": record.CHROM,
                "POS": record.POS,
                "ID": record.ID,
                "REF": record.REF,
                "ALT": str(alt),
                "QUAL": record.QUAL,
                "FILTER": record.FILTER,
                "GENE": "gene_example",  # Adicione lógica para obter o gene
                "dbSNP_ID": record.ID if record.ID.startswith('rs') else None,  # Simulação
                "FREQUENCY": 0.05  # Simulação; você pode integrar com um banco de dados real
            }
            variants.append(variant_info)

    df = pd.DataFrame(variants)
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    input_vcf = sys.argv[1]
    output_csv = sys.argv[2]
    annotate_vcf(input_vcf, output_csv)
