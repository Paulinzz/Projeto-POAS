from pydantic import ( 
    Field, 
    BaseModel
)
from datetime import datetime


class AssistidoCreate(BaseModel):
    conteudo_id: int = Field(ge=1)
    usuario_id: int = Field(ge=1)

class AssistidoRead(BaseModel):
    id: int
    conteudo_id: int
    usuario_id: int
    data_adicao: datetime

# class AssistidoUpdate(BaseModel):
    # conteudo_id: Optional[int] = Field(ge=1)
    # usuario_id: Optional[int] = Field(ge=1)