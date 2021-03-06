#usage
#python parse.xml.py <input.xml>  >  <output>
# 	0		1	     


import sys
import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

#input
result_handle = open(sys.argv[1], "r")
#result_handle = open("test.xml")

print ("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %("Query", "Alignment", "Identity(%)", "Similarity(%)", "Alignment length", "Expected value", "Score", "Length Query", "Length Subject"))

blast_records = NCBIXML.parse(result_handle)
for blast_record in blast_records:
   for alignment in blast_record.alignments:
      for hsp in alignment.hsps:
         pident = (hsp.identities) / float(hsp.align_length) * 100
         psimil = (hsp.positives) / float(hsp.align_length) * 100
         mygaps = str(hsp.gaps)
         print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %(blast_record.query, alignment.title, pident, psimil, hsp.align_length, hsp.expect, hsp.score, len(hsp.query), len(hsp.sbjct), mygaps)

result_handle.close()

