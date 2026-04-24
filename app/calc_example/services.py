from app.constants import TEGANGAN_LELEH_BJ37, FAKTOR_KEAMANAN, MODULUS_ELASTISITAS_BAJA

def hitung_tegangan_baja(gaya_n: float, luas_mm2: float) -> dict:
    """
    Menghitung tegangan aktual, regangan, dan status keamanan
    berdasarkan rumus P / A.
    """
    # Menghitung tegangan (MPa = N/mm^2)
    tegangan_aktual = gaya_n / luas_mm2
    
    # Menghitung batas aman
    tegangan_izin = TEGANGAN_LELEH_BJ37 / FAKTOR_KEAMANAN
    
    # Cek apakah struktur aman
    is_aman = tegangan_aktual <= tegangan_izin
    
    # Menghitung regangan
    regangan = tegangan_aktual / MODULUS_ELASTISITAS_BAJA

    return {
        "material": "Baja BJ-37",
        "tegangan_aktual_mpa": round(tegangan_aktual, 2),
        "tegangan_izin_mpa": round(tegangan_izin, 2),
        "regangan": round(regangan, 6),
        "faktor_keamanan_digunakan": FAKTOR_KEAMANAN,
        "status": "Aman" if is_aman else "Tidak Aman (Melebihi Tegangan Izin)"
    }
