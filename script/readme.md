# Script NVIDIA

Este script permite consultar varios parámetros de las tarjetas gráficas NVIDIA. Se utiliza para llamarlo mediante subprocess desde el complemento, ya que la DLL que se necesita (nvml.dll) es de 64 bits, mientras que NVDA es de 32 bits.

## Requisitos

- Python 3.11 o superior
- pynvml
- cx_Freeze

## Cómo compilar

Se recomienda utilizar un entorno virtual:
- Instalar las dependencias: `pip install -r requirements.txt`
- Compilar con: `python setup.py build`
- Luego de compilar copiar el contenido de la carpeta build a addon/globalPlugins/NVIDIAMonitor. Se recomienda renombrar la carpeta que contiene el ejecutable a script

## Cómo utilizar

Al ejecutar el script, se espera que se ingrese un comando como nombre, uuid, version_driver etc. El comando exit cierra el script.

## Lista de comandos

Nota: algúnos parámetros de información pueden no ser compatibles o estár soportados dependiendo de la tarjeta gráfica.

- `nombre`: Devuelve el nombre de la GPU
- `uuid`: Devuelve el UUID de la GPU
- `version_driver`: Devuelve la versión del driver
- `version_bios`: Devuelve la versión de la BIOS
- `carga`: Devuelve la carga de la GPU. Ej: 5%
- `carga_memoria`: Devuelve la carga de la memoria
- `memoria_libre`: Memoria libre de la GPU. Ej: 3.84 GB
- `memoria_usada`: Memoria utilizada de la GPU. Ej: 0.00 GB
- `memoria_total`: Memoria total de la GPU. Ej: 4.00 GB
- `temperatura`: Temperatura de la GPU. Ej: 35°C
- `consumo_energia`: Consumo de la GPU. Ej: 17.89 W
- `consumo_limite`: Límite de energía
- `velocidad_ventilador`: Velocidad del ventilador en porcentaje.
- `procesos_cuda`: Devuelve la cantidad de procesos CUDA.
- `procesos_memoria`: Devuelve la memoria utilizada por los procesos
- `frecuencia_reloj`: Devuelve la frecuencia del relojGPU. Ej: 1380 MHz
- `frecuencia_max_reloj`: Devuelve la frecuencia máxima del reloj GPU
- `frecuencia_reloj_sm`: Devuelve la frecuencia del reloj SM
- `frecuencia_max_reloj_sm`: Devuelve la frecuencia máxima del reloj SM
- `frecuencia_reloj_memoria`: Devuelve la frecuencia del reloj memoria
- `frecuencia_max_reloj_memoria`: Devuelve la frecuencia máxima del reloj memoria
- `tx_throughput`: Devuelve el TX Throughput
- `rx_throughput`: Devuelve el RX Throughput
- `estado_energia`: Devuelve el estado de energía
- `exit`: Cierra el script
