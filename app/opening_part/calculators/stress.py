def calc_stress(momen_lentur: float, gaya_aksial: float, net: dict) -> dict:
    # Konversi satuan:
    # momen_lentur (kN.m) -> N.mm  (dikalikan 1.000.000)
    # gaya_aksial (kN) -> N (dikalikan 1.000)
    
    M_Nmm = momen_lentur * 1e6
    N_N = gaya_aksial * 1e3

    sigma_lentur = M_Nmm / net["modulus_penampang_bersih"]
    sigma_aksial = N_N / net["luas_penampang_bersih"]
    
    sigma_total = sigma_lentur + sigma_aksial

    return {
        "sigma_lentur": sigma_lentur,
        "sigma_aksial": sigma_aksial,
        "sigma_total": sigma_total
    }