# Script NVIDIA

Este script permite consultar varios parámetros de las tarjetas gráficas NVIDIA. Se utiliza para llamarlo mediante subprocess desde el complemento, ya que la DLL que se necesita (nvml.dll) es de 64 bits, mientras que NVDA es de 32 bits.

## Requisitos

- Python 3.11 o superior
- pynvml
- pyinstaller

## Cómo compilar

Se recomienda utilizar un entorno virtual:
- Instalar las dependencias: `pip install -r requirements.txt`
- Compilar con: `pyinstaller --onefile script.py`

## Cómo utilizar

Llama a `script.py` o `script.exe` y pasa un argumento como: `script.py nombre`

## Lista de argumentos

Nota: Algunos argumentos, como `velocidad_ventilador`, no están disponibles dependiendo del modelo de la GPU.

- `nombre`: Devuelve el nombre de la GPU.
- `carga`: Devuelve la carga de la GPU. Ej: 5%
- `memoria_libre`: Memoria libre de la GPU. Ej: 3.84 GB
- `memoria_usada`: Memoria usada de la GPU. Ej: 0.00 GB
- `memoria_total`: Memoria total de la GPU. Ej: 4.00 GB
- `temperatura`: Temperatura de la GPU. Ej: 35°C
- `consumo_energia`: Consumo de la GPU. Ej: 17.89 W
- `velocidad_ventilador`: Velocidad del ventilador en porcentaje.
- `procesos_cuda`: Devuelve la cantidad de procesos CUDA.
- `frecuencia_reloj`: Devuelve la frecuencia del reloj. Ej: 1380 MHz
