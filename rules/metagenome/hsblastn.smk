rule hs_blastn:
	input:
		nonhumanfa = 'sample_output/nonhuman_fasta/{read}/{sample}_{read}.fa',
		db = 'databases/blast/{conversion}_conversion/NCBIGenomes06_{conversion}.fna',
		gi_to_taxid = 'databases/blast/NCBIGenomes06.gis.taxids',
		grammy_db_proof = 'logs/grammy/grammy_prompts_{conversion}',
		obinary = 'databases/blast/{conversion}_conversion/NCBIGenomes06_{conversion}.fna.counts.obinary'
	output:
		blast_outfmt6 = 'sample_output/blast/{conversion}_genome/{read}/{sample}.{read}.outfmt6'
	threads: blast_threads
	resources:
		mem_mb=20000
	shell:
		"""
		{HSBLASTN} align -query {input.nonhumanfa} \
                        -db {input.db} \
                        -evalue 0.0001 \
                        -perc_identity 95 \
                        -num_threads {threads} \
                        -outfmt 6 | python scripts/metagenome/get_taxid_filter_strand.py {output.blast_outfmt6} {input.gi_to_taxid} {wildcards.conversion}
		"""
								#-window_masker_db {input.obinary} \

rule filter_blastn:
	input:
		GA_genomeR1 = 'sample_output/blast/GA_genome/R1/{sample}.R1.outfmt6',
		GA_genomeR2 = 'sample_output/blast/GA_genome/R2/{sample}.R2.outfmt6',
		CT_genomeR1 = 'sample_output/blast/CT_genome/R1/{sample}.R1.outfmt6',
		CT_genomeR2 = 'sample_output/blast/CT_genome/R2/{sample}.R2.outfmt6',
		taxid_lengths = 'databases/GenomeDB/taxids_lengths.txt'
	output:
		tblatGA= 'sample_output/blast/consolidated_blast/{sample}.GA.pe',
		tblatCT= 'sample_output/blast/consolidated_blast/{sample}.CT.pe',
		tblatpe= 'sample_output/blast/consolidated_blast/{sample}.tblat.pe',
		tblat1 = 'sample_output/grammy/{sample}/{sample}.tblat.1'
	shell:
		"""
		Rscript scripts/metagenome/filter_paired_end_blast.R {input.GA_genomeR1} {input.GA_genomeR2} {output.tblatGA} {input.taxid_lengths}
		Rscript scripts/metagenome/filter_paired_end_blast.R {input.CT_genomeR1} {input.CT_genomeR2} {output.tblatCT} {input.taxid_lengths}

		Rscript scripts/metagenome/consolidate_GA_CT_reads.R {output.tblatGA} {output.tblatCT} {output.tblatpe} {output.tblat1}
		"""
