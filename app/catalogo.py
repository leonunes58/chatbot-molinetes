"""Leitura do catálogo e formatação de valores."""
from functools import lru_cache
from pathlib import Path

import yaml

CAMINHO_CATALOGO = Path(__file__).resolve().parents[1] / "data" / "catalogo.yaml"


@lru_cache
def carregar() -> dict:
    return yaml.safe_load(CAMINHO_CATALOGO.read_text(encoding="utf-8"))


def formatar_preco(valor) -> str:
    if valor is None:
        return "sob avaliação"
    # 1234.5 -> "R$ 1.234,50" (formato brasileiro)
    return "R$ " + f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_prazo(dias) -> str:
    return "após avaliação" if dias is None else f"{dias} dias úteis"
