from abc import ABC, abstractmethod

from models import Usuario
from schemas.usuario import UsuarioCreate


class UsuarioService(ABC):
    @abstractmethod
    def create_usuario(self, usuario: UsuarioCreate) -> Usuario:
        pass

    @abstractmethod
    def list_usuario(self) -> list[Usuario]:
        pass

    @abstractmethod
    def get_usuario(self, id: int) -> Usuario:
        pass