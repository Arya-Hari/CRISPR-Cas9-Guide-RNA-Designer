import streamlit as st
from io import StringIO
from Bio.Seq import Seq
from fetchsequence import find_gRNAs
from sequencefeatures import calculate_gc_content, find_off_targets_scores

"""
# CRISPR-Cas9 Guide RNA Designer

This tool allows you to find appropriate guide RNA (gRNA) sequences for CRISPR-Cas9 gene editing.

Make appropriate choices for the below parameters :

"""

entering_file = st.checkbox("Are you manually entering a DNA sequence?")
sequence = ""

if entering_file:
    sequence = st.text_input("Enter DNA sequence : ")

if (entering_file is False):
    uploaded_file = st.file_uploader("Choose FASTA file : ", type="fasta")
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        sequence = stringio.read()

if sequence != "":
    gRNA_sequences, optimized_gRNA_sequences = find_gRNAs(sequence)
    st.write("Number of gRNA sequences identified :",len(gRNA_sequences))
    st.write("Number of optimized gRNA sequences identified :",len(optimized_gRNA_sequences))

    max_mismatches = st.slider("Maximum number of permissible mismatches : ", min_value = 0,max_value=20)
    max_off_targets = st.number_input("Maximum number of permissible off-targets : ",min_value=0)
    optimal_gc_content = st.slider("Optimal GC content (in %) : ",min_value=0,max_value=100)
    weight_gc_content = st.number_input("Weight for GC content (0-10) : ",min_value=0,max_value=10)
    weight_offtarget_score = st.number_input("Weight for off-target score (0-10) : ",min_value=0,max_value=10)

    if (weight_gc_content and weight_offtarget_score and optimal_gc_content):
        if ((weight_gc_content+weight_offtarget_score) != 10):
            st.write("Weights do not add up to 10. Enter proper weights")

        else:
            list_of_off_target_scores = []
            for (i) in optimized_gRNA_sequences:
                off_targets_scores = find_off_targets_scores(sequence,i,max_mismatches,max_off_targets)
                list_of_off_target_scores.append(off_targets_scores)

            gc_content_scores = []
            for (i) in optimized_gRNA_sequences:
                gc_content = calculate_gc_content(i,optimal_gc_content)
                gc_content_scores.append(gc_content)
            
            scores = []
            for (i) in range(len(optimized_gRNA_sequences)):
                score = (weight_gc_content/10)*gc_content_scores[i] + (weight_offtarget_score/10)*list_of_off_target_scores[i] 
                final_score = [score,optimized_gRNA_sequences[i]]
                scores.append(final_score)
            
            st.subheader("The optimized gRNA sequences sorted as per scores are : ")
            scores.sort(reverse=True)
            st.write(scores)
            st.write(optimized_gRNA_sequences)


        




