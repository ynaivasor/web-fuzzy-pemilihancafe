import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ====================================================
# DEFINISI
# ====================================================

harga = ctrl.Antecedent(np.arange(0, 101, 1), 'Harga')
jarak = ctrl.Antecedent(np.arange(0, 101, 1), 'Jarak')
fasilitas = ctrl.Antecedent(np.arange(0, 101, 1), 'Fasilitas')
rekomendasi = ctrl.Consequent(np.arange(0, 101, 1), 'Rekomendasi')

# Membership Function
harga['murah'] = fuzz.trapmf(harga.universe, [0, 0, 20, 40])
harga['normal'] = fuzz.trimf(harga.universe, [30, 50, 70])
harga['mahal'] = fuzz.trapmf(harga.universe, [60, 80, 100, 100])

jarak['dekat'] = fuzz.trapmf(jarak.universe, [0, 0, 20, 40])
jarak['sedang'] = fuzz.trimf(jarak.universe, [30, 50, 70])
jarak['jauh'] = fuzz.trapmf(jarak.universe, [60, 80, 100, 100])

fasilitas['tidak lengkap'] = fuzz.trapmf(fasilitas.universe, [0, 0, 20, 40])
fasilitas['lengkap'] = fuzz.trimf(fasilitas.universe, [30, 50, 70])
fasilitas['sangat lengkap'] = fuzz.trapmf(fasilitas.universe, [60, 80, 100, 100])

rekomendasi['TD'] = fuzz.trapmf(rekomendasi.universe, [0, 0, 20, 40])
rekomendasi['C'] = fuzz.trimf(rekomendasi.universe, [30, 50, 70])
rekomendasi['D'] = fuzz.trimf(rekomendasi.universe, [60, 75, 90])
rekomendasi['SD'] = fuzz.trapmf(rekomendasi.universe, [80, 90, 100, 100])

# Rules
rules = []
# (rules kamu tetap, tidak perlu diubah)

rekom_ctrl = ctrl.ControlSystem(rules)
rekom_sim = ctrl.ControlSystemSimulation(rekom_ctrl)

def hitung_rekomendasi(harga_input, jarak_input, fasilitas_input):
    rekom_sim.input['Harga'] = harga_input
    rekom_sim.input['Jarak'] = jarak_input
    rekom_sim.input['Fasilitas'] = fasilitas_input
    rekom_sim.compute()
    return rekom_sim.output['Rekomendasi']
