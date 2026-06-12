from sqlalchemy import Select
from pwdlib import PasswordHash


from database import SessionDep
from services.usuario_service import UsuarioService
from schemas.usuario import UsuarioCreate
from models import Usuario

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(password, hashed_password):
    return password_hash.verify(password, hashed_password)


class UsuarioServiceImpl(UsuarioService):
    def __init__(self, session: SessionDep):
        self.session = session

    def create_usuario(self, usuario_data: UsuarioCreate):
        senha_hash = get_password_hash(usuario.senha)
        usuario = Usuario(
            nome=usuario_data.nome,
            email=usuario_data.email,
            senha_hash=senha_hash,
            foto_perfil_url="", # colocar depois de alterar o schema UsuarioCreate
        )
        
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)

        return usuario

    def list_usuario(self):
        usuarios = self.session.scalars(
            Select(Usuario)
        ).all()

        return usuarios
    
    def get_usuario(self, id: int):
        pass