"""
viz.py
Configurações básicas de identidade visual e estilo para Matplotlib e Seaborn.
"""

from pathlib import Path
from typing import Optional
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore


def set_style(
    style: str = "whitegrid",
    palette: str = "deep",
    font_scale: float = 1.0,
    despine: bool = True
) -> None:
    """
    Aplica configurações visuais limpas para todos os gráficos do projeto.
    """
    # Tema base do Seaborn
    sns.set_theme(
        style=style,
        palette=palette,
        font_scale=font_scale
    )

    # Ajustes finos no Matplotlib rcParams
    plt.rcParams.update({
        "figure.dpi": 120,
        "figure.figsize": (8, 4.5),
        "figure.autolayout": True,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.labelsize": 10,
        "axes.edgecolor": "#cccccc",
        "axes.linewidth": 0.8,
        "grid.color": "#e0e0e0",
        "grid.linestyle": "--",
        "grid.alpha": 0.7,
        "legend.frameon": True,
        "legend.facecolor": "white",
        "legend.framealpha": 0.85
    })

    # Remove bordas superior e direita por padrão
    if despine:
        plt.rcParams.update({
            "axes.spines.top": False,
            "axes.spines.right": False
        })


def save_fig(
    fig: plt.Figure,
    filepath: str,
    dpi: int = 300,
    transparent: bool = False
) -> None:
    """
    Salva uma figura criando os diretórios necessários automaticamente.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, transparent=transparent, bbox_inches="tight")
