from dataclasses import dataclass
from typing import Optional

@dataclass
class OpeningPartInput:
    diameter_luar: float                # mm
    tebal_dinding: float                # mm
    tinggi_lubang: float                # mm
    lebar_lubang: float                 # mm
    posisi_lubang_dari_dasar: float     # mm
    tegangan_leleh: float               # MPa
    modulus_elastisitas: float          # MPa
    faktor_keamanan: float
    momen_lentur: float                 # kN.m
    gaya_aksial: float                  # kN
    jarak_centroid_lubang: Optional[float] = None  # mm (Bisa diisi jika posisi lubang tidak di serat terluar)