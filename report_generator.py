from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER


def generate_clinical_report(row):
    """
    Generates a PDF report for a clinical variant.

    Parameters
    ----------
    row : pandas.Series
        A row returned from the Clinical Variant Explorer.

    Returns
    -------
    BytesIO
        PDF stored in memory.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading = styles["Heading2"]
    normal = styles["BodyText"]

    elements = []

    # --------------------------------------------------
    # Title
    # --------------------------------------------------

    elements.append(Paragraph("ONCOINSIGHT", title_style))
    elements.append(
        Paragraph(
            "Integrated Cancer Bioinformatics Platform",
            normal
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Clinical Variant Report",
            heading
        )
    )

    elements.append(Spacer(1, 15))

    # --------------------------------------------------
    # Clinical Summary
    # --------------------------------------------------

    elements.append(
        Paragraph("<b>Gene:</b> " + row["Gene"], normal)
    )

    elements.append(
        Paragraph("<b>Variant:</b> " + row["Variant"], normal)
    )

    elements.append(
        Paragraph("<b>Disease:</b> " + row["Disease"], normal)
    )

    elements.append(
        Paragraph(
            "<b>Clinical Significance:</b> " +
            row["Clinical Significance"],
            normal
        )
    )

    elements.append(
        Paragraph(
            "<b>Therapy:</b> " +
            row["Therapy"],
            normal
        )
    )

    elements.append(
        Paragraph(
            "<b>Evidence:</b> " +
            row["Evidence"],
            normal
        )
    )

    elements.append(Spacer(1, 20))

    # --------------------------------------------------
    # Interpretation
    # --------------------------------------------------

    interpretation = f"""
    The {row['Gene']} {row['Variant']} variant is associated with
    {row['Disease']}.

    Current evidence classifies this variant as
    {row['Clinical Significance']}.

    Recommended targeted therapy includes
    {row['Therapy']}.

    This report is intended for research and educational purposes only.
    """

    elements.append(
        Paragraph(
            "<b>Clinical Interpretation</b>",
            heading
        )
    )

    elements.append(
        Paragraph(
            interpretation,
            normal
        )
    )

    elements.append(Spacer(1, 20))

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    elements.append(
        Paragraph(
            "<b>Developer:</b> Ms. Sresi Singh",
            normal
        )
    )

    elements.append(
        Paragraph(
            "<b>Project Supervisor:</b> Dr. Mohd Tashfeen Ashraf",
            normal
        )
    )

    doc.build(elements)

    buffer.seek(0)

    return buffer