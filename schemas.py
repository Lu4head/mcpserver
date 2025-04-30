from pydantic import BaseModel

class CarroBase(BaseModel):
    marca: str
    modelo: str
    ano: int
    
class CreateCarro(CarroBase):
    class Config:
        model_config = {
            "from_attributes": True
        }
        json_schema_extra = {
            "example": {
                "marca": "Fiat",
                "modelo": "Uno",
                "ano": 1990
            }
        }

class CarroResponse(CarroBase):
    id: int

    class Config:
        model_config = {
            "from_attributes": True
        }
        json_schema_extra = {
            "example": {
                "id": 1,
                "marca": "Fiat",
                "modelo": "Uno",
                "ano": 1990
            }
        }
    
