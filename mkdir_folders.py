import os

folders = [
    'maquinas2/presentaciones/slides',
    'maquinas2/presentaciones/images'
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f'Created {folder}')