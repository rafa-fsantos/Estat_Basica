"""
stats_utils.py
Módulo utilitário genérico com rotinas de análise estatística descritiva,
inferencial, testes de aderência e reamostragem bootstrap.
"""

from typing import Any, Callable, Dict, Optional, Tuple, Union
import numpy as np # type: ignore
import pandas as pd # pyright: ignore[reportMissingModuleSource]
from scipy import stats # pyright: ignore[reportMissingImports]


ArrayLike = Union[pd.Series, np.ndarray, list]


def _to_clean_1d_array(data: ArrayLike) -> np.ndarray:
    """Valida, converte para array 1D float e descarta valores nulos."""
    arr = np.asanyarray(data, dtype=float).ravel()
    return arr[~np.isnan(arr)]


# ==============================================================================
# 1. Análise Exploratória de Dados (EDA)
# ==============================================================================

# Função para criar uma tabela de frequências
import pandas as pd # type: ignore


def criar_tabela_frequencias(dados: pd.Series, ordem_categorias=None) -> pd.DataFrame:
    """Gera uma tabela de distribuição de frequências para uma série de dados.

    Calcula a frequência absoluta, a frequência relativa (proporção) e a
    porcentagem de cada categoria, adicionando uma linha final com os totais.

    Parâmetros:
    -----------
    dados : pd.Series
        Série contendo os dados brutos a serem contabilizados.
    ordem_categorias : list, tuple ou pd.Index, opcional
        Sequência definindo a ordem desejada para as categorias no índice.
        Se None, mantém a ordenação decrescente padrão por contagem.

    Retorno:
    --------
    pd.DataFrame
        Tabela com as colunas:
        - 'Frequência (ni)': Contagem absoluta de ocorrências.
        - 'Proporção (fi)': Frequência relativa (entre 0 e 1), arredondada para 2 casas decimais.
        - 'Porcentagem (100 * fi)': Frequência percentual (entre 0% e 100%).
        Linha 'Total' com a soma de cada coluna.
    """
    # Contagem de ocorrências absolutas
    freq_absoluta = dados.value_counts()

    # Cálculo da proporção e porcentagem reaproveitando a contagem
    freq_relativa = (freq_absoluta / freq_absoluta.sum()).round(4)
    freq_percentual = (freq_relativa * 100).round(2)

    # Construção do DataFrame com nomes de colunas padronizados
    tabela = pd.DataFrame({
        'Frequência (ni)': freq_absoluta,
        'Proporção (fi)': freq_relativa,
        'Porcentagem (100 * fi)': freq_percentual
    })

    # Aplicação de ordenação personalizada, se fornecida
    if ordem_categorias is not None:
        tabela = tabela.reindex(ordem_categorias)
    else:
        tabela = tabela.sort_index()

    # Linha de totalização calculada diretamente sobre as colunas da tabela
    tabela.loc['Total'] = [
        tabela['Frequência (ni)'].sum(),
        tabela['Proporção (fi)'].sum().round(),
        tabela['Porcentagem (100 * fi)'].sum().round()
    ]

    return tabela

# ==============================================================================
# 2
# ==============================================================================
