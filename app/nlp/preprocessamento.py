import re
import unicodedata

ABREVIACOES = {
    "qto": "quanto",
    "vcs": "voces",
    "pra": "para",
    "vc": "você",
    "blz": "beleza",
    "vlw": "valeu",
    "oq": "o que"
}

def remover_acentos(texto: str) -> str:
    separado = unicodedata.normalize("NFD", texto)
    return "".join(c for c in separado if unicodedata.category(c) != "Mn")


def normalizar(texto: str) -> str:
    texto = texto.lower()
    texto = remover_acentos(texto)
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    palavras = [ABREVIACOES.get(p, p) for p in texto.split()]
    return " ".join(palavras)