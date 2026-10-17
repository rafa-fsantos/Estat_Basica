"""
src: Pacote utilitário de rotinas analíticas, inferência e visualização.
"""

from .stats_utils import (
    criar_tabela_frequencias
)
# from .io_utils import (
#     load_data,
#     get_project_root,
# )
# from .viz import (
#     configurar_estilo,
#     plot_distribuicao,
# )

__version__ = "0.1.0"
__author__ = "Rafael Franco"

# Controla explicitamente o que é exportado via: from src import *
# Também orienta linters, IDEs (VS Code/PyCharm) e autocompletion
# __all__ = [
#     # Metadados
#     "__version__",
#     "__author__",
#     # Estatística & Inferência
#     "resumo_descritivo",
#     "identificar_outliers_iqr",
#     "ic_media",
#     "ic_proporcao",
#     "bootstrap_ci",
#     "verificar_normalidade",
#     # I/O & Caminhos
#     "load_data",
#     "get_project_root",
#     # Visualização
#     "configurar_estilo",
#     "plot_distribuicao",
# ]