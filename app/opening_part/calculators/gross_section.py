from app.constants import PI

def calc_gross_section(diameter_luar: float, tebal_dinding: float) -> dict:
    """
    Menghitung properti penampang utuh tiang pipa baja.
    Referensi: SNI 1729-2020 Pasal 6.2

    Args:
        diameter (float): Diameter luar tiang (mm)
        tinggi_tiang (float): Tebal dinding tiang (mm)
    Returns:
        dict: diameter_dalam, luas_penampang_utuh (mm²), momen_inersia_utuh (mm⁴)
    """
    diameter_dalam = diameter_luar - (2 * tebal_dinding)
    
    luas_penampang_utuh = (PI / 4) * (diameter_luar**2 - diameter_dalam**2)
    momen_inersia_utuh = (PI / 64) * (diameter_luar**4 - diameter_dalam**4)

    return {
        "diameter_dalam": diameter_dalam,
        "luas_penampang_utuh": luas_penampang_utuh, #A
        "momen_inersia_utuh": momen_inersia_utuh, #I
    }

def calc_z_gross(diameter_luar: float, momen_inersia_utuh: float):
    modulus_penampang_utuh = momen_inersia_utuh / (diameter_luar / 2)

    return modulus_penampang_utuh