from .schemas import OpeningPartInput
from app.opening_part.calculators import (
    calc_net_section,
    calc_stress,
    calc_unity_check,
)
from app.opening_part.calculators import gross_section

def evaluate_pole_opening(data: OpeningPartInput) -> dict:
    """
    Orchestrator untuk mengeksekusi 4 tahapan kalkulasi Opening Part.
    1. Gross Section
    2. Net Section
    3. Stress
    4. Unity Check
    """
    # Tahap 1: Hitung Gross Section(Multiple Function)
    gross_props = gross_section.calc_gross_section(diameter_luar=data.diameter_luar, tebal_dinding=data.tebal_dinding)
    
    # hitung modulus_penampang_utuh terpisah
    modulus_penampang_utuh = gross_section.calc_z_gross(diameter_luar=data.diameter_luar, momen_inersia_utuh=gross_props['momen_inersia_utuh'])

    # penambahan modulus_penampang_utuh kedalam props
    gross_props['modulus_penampang_utuh'] = modulus_penampang_utuh

    # Menentukan jarak_centroid_lubang (worst-case di serat terluar jika tidak di-supply user)
    y_lubang_aktual = data.jarak_centroid_lubang if data.jarak_centroid_lubang else (data.diameter_luar / 2) - (data.tebal_dinding / 2)

    # Tahap 2: Hitung Net Section
    net_props = calc_net_section(
        diameter_luar=data.diameter_luar, 
        tebal_dinding=data.tebal_dinding, 
        lebar_lubang=data.lebar_lubang, 
        y_lubang=y_lubang_aktual, 
        gross=gross_props
    )

    # Tahap 3: Hitung Tegangan Aktual
    stress_props = calc_stress(
        momen_lentur=data.momen_lentur, 
        gaya_aksial=data.gaya_aksial, 
        net=net_props
    )

    # Tahap 4: Unity Check (Keamanan)
    uc_props = calc_unity_check(
        sigma_total=stress_props["sigma_total"], 
        tegangan_leleh=data.tegangan_leleh, 
        faktor_keamanan=data.faktor_keamanan
    )

    # Return Payload untuk dikirim ke routes/controller
    # belum memakai utils/response.py
    return {
        # "status": "success",
        "conclusion": "OK" if uc_props["is_safe"] else "NG",
        # "test" : modulus_penampang_utuh,
        "details": {
            "tahap_1_gross_section": gross_props,
            "tahap_2_net_section": net_props,
            "tahap_3_stress": stress_props,
            "tahap_4_unity_check": uc_props
        }
    }