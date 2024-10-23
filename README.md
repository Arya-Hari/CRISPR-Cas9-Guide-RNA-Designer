# CRISPR-Cas9-Guide-RNA-Designer

The **CRISPR-Cas9 Guide RNA Designer** is a bioinformatics tool that allows users to input a DNA sequence and retrieve guide RNA (gRNA) sequences optimized for CRISPR-Cas9 gene editing. Built using Python and Streamlit, this tool ranks the extracted gRNAs based on several key metrics to help users identify the most suitable candidates for their genetic editing needs.

## Tech Stack
- **Python**: Core programming language.
- **Streamlit**: Framework for building the UI.

## Methodology
1. Accepts an input DNA sequence from the user.
2. Analyzes the sequence to extract potential gRNAs.
3. Ranks the gRNAs based on:
   - **GC Content**: Measures the proportion of guanine (G) and cytosine (C) nucleotides.
   - **Off-target Count**: Calculates the potential for off-target activity with a specified number of mismatches.
   - **Preferred Positions**: Evaluates the presence of adenine (A), guanine (G), or cytosine (C) in preferred positions within the sequence.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/CRISPR-Cas9-gRNA-Designer.git
   ```
   Ensure the required dependencies are installed.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Input your DNA sequence into the interface and get ranked gRNA sequences.

## Contributors
- Arya Hariharan
- B H Abhisha
- Bhumika K

## Mentor
- Dr. Narendra Kumar S, Department of Biotechnology, RVCE
