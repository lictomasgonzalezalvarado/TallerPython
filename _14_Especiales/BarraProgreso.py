from tqdm import tqdm
import time

if __name__ == '__main__':
    # barra=tqdm(total=300,desc="Progreso", ncols=80,ascii=True, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", unit='incremento')
    # # Simular un proceso con barra de progreso
    # for i in range(300):
    #     time.sleep(0.05)  # Simula un trabajo que toma tiempo
    #     barra.update(50)

    progress_bar = tqdm(total=300, desc="Progreso", ncols=80,ascii=True, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", unit='incremento')

    # Actualizar manualmente la barra
    avance=20
    for i in range(int(progress_bar.total/avance)):
        time.sleep(0.2)  # Simula un trabajo que lleva tiempo
        progress_bar.update(avance)  # Avanza la barra 10 pasos
    progress_bar.close()  # Cierra la barra de progreso al finalizar
