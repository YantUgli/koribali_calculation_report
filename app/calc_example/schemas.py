from pydantic import BaseModel, Field

class CalcTeganganRequest(BaseModel):
    # Gaya yang bekerja dalam Newton (N)
    gaya_newton: float = Field(..., description="Gaya aksial dalam satuan Newton (N)", gt=0)
    # Luas penampang baja dalam mm^2
    luas_penampang_mm2: float = Field(..., description="Luas penampang baja dalam satuan mm^2", gt=0)