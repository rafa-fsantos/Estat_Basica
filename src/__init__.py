"""
src: Pacote utilitário de rotinas analíticas, inferência e visualização.
"""

from .stats_utils import (
    criar_tabela_frequencias
)
from .io_utils import (
    get_project_root,
    get_data_path,
    load_data,
    save_data
)
from .viz import (
    set_style,
    save_fig,
)

__version__ = "0.1.0"
__author__ = "Rafael Franco"

# Controla explicitamente o que é exportado via: from src import *
# Também orienta linters, IDEs (VS Code/PyCharm) e autocompletion
__all__ = [
    # Metadados
    "__version__",
    "__author__",
    # Estatística & Inferência
    "criar_tabela_frequencias",
    # I/O & Caminhos
    "load_data",
    "save_data",
    # Visualização
    "set_style",
    "save_fig",
]