def calc_unity_check(sigma_total: float, tegangan_leleh: float, faktor_keamanan: float) -> dict:
    sigma_ijin = tegangan_leleh / faktor_keamanan
    uc_ratio = sigma_total / sigma_ijin
    
    is_safe = uc_ratio <= 1.0

    return {
        "sigma_ijin": sigma_ijin,
        "UC": uc_ratio,
        "is_safe": is_safe
    }