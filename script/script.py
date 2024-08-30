import pynvml
import argparse

# nombre, carga, memoria_libre, memoria_usada, memoria_total, temperatura, consumo_energia, velocidad_ventilador, procesos_cuda, frecuencia_reloj


def get_gpu_info(info_type):
    pynvml.nvmlInit()

    try:
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)

        if info_type == "nombre":
            gpu_name = pynvml.nvmlDeviceGetName(handle)
            full_name=gpu_name.strip()
            return f"GPU: {full_name}"

        elif info_type == "carga":
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
            return f"Carga de la GPU: {utilization.gpu}%"

        elif info_type == "memoria_libre":
            memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            return f"Memoria libre: {memory_info.free / (2**30):.2f} GB"

        elif info_type == "memoria_usada":
            memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            return f"Memoria utilizada: {memory_info.used // (2**30):.2f} GB"

        elif info_type == "memoria_total":
            memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            return f"Memoria total: {memory_info.total / (2**30):.2f} GB"

        elif info_type == "temperatura":
            temperature = pynvml.nvmlDeviceGetTemperature(
                handle, pynvml.NVML_TEMPERATURE_GPU
            )
            return f"Temperatura: {temperature} °C"

        elif info_type == "consumo_energia":
            power_usage = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0
            return f"Consumo: {power_usage:.2f} W"

        elif info_type == "velocidad_ventilador":
            fan_speed = pynvml.nvmlDeviceGetFanSpeed(handle)
            return f"Velocidad de la ventilación del GPU: {fan_speed}"

        elif info_type == "procesos_cuda":
            cuda_processes = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)
            return f"Procesos cuda: {len(cuda_processes)}"

        elif info_type == "frecuencia_reloj":
            clock_graphics_current = pynvml.nvmlDeviceGetClockInfo(
                handle, pynvml.NVML_CLOCK_GRAPHICS
            )
            return f"Frecuencia reloj: {clock_graphics_current} MHz"

        else:
            return "Tipo de información no válido"
    except pynvml.NVMLError as e:
        return f"Error obteniendo la info: {str(e)}"

    finally:
        pynvml.nvmlShutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obtener información de la GPU.")
    parser.add_argument("info_type", type=str, help="tipo de información obtenida).")

    args = parser.parse_args()

    result = get_gpu_info(args.info_type)

    if isinstance(result, float):
        print(f"{result:.2f}")
    elif isinstance(result, int):
        print(result)
    elif isinstance(result, str):
        print(result)
    else:
        print(result)
