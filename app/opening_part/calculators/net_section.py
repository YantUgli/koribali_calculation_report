def calc_net_section(diameter_luar: float, tebal_dinding: float, lebar_lubang: float, y_lubang: float, gross: dict) -> dict:
    luas_lubang = lebar_lubang * tebal_dinding
    luas_penampang_bersih = gross["luas_penampang_utuh"] - luas_lubang

    # Parallel axis theorem
    momen_inersia_lubang = ((lebar_lubang * lebar_lubang**3) / 12) + (luas_lubang * (y_lubang**2))
    momen_inersia_bersih = gross["momen_inersia_utuh"] - momen_inersia_lubang
    
    modulus_penampang_bersih = momen_inersia_bersih / (diameter_luar / 2)

    return {
        "luas_lubang": luas_lubang,                             # A_lubang 
        "luas_penampang_bersih": luas_penampang_bersih,         # A_net
        "momen_inersia_lubang": momen_inersia_lubang,           # I_lubang
        "momen_inersia_bersih": momen_inersia_bersih,           # I_net
        "modulus_penampang_bersih": modulus_penampang_bersih,   # Z_net
        "jarak_centroid_lubang_digunakan": y_lubang
    }