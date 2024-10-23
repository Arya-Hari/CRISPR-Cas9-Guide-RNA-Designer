import subprocess
import os

def mismatch(potential_off_target,sequence):
    mismatches = 0
    for (i) in range(0,23):
        if potential_off_target[i] != sequence[i]:
            mismatches+=1
    return mismatches

def find_off_targets_scores(sequence, sub_sequence, max_mismatches, max_off_targets):
    count = 0
    for j in range(len(sequence)-1):
        if (j>20):
            potential_off_target = sequence[j-20-1:j+2]
            if (potential_off_target[20:23] == sub_sequence[20:23]):
                mismatches = mismatch(potential_off_target,sub_sequence)
                if (mismatches <= max_mismatches):
                    count+=1
    if (count > max_off_targets):
        
        score = 0
    else:
        score = 10 - (count/max_off_targets)*10
    return score

def calculate_gc_content(sequence,optimal_gc_content):
    gc_count = sequence.count('G') + sequence.count('C')
    gc_content = int((gc_count / len(sequence)) * 100)
    score = 10 - abs(gc_content - optimal_gc_content) / optimal_gc_content * 10
    return max(0,score)





