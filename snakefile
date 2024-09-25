# Snakefile
rule all:
    input: "output/annotated_variants.csv"

rule annotate_variants:
    input: "input/NIST.vcf"
    output: "output/annotated_variants.csv"
    shell:
        "python annotate.py {input} {output}"
