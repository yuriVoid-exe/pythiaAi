from pydantic import BaseModel
from typing import List

# Estrutura o resultado da consulta
class QueryResult(BaseModel):
    title: str = None
    url: str = None
    resume: str = None

# Responsavel por carregar a informação
class ReportState(BaseModel):
    user_input: str = None
    final_response: str = None
    queries: List[str] = []
