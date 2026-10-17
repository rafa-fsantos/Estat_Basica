"""
io_utils.py
Rotinas utilitárias para localização da raiz do projeto e I/O de bases de dados.
"""

from pathlib import Path
from typing import Optional, Union
import pgiandas as pd # type: ignore


def get_project_root() -> Path:
    """
    Retorna o caminho absoluto da raiz do repositório.
    Garante que o caminho funcione de qualquer subpasta de notebooks ou scripts.
    """
    # src/io_utils.py -> parent = src -> parent.parent = raiz
    return Path(__file__).resolve().parent.parent


def get_data_path(filename: str, folder: str = "raw") -> Path:
    """
    Monta o caminho absoluto para um arquivo dentro do diretório data/.
    folder: 'raw', 'processed' ou subpasta customizada.
    """
    return get_project_root() / "data" / folder / filename


def load_data(
    filename: str,
    folder: str = "raw",
    **kwargs
) -> pd.DataFrame:
    """
    Carrega dados de data/raw ou data/processed com base na extensão do arquivo.
    Suporta .csv, .xlsx, .xls e .parquet.
    """
    path = get_data_path(filename, folder=folder)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    ext = path.suffix.lower()

    if ext == ".csv":
        return pd.read_csv(path, **kwargs)
    elif ext in [".xlsx", ".xls"]:
        return pd.read_excel(path, **kwargs)
    elif ext == ".parquet":
        return pd.read_parquet(path, **kwargs)
    else:
        raise ValueError(f"Extensão não suportada: '{ext}'. Use .csv, .xlsx ou .parquet.")


def save_data(
    df: pd.DataFrame,
    filename: str,
    folder: str = "processed",
    index: bool = False,
    **kwargs
) -> Path:
    """
    Salva um DataFrame criando diretórios ausentes automaticamente.
    Suporta .csv, .xlsx e .parquet.
    """
    path = get_data_path(filename, folder=folder)
    path.parent.mkdir(parents=True, exist_ok=True)

    ext = path.suffix.lower()

    if ext == ".csv":
        df.to_csv(path, index=index, **kwargs)
    elif ext in [".xlsx", ".xls"]:
        df.to_excel(path, index=index, **kwargs)
    elif ext == ".parquet":
        df.to_parquet(path, index=index, **kwargs)
    else:
        raise ValueError(f"Extensão não suportada: '{ext}'. Use .csv, .xlsx ou .parquet.")

    return path
