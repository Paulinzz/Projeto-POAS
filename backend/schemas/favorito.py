from pydantic import ( 
    Field, 
    BaseModel
)
from datetime import datetime


class FavoritoCreate(BaseModel):
    conteudo_id: int = Field(ge=1)
    usuario_id: int = Field(ge=1)

class FavoritoRead(BaseModel):
    id: int
    conteudo_id: int
    usuario_id: int
    data_adicao: datetime

# class FavoritoUpdate(BaseModel):
    # conteudo_id: Optional[int] = Field(ge=1)
    # usuario_id: Optional[int] = Field(ge=1)