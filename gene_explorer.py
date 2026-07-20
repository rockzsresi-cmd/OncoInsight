from Bio import Entrez

Entrez.email = "singhsresi@gmail.com"


def search_gene(gene_name):

    search = Entrez.esearch(
        db="gene",
        term=f"{gene_name}[Gene] AND Homo sapiens[Organism]"
    )

    result = Entrez.read(search)
    search.close()

    if not result["IdList"]:
        return None

    gene_id = result["IdList"][0]

    fetch = Entrez.efetch(
        db="gene",
        id=gene_id,
        rettype="xml"
    )

    records = Entrez.read(fetch)
    fetch.close()

    gene = records[0]

    info = {
        "Gene ID": gene_id,
        "Symbol": gene["Entrezgene_gene"]["Gene-ref"]["Gene-ref_locus"],
        "Description": gene["Entrezgene_gene"]["Gene-ref"].get(
            "Gene-ref_desc",
            "Not Available"
        ),
        "Organism": gene["Entrezgene_source"]["BioSource"][
            "BioSource_org"
        ]["Org-ref"]["Org-ref_taxname"]
    }

    return info