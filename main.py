import models
from typing import List
from sqlalchemy.orm import Session
from mcp.server.fastmcp import FastMCP
from schemas import CreateCarro, CarroResponse

# Initialize FastMCP server
mcp = FastMCP("teste-mcp")

models.Base.metadata.create_all(bind=models.engine)

@mcp.tool()
async def get_carros() -> List[CarroResponse]:
    """Obtem uma lista de todos os carros"""
    with Session(models.engine) as db:
        carros = db.query(models.Carro).all()
        if carros is None:
            return None
        return [CarroResponse.model_validate(carro) for carro in carros]

@mcp.tool()
async def get_carro_by_id(id : int) -> CarroResponse:
    """Obtem um carro pelo ID"""
    with Session(models.engine) as db:
        carro = db.query(models.Carro).filter(models.Carro.id == id).first()
        if carro is None:
            return None
        return CarroResponse.model_validate(carro)

@mcp.tool()
async def create_carro(carro : CreateCarro) -> CarroResponse:
    """
    Cria um novo carro
    
    Args:
        marca (str): Marca do carro
        modelo (str): Modelo do carro
        ano (int): Ano do carro

    """
    with Session(models.engine) as db:
        db_carro = models.Carro(**carro.model_dump())
        db.add(db_carro)
        db.commit()
        db.refresh(db_carro)
        return CarroResponse.model_validate(db_carro)

@mcp.tool()
async def update_carro(id : int, carro : CreateCarro) -> CarroResponse:
    """Atualiza um carro pelo ID"""
    with Session(models.engine) as db:
        db_carro = db.query(models.Carro).filter(models.Carro.id == id).first()
        if db_carro is None:
            return None
        db_carro.marca = carro.marca
        db_carro.modelo = carro.modelo
        db_carro.ano = carro.ano
        db.update(db_carro)
        db.commit()
        db.refresh(db_carro)
        return CarroResponse.model_validate(db_carro)

@mcp.tool()    
async def delete_carro(id : int):
    """Deleta um carro pelo ID"""
    with Session(models.engine) as db:
        db_carro = db.query(models.Carro).filter(models.Carro.id == id).first()
        if db_carro is None:
            return None
        db.delete(db_carro)
        db.commit()
        return {"message": "Carro deletado com sucesso"}
    

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
