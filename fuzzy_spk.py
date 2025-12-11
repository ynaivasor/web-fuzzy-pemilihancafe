import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

harga = ctrl.Antecedent(np.arange(0, 101, 1), 'Harga')
jarak = ctrl.Antecedent(np.arange(0, 101, 1), 'Jarak')
fasilitas = ctrl.Antecedent(np.arange(0, 101, 1), 'Fasilitas')
rekomendasi = ctrl.Consequent(np.arange(0, 101, 1), 'Rekomendasi')

harga['murah'] = fuzz.trapmf(harga.universe, [0, 0, 20, 40])
harga['normal'] = fuzz.trimf(harga.universe, [30, 50, 70])
harga['mahal'] = fuzz.trapmf(harga.universe, [60, 80, 100, 100])

jarak['dekat'] = fuzz.trapmf(jarak.universe, [0, 0, 20, 40])
jarak['sedang'] = fuzz.trimf(jarak.universe, [30, 50, 70])
jarak['jauh'] = fuzz.trapmf(jarak.universe, [60, 80, 100, 100])

fasilitas['tidak lengkap'] = fuzz.trapmf(fasilitas.universe, [0, 0, 20, 40])
fasilitas['lengkap'] = fuzz.trimf(fasilitas.universe, [30, 50, 70])
fasilitas['sangat lengkap'] = fuzz.trapmf(fasilitas.universe, [60, 80, 100, 100])

rekomendasi['TD'] = fuzz.trapmf(rekomendasi.universe, [0, 0, 20, 40])     # Senja
rekomendasi['C']  = fuzz.trimf(rekomendasi.universe, [30, 50, 70])        # Bento
rekomendasi['D']  = fuzz.trimf(rekomendasi.universe, [60, 75, 90])        # MaTo
rekomendasi['SD'] = fuzz.trapmf(rekomendasi.universe, [80, 90, 100, 100]) # Santai Kawan

rules = [

    ctrl.Rule(harga['murah'] & jarak['dekat'] & fasilitas['sangat lengkap'], rekomendasi['SD']),
    ctrl.Rule(harga['murah'] & jarak['dekat'] & fasilitas['lengkap'], rekomendasi['SD']),
    ctrl.Rule(harga['murah'] & jarak['dekat'] & fasilitas['tidak lengkap'], rekomendasi['D']),

    ctrl.Rule(harga['murah'] & jarak['sedang'] & fasilitas['sangat lengkap'], rekomendasi['D']),
    ctrl.Rule(harga['murah'] & jarak['sedang'] & fasilitas['lengkap'], rekomendasi['D']),
    ctrl.Rule(harga['murah'] & jarak['sedang'] & fasilitas['tidak lengkap'], rekomendasi['C']),

    ctrl.Rule(harga['murah'] & jarak['jauh'] & fasilitas['sangat lengkap'], rekomendasi['C']),
    ctrl.Rule(harga['murah'] & jarak['jauh'] & fasilitas['lengkap'], rekomendasi['C']),
    ctrl.Rule(harga['murah'] & jarak['jauh'] & fasilitas['tidak lengkap'], rekomendasi['TD']),

    ctrl.Rule(harga['normal'] & jarak['dekat'] & fasilitas['sangat lengkap'], rekomendasi['D']),
    ctrl.Rule(harga['normal'] & jarak['dekat'] & fasilitas['lengkap'], rekomendasi['D']),
    ctrl.Rule(harga['normal'] & jarak['dekat'] & fasilitas['tidak lengkap'], rekomendasi['C']),

    ctrl.Rule(harga['normal'] & jarak['sedang'] & fasilitas['sangat lengkap'], rekomendasi['C']),
    ctrl.Rule(harga['normal'] & jarak['sedang'] & fasilitas['lengkap'], rekomendasi['C']),
    ctrl.Rule(harga['normal'] & jarak['sedang'] & fasilitas['tidak lengkap'], rekomendasi['TD']),

    ctrl.Rule(harga['normal'] & jarak['jauh'] & fasilitas['sangat lengkap'], rekomendasi['TD']),
    ctrl.Rule(harga['normal'] & jarak['jauh'] & fasilitas['lengkap'], rekomendasi['TD']),
    ctrl.Rule(harga['normal'] & jarak['jauh'] & fasilitas['tidak lengkap'], rekomendasi['TD']),

    ctrl.Rule(harga['mahal'] & jarak['dekat'] & fasilitas['sangat lengkap'], rekomendasi['C']),
    ctrl.Rule(harga['mahal'] & jarak['dekat'] & fasilitas['lengkap'], rekomendasi['C']),
    ctrl.Rule(harga['mahal'] & jarak['dekat'] & fasilitas['tidak lengkap'], rekomendasi['TD']),

    ctrl.Rule(harga['mahal'] & jarak['sedang'] & fasilitas['sangat lengkap'], rekomendasi['TD']),
    ctrl.Rule(harga['mahal'] & jarak['sedang'] & fasilitas['lengkap'], rekomendasi['TD']),
    ctrl.Rule(harga['mahal'] & jarak['sedang'] & fasilitas['tidak lengkap'], rekomendasi['TD']),

    ctrl.Rule(harga['mahal'] & jarak['jauh'] & fasilitas['sangat lengkap'], rekomendasi['TD']),
    ctrl.Rule(harga['mahal'] & jarak['jauh'] & fasilitas['lengkap'], rekomendasi['TD']),
    ctrl.Rule(harga['mahal'] & jarak['jauh'] & fasilitas['tidak lengkap'], rekomendasi['TD']),

]


rekom_ctrl = ctrl.ControlSystem(rules)
rekom_sim = ctrl.ControlSystemSimulation(rekom_ctrl)

def hitung_fuzzy(harga_input, jarak_input, fasilitas_input):
    rekom_sim.input['Harga'] = harga_input
    rekom_sim.input['Jarak'] = jarak_input
    rekom_sim.input['Fasilitas'] = fasilitas_input

    rekom_sim.compute()
    nilai = rekom_sim.output['Rekomendasi']

    if nilai >= 80:
        return "santai"   
    elif nilai >= 60:
        return "mato"     
    elif nilai >= 40:
        return "bento"    
    else:
        return "senja"    
