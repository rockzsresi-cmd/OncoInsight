import streamlit as st
import pandas as pd

from sequence import analyze_sequence
from gene_explorer import search_gene
from mutation_analyzer import compare_sequences
from gene_expression import analyze_expression
from clinical_variant import search_variant
from report_generator import generate_clinical_report
from myvariant import search_myvariant

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="OncoInsight",
    page_icon="🧬",
    layout="wide"
)

# ----------------------------------
# Sidebar
# ----------------------------------

st.sidebar.title("OncoInsight")

st.sidebar.caption(
    "Integrated Cancer Bioinformatics Platform"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Sequence Analyzer",
        "Gene Explorer",
        "Mutation Analyzer",
        "Gene Expression",
        "Clinical Variant Explorer",
        "About"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### Platform")

st.sidebar.write("Version : **0.5 Beta**")
st.sidebar.write("Modules : **5**")
st.sidebar.write("Databases : **2**")

st.sidebar.divider()

st.sidebar.caption("Developed by")

st.sidebar.write("**Ms. Sresi Singh**")

# ----------------------------------
# Home
# ----------------------------------

if page == "Home":

    st.title("OncoInsight")

    st.subheader(
        "Integrated Cancer Bioinformatics Platform"
    )

    st.write("""
OncoInsight is an integrated bioinformatics platform developed to assist researchers and students in sequence analysis, mutation detection, gene exploration, gene expression analysis and clinically relevant variant interpretation.

The objective of the platform is to provide a unified environment for cancer bioinformatics research using Python, Streamlit and Biopython.
""")

    st.divider()

    # ----------------------------------
    # Platform Overview
    # ----------------------------------

    st.subheader("Platform Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Modules",
        "5"
    )

    c2.metric(
        "Databases",
        "2"
    )

    c3.metric(
        "Analysis Tools",
        "5"
    )

    c4.metric(
        "Version",
        "0.5 Beta"
    )

    st.divider()

    # ----------------------------------
    # Available Modules
    # ----------------------------------

    st.subheader("Available Modules")

    left, right = st.columns(2)

    with left:

        st.success("Sequence Analyzer")

        st.write(
            "Analyze DNA sequences, nucleotide composition, GC content, reverse complements and translated protein sequences."
        )

        st.success("Gene Explorer")

        st.write(
            "Retrieve curated gene information directly from the NCBI Gene database."
        )

        st.success("Mutation Analyzer")

        st.write(
            "Compare normal and mutated DNA sequences, identify mutations and generate biological interpretations."
        )

    with right:

        st.success("Gene Expression Analysis")

        st.write(
            "Visualize gene expression datasets, calculate summary statistics and download results."
        )

        st.success("Clinical Variant Explorer")

        st.write(
            "Explore clinically relevant variants, associated diseases, targeted therapies and supporting evidence."
        )

    st.divider()

    # ----------------------------------
    # Technology Stack
    # ----------------------------------

    st.subheader("Technology Stack")

    t1, t2, t3 = st.columns(3)

    with t1:

        st.markdown("""
**Programming**

- Python
- Streamlit
""")

    with t2:

        st.markdown("""
**Libraries**

- Biopython
- Pandas
""")

    with t3:

        st.markdown("""
**Databases**

- NCBI Entrez
- Clinical Variant Dataset
""")

    st.divider()

    # ----------------------------------
    # Project Vision
    # ----------------------------------

    st.subheader("Project Vision")

    st.info("""
OncoInsight aims to provide researchers and students with a unified bioinformatics platform integrating molecular sequence analysis, mutation detection, gene exploration, expression profiling and clinical variant interpretation. Future versions will incorporate live biomedical databases, literature integration, downloadable PDF reports and advanced visualization tools.
""")

    st.divider()

    st.caption(
        "OncoInsight • Version 0.5 Beta • Developed by Ms. Sresi Singh"
    )

# ----------------------------------
# Sequence Analyzer
# ----------------------------------

elif page == "Sequence Analyzer":
    st.title("Sequence Analyzer")

    st.write(
        """
Analyze DNA sequences uploaded in FASTA format. This module calculates
sequence length, GC content, nucleotide composition, reverse complements,
and translated protein sequences.
"""
    )

    st.divider()

    # ----------------------------------
    # Upload FASTA File
    # ----------------------------------

    st.subheader("Upload Sequence")

    uploaded_file = st.file_uploader(
        "Upload a FASTA file",
        type=["fasta", "fa"]
    )

    if uploaded_file is not None:

        result = analyze_sequence(uploaded_file)

        st.success("Sequence analysis completed successfully.")

        st.divider()

        # ----------------------------------
        # Sequence Summary
        # ----------------------------------

        st.subheader("Sequence Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Sequence Length",
                f"{result['Length']} bp"
            )

        with col2:

            st.metric(
                "GC Content",
                f"{result['GC']} %"
            )

        st.divider()

        # ----------------------------------
        # Nucleotide Composition
        # ----------------------------------

        st.subheader("Nucleotide Composition")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("A", result["A"])
        c2.metric("T", result["T"])
        c3.metric("G", result["G"])
        c4.metric("C", result["C"])

        chart_data = pd.DataFrame(
            {
                "Nucleotide": ["A", "T", "G", "C"],
                "Count": [
                    result["A"],
                    result["T"],
                    result["G"],
                    result["C"]
                ]
            }
        )

        st.bar_chart(
            chart_data.set_index("Nucleotide")
        )

        st.divider()

        # ----------------------------------
        # DNA Sequence
        # ----------------------------------

        st.subheader("DNA Sequence")

        st.text_area(
            "Uploaded DNA Sequence",
            result["Sequence"],
            height=180
        )

        st.divider()

        # ----------------------------------
        # Reverse Complement
        # ----------------------------------

        st.subheader("Reverse Complement")

        st.code(
            result["Reverse Complement"],
            language="text"
        )

        st.divider()

        # ----------------------------------
        # Protein Translation
        # ----------------------------------

        st.subheader("Protein Translation")

        st.code(
            result["Protein"],
            language="text"
        )

        st.divider()

        # ----------------------------------
        # Download Results
        # ----------------------------------

        st.subheader("Download Results")

        st.download_button(
            label="Download DNA Sequence",
            data=result["Sequence"],
            file_name="sequence.txt",
            mime="text/plain"
        )

        st.divider()

        st.caption(
            "OncoInsight • Version 0.5 Beta • Developed by Ms. Sresi Singh"
        )

# ----------------------------------
# Gene Explorer
# ----------------------------------

elif page == "Gene Explorer":

    st.title("Gene Explorer")

    st.write(
        """
Search the NCBI Gene database to retrieve curated information
about human genes including gene symbols, descriptions,
organisms and Gene IDs.
"""
    )

    st.divider()

    st.subheader("Gene Search")

    gene_name = st.text_input(
        "Enter Gene Symbol",
        placeholder="Example: TP53, BRCA1, EGFR"
    )

    if st.button("Search Gene"):

        if gene_name.strip():

            with st.spinner("Searching NCBI Database..."):

                gene = search_gene(gene_name)

            if gene:

                st.success("Gene Found")

                st.divider()

                st.subheader("Gene Summary")

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Gene Symbol",
                        gene["Symbol"]
                    )

                    st.metric(
                        "NCBI Gene ID",
                        gene["Gene ID"]
                    )

                with col2:

                    st.metric(
                        "Organism",
                        gene["Organism"]
                    )

                st.divider()

                st.subheader("Gene Description")

                st.info(
                    gene["Description"]
                )

            else:

                st.error(
                    "No matching gene found."
                )

        else:

            st.warning(
                "Please enter a gene symbol."
            )

    st.divider()

    st.caption(
        "OncoInsight • Version 0.5 Beta • Developed by Ms. Sresi Singh"
    )

# ----------------------------------
# Mutation Analyzer
# ----------------------------------

elif page == "Mutation Analyzer":

    st.title("Mutation Analyzer")

    st.write(
        """
Compare reference and mutated DNA sequences to identify
sequence variations, calculate mutation statistics and
generate biological interpretations.
"""
    )

    st.divider()

    st.subheader("Upload Sequences")

    normal_file = st.file_uploader(
        "Upload Normal FASTA",
        type=["fasta", "fa"],
        key="normal"
    )

    mutant_file = st.file_uploader(
        "Upload Mutated FASTA",
        type=["fasta", "fa"],
        key="mutant"
    )

    if normal_file and mutant_file:

        result = compare_sequences(
            normal_file,
            mutant_file
        )

        st.success("Mutation analysis completed successfully.")

        st.divider()

        # ----------------------------------
        # Summary
        # ----------------------------------

        st.subheader("Mutation Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Total Mutations",
            result["Total"]
        )

        c2.metric(
            "Mutation Rate",
            f"{result['Mutation Rate']} %"
        )

        c3.metric(
            "Mutation Type",
            result["Mutation Type"]
        )

        st.divider()

        # ----------------------------------
        # DNA Sequences
        # ----------------------------------

        st.subheader("DNA Sequences")

        col1, col2 = st.columns(2)

        with col1:

            st.text_area(
                "Reference Sequence",
                result["Normal Sequence"],
                height=180
            )

        with col2:

            st.text_area(
                "Mutated Sequence",
                result["Mutant Sequence"],
                height=180
            )

        st.divider()

        # ----------------------------------
        # Protein Translation
        # ----------------------------------

        st.subheader("Protein Translation")

        col1, col2 = st.columns(2)

        with col1:

            st.code(
                result["Normal Protein"]
            )

        with col2:

            st.code(
                result["Mutant Protein"]
            )

        st.divider()

        # ----------------------------------
        # Mutation Table
        # ----------------------------------

        if result["Total"] == 0:

            st.success(
                "No mutations detected."
            )

        else:

            st.subheader("Detected Mutations")

            st.dataframe(
                result["Mutations"],
                use_container_width=True
            )

        st.divider()

        # ----------------------------------
        # Biological Interpretation
        # ----------------------------------

        st.subheader("Biological Interpretation")

        st.info(
            result["Interpretation"]
        )

        st.warning(
            "This analysis is intended for research and educational purposes only. "
            "The results should not be used for clinical diagnosis or treatment decisions."
        )

        st.divider()

        st.download_button(
            label="Download Mutation Table",
            data=pd.DataFrame(
                result["Mutations"]
            ).to_csv(index=False),
            file_name="mutation_results.csv",
            mime="text/csv"
        )

    st.divider()

    st.caption(
        "OncoInsight • Version 0.5 Beta • Developed by Ms. Sresi Singh"
    )

# ----------------------------------
# Gene Expression
# ----------------------------------

elif page == "Gene Expression":
    st.title("Gene Expression Analysis")

    st.write(
        """
Analyze gene expression datasets, visualize expression profiles,
identify highly expressed genes and export results for downstream
analysis.
"""
    )

    st.divider()

    st.subheader("Upload Dataset")

    uploaded_csv = st.file_uploader(
        "Upload Gene Expression CSV",
        type=["csv"]
    )

    if uploaded_csv is not None:

        try:

            result = analyze_expression(uploaded_csv)

            st.success("Gene expression analysis completed successfully.")

            st.divider()

            # ----------------------------------
            # Summary Statistics
            # ----------------------------------

            st.subheader("Expression Summary")

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Highest Expressed Gene",
                result["Highest Gene"],
                f"{result['Highest Expression']}"
            )

            c2.metric(
                "Lowest Expressed Gene",
                result["Lowest Gene"],
                f"{result['Lowest Expression']}"
            )

            c3.metric(
                "Average Expression",
                result["Average Expression"]
            )

            st.divider()

            # ----------------------------------
            # Expression Chart
            # ----------------------------------

            st.subheader("Expression Profile")

            chart = result["Data"].sort_values(
                by="Expression",
                ascending=False
            )

            st.bar_chart(
                chart.set_index("Gene")["Expression"]
            )

            st.divider()

            # ----------------------------------
            # Search Gene
            # ----------------------------------

            st.subheader("Search Gene")

            gene_search = st.text_input(
                "Enter Gene Name"
            )

            display_df = result["Data"]

            if gene_search:

                display_df = display_df[
                    display_df["Gene"].str.contains(
                        gene_search,
                        case=False
                    )
                ]

            st.dataframe(
                display_df,
                use_container_width=True
            )

            st.divider()

            st.download_button(
                label="Download Expression Results",
                data=display_df.to_csv(index=False),
                file_name="gene_expression_results.csv",
                mime="text/csv"
            )

        except Exception as e:

            st.error(str(e))

    st.divider()

    st.caption(
        "OncoInsight • Version 0.5 Beta • Developed by Ms. Sresi Singh"
    )

# ----------------------------------
# Clinical Variant Explorer
# ----------------------------------

elif page == "Clinical Variant Explorer":

    st.title("Clinical Variant Explorer")

    st.write("""
Search clinically relevant genetic variants and retrieve associated disease
information, targeted therapies, clinical evidence and supporting resources.
""")

    st.divider()

    # ----------------------------------
    # Variant Search
    # ----------------------------------

    st.subheader("Variant Search")

    gene = st.text_input(
        "Gene Symbol",
        placeholder="Example: EGFR"
    )

    variant = st.text_input(
        "Protein Variant",
        placeholder="Example: L858R"
    )

    if st.button("Search Variant"):

        if gene and variant:

                        result = search_variant(
                gene,
                variant
            )

            st.write("Gene entered:", gene)
            st.write("Variant entered:", variant)
            st.write(result)

            if not result.empty:

            if not result.empty:

                row = result.iloc[0]

                st.success("Variant Found")

                st.divider()

                # ----------------------------------
                # Clinical Evidence Summary
                # ----------------------------------

                st.subheader("Clinical Evidence Summary")

                st.info(f"""
**Clinical Significance:** {row['Clinical Significance']}

**Evidence Source:** {row['Evidence']}

**Associated Disease:** {row['Disease']}

**Recommended Therapy:** {row['Therapy']}
""")

                st.divider()

                # ----------------------------------
                # Clinical Summary
                # ----------------------------------

                st.subheader("Clinical Summary")

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Gene",
                        row["Gene"]
                    )

                    st.metric(
                        "Variant",
                        row["Variant"]
                    )

                    st.metric(
                        "Disease",
                        row["Disease"]
                    )

                with col2:

                    st.metric(
                        "Clinical Significance",
                        row["Clinical Significance"]
                    )

                    st.metric(
                        "Therapy",
                        row["Therapy"]
                    )

                    st.metric(
                        "Evidence",
                        row["Evidence"]
                    )

                st.divider()

                # ----------------------------------
                # Therapeutic Summary
                # ----------------------------------

                st.subheader("Therapeutic Summary")

                st.success(f"""
### Recommended Targeted Therapy

**{row['Therapy']}**

The identified variant is currently associated with the above targeted
therapy according to the curated clinical dataset available within
OncoInsight.

Treatment decisions should always be confirmed using current clinical
guidelines and multidisciplinary clinical evaluation.
""")

                st.divider()

                # ----------------------------------
                # Clinical Interpretation
                # ----------------------------------

                st.subheader("Clinical Interpretation")

                st.info(f"""
The **{row['Gene']} {row['Variant']}** variant is associated with
**{row['Disease']}**.

Current evidence classifies this variant as
**{row['Clinical Significance']}**.

Potential targeted therapy includes
**{row['Therapy']}**.

Clinical interpretation should always consider molecular findings,
patient history, tumour characteristics and current evidence-based
clinical guidelines.
""")

                st.divider()

                # ----------------------------------
                # Clinical Recommendations
                # ----------------------------------

                st.subheader("Clinical Recommendations")

                st.warning("""
• Confirm the detected variant using a validated molecular diagnostic assay.

• Correlate molecular findings with the patient's clinical presentation.

• Review current NCCN, ESMO or institutional treatment guidelines.

• Consider targeted therapy when clinically appropriate.

• Discuss complex cases within a multidisciplinary molecular tumour board whenever possible.
""")

                st.divider()

                # ----------------------------------
                # Variant Details
                # ----------------------------------

                st.subheader("Variant Details")

                st.dataframe(
                    result,
                    use_container_width=True
                )

                st.divider()

                # ----------------------------------
                # External Resources
                # ----------------------------------

                st.subheader("External Resources")

                clinvar_url = (
                    f"https://www.ncbi.nlm.nih.gov/clinvar/?term={row['Gene']}+{row['Variant']}"
                )

                pubmed_url = (
                    f"https://pubmed.ncbi.nlm.nih.gov/?term={row['Gene']}+{row['Variant']}"
                )

                civic_url = (
                    f"https://civicdb.org/search/variants?query={row['Gene']}"
                )

                c1, c2, c3 = st.columns(3)

                with c1:
                    st.link_button(
                        "Open ClinVar",
                        clinvar_url
                    )

                with c2:
                    st.link_button(
                        "Search PubMed",
                        pubmed_url
                    )

                with c3:
                    st.link_button(
                        "Open CIViC",
                        civic_url
                    )

                st.divider()

                # ----------------------------------
                # Download Report
                # ----------------------------------

                st.subheader("Download Report")

                report = f"""
==============================
ONCOINSIGHT CLINICAL REPORT
==============================

Gene:
{row['Gene']}

Variant:
{row['Variant']}

Disease:
{row['Disease']}

Clinical Significance:
{row['Clinical Significance']}

Recommended Therapy:
{row['Therapy']}

Evidence Source:
{row['Evidence']}

Clinical Interpretation

The {row['Gene']} {row['Variant']} variant is associated with
{row['Disease']}.

Current evidence classifies this variant as
{row['Clinical Significance']}.

Potential targeted therapy includes
{row['Therapy']}.

Disclaimer

This report is intended for research and educational
purposes only and should not be used as a substitute
for professional medical advice or clinical decision-making.

Generated using OncoInsight v0.5 Beta

Developer:
Ms. Sresi Singh

Project Supervisor:
Dr. Mohd Tashfeen Ashraf
"""

                pdf_buffer = generate_clinical_report(row)

                st.download_button(
                    label="Download Clinical Report (PDF)",
                    data=pdf_buffer,
                    file_name="OncoInsight_Clinical_Report.pdf",
                    mime="application/pdf"
                )

            else:

                st.error(
                    "No matching variant was found in the current clinical variant database."
                )

        else:

            st.warning(
                "Please enter both Gene Symbol and Protein Variant."
            )

    st.divider()

    st.caption(
        "OncoInsight • Version 0.5 Beta • Developed by Ms. Sresi Singh"
    )


# ----------------------------------
# Project Information
# ----------------------------------

elif page == "About":

    st.title("Project Information")

    st.write("""
## OncoInsight

OncoInsight is an integrated cancer bioinformatics platform
developed to assist researchers and students in sequence
analysis, mutation detection, gene exploration, gene
expression analysis and clinical variant interpretation.

---

### Developer

**Ms. Sresi Singh**

---

### Project Supervisor

**Dr. Mohd Tashfeen Ashraf**

---

### Technology Stack

- Python
- Streamlit
- Biopython
- Pandas
- NCBI Entrez

---

### Current Modules

- Sequence Analyzer
- Gene Explorer
- Mutation Analyzer
- Gene Expression Analysis
- Clinical Variant Explorer

---

### Upcoming Features

- Live ClinVar Integration
- MyVariant.info Integration
- PDF Report Generation
- PubMed Literature Search
- Protein Structure Visualization
- Streamlit Cloud Deployment

---

Version **0.5 Beta**
""")

