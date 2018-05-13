import pandas as pd

r = [['2d1v', {'br_c2v-c2d': [60, 40], 'dist_vM-dM': [0.0024787696183466478, 0.0026694179517862977]}], ['1v2d', {'br_c2v-c2d': [19, 81], 'dist_vM-dM': [0.0026285336693347683, 0.0021850339561409761]}], ['2v1d', {'br_c2v-c2d': [44, 56], 'dist_vM-dM': [0.0026495463931877307, 0.0025134540627839898]}], ['1d2v', {'br_c2v-c2d': [82, 18], 'dist_vM-dM': [0.0021823124237625997, 0.0026353459304046174]}]]

#[['2v1d', {'br_c2v-c2d': [4201, 5799], 'dist_vM-dM': [0.0027514631290620796, 0.0026156384550916952]}]]
# [['2d1v', {'dist_vM-dM': [0.0026201764748794813, 0.0027587279635444034], 'br_c2v-c2d': [5793, 4207]}]]
#[['2v1d-Rand', {'br_c2v-c2d': [6393, 3607], 'dist_vM-dM': [0.0024845981485752348, 0.0027044313088072282]}]]
#[['2d1v-Rand', {'br_c2v-c2d': [3615, 6385], 'dist_vM-dM': [0.0027074417556008428, 0.002496571262124621]}]]


[print(i) for i in r]

# split binary rank results
br = {}
for i in range(0,4):
    br.update({r[i][0]:r[i][1]['br_c2v-c2d']})

df2 = pd.DataFrame(br).T

print(df2.head())
