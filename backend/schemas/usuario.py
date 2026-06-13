from pydantic import (
    EmailStr, 
    Field, 
    BaseModel, 
    Base64Bytes, 
    FileUrl
)
from typing import Optional
from datetime import datetime


class UsuarioCreate(BaseModel):
    nome: str = Field(min_length=2, max_length=50)
    email: EmailStr = Field(max_length=150)
    senha: str = Field(min_length=8)
    foto_perfil: Optional[Base64Bytes | FileUrl] = Field(default=None)

class UsuarioRead(BaseModel):
    id: int
    nome: str
    email: EmailStr
    foto_perfil_url: Optional[FileUrl]
    data_criacao: datetime

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = Field(default=None, min_length=3, max_length=50)
    email: Optional[EmailStr] = Field(default=None)
    senha: Optional[str] = Field(default=None, min_length=8)
    foto_perfil: Optional[Base64Bytes | FileUrl] = Field(default=None)