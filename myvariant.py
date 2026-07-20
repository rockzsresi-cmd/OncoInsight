import requests


def search_myvariant(gene, variant):
    """
    Query MyVariant.info for variant annotations.

    Example:
    Gene: EGFR
    Variant: L858R
    """

    query = f"{gene} {variant}"

    url = "https://myvariant.info/v1/query"

    params = {
        "q": query,
        "size": 5
    }

    try:
        response = requests.get(url, params=params, timeout=15)

        if response.status_code == 200:
            data = response.json()

            if data.get("hits"):
                return data["hits"]

    except Exception as e:
        return {"error": str(e)}

    return []