import pynvml

#comandos: nombre, uuid, version_driver, carga, carga_memoria ,memoria_libre, memoria_usada, memoria_total, temperatura, consumo_energia, consumo_limite, velocidad_ventilador, procesos_cuda, procesos_memoria, frecuencia_reloj, frecuencia_reloj_sm, frecuencia_reloj_memoria, frecuencia_max_reloj, frecuencia_max_reloj_sm, frecuencia_max_reloj_memoria, tx_throughput, rx_throughput, version_bios, estado_energia

def get_gpu_info(info_type,handle):
    if info_type == "nombre":
        gpu_name = pynvml.nvmlDeviceGetName(handle)
        full_name = gpu_name.strip()
        return f"Nombre: {full_name}"

    elif info_type=="uuid":
        return f"UUID: {pynvml.nvmlDeviceGetUUID(handle)}"

    elif info_type=="version_driver":
        return f"Versión del driver: {pynvml.nvmlSystemGetDriverVersion()}"

    elif info_type == "carga":
        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
        return f"Carga de la GPU: {utilization.gpu}%"

    elif info_type=="carga_memoria":
        utilization_memory=pynvml.nvmlDeviceGetUtilizationRates(handle)
        return f"Carga de la memoria: {utilization_memory.memory}%"

    elif info_type == "memoria_libre":
        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        free_memory=memory_info.free
        if free_memory < 2**10:
            return f"Memoria libre: {free_memory}B"
        elif free_memory < 2**20:
            return f"Memoria libre: {free_memory / (2**10):.2f}KB"
        elif free_memory < 2**30:
            return f"Memoria libre: {free_memory / (2**20):.2f}MB"
        else:
            return f"Memoria libre: {free_memory / (2**30):.2f}GB"

    elif info_type == "memoria_usada":
        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        used_memory=memory_info.used
        if used_memory < 2**10:
            return f"Memoria utilizada: {used_memory}B"
        elif used_memory < 2**20:
            return f"Memoria utilizada: {used_memory / (2**10):.2f}KB"
        elif used_memory < 2**30:
            return f"Memoria utilizada: {used_memory / (2**20):.2f}MB"
        else:
            return f"Memoria utilizada: {used_memory / (2**30):.2f}GB"

    elif info_type == "memoria_total":
        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        total_memory=memory_info.total
        if total_memory < 2**10:
            return f"Memoria total: {total_memory}B"
        elif total_memory < 2**20:
            return f"Memoria total: {total_memory / (2**10):.2f}KB"
        elif total_memory < 2**30:
            return f"Memoria total: {total_memory / (2**20):.2f}MB"
        else:
            return f"Memoria total: {total_memory / (2**30):.2f}GB"

    elif info_type == "temperatura":
        temperature = pynvml.nvmlDeviceGetTemperature(
            handle, pynvml.NVML_TEMPERATURE_GPU
        )
        return f"Temperatura: {temperature} °C"

    elif info_type == "consumo_energia":
        power_usage = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0
        return f"Consumo: {power_usage:.2f} W"

    elif info_type=="consumo_limite":
        power_limit=pynvml.nvmlDeviceGetPowerManagementLimit(handle) / 1000.0
        return f"Límite: {power_limit:.2f} W"

    elif info_type == "velocidad_ventilador":
        fan_speed = pynvml.nvmlDeviceGetFanSpeed(handle)
        return f"Velocidad del ventilador: {fan_speed}%"

    elif info_type == "procesos_cuda":
        cuda_processes = pynvml.nvmlDeviceGetComputeRunningProcesses(handle)
        return f"Procesos cuda: {len(cuda_processes)}"

    elif info_type=="procesos_memoria":
        processes=pynvml.nvmlDeviceGetComputeRunningProcesses(handle)
        total_process_memory = 0
        for proc in processes:
            if proc.usedGpuMemory is not None:
                total_process_memory += proc.usedGpuMemory
        if total_process_memory < 2**10:
            return f"Memoria utilizada por procesos: {total_process_memory}B"
        elif total_process_memory < 2**20:
            return f"Memoria utilizada por procesos: {total_process_memory / (2**10):.2f}KB"
        elif total_process_memory < 2**30:
            return f"Memoria utilizada por procesos: {total_process_memory / (2**20):.2f}MB"
        else:
            return f"Memoria utilizada por procesos: {total_process_memory / (2**30):.2f}GB"

    elif info_type == "frecuencia_reloj":
        clock_graphics_current = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_GRAPHICS)
        return f"Frecuencia reloj GPU: {clock_graphics_current} MHz"

    elif info_type=="frecuencia_reloj_sm":
        clock_SM=pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_SM)
        return f"Frecuencia reloj SM: {clock_SM} MHz"

    elif info_type=="frecuencia_reloj_memoria":
        clock_memory=pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_MEM)
        return f"Frecuencia reloj memoria: {clock_memory} MHz"

    elif info_type=="frecuencia_max_reloj":
        clock_max=pynvml.nvmlDeviceGetMaxClockInfo(handle, pynvml.NVML_CLOCK_GRAPHICS)
        return f"Frecuencia máxima reloj GPU: {clock_max} MHz"

    elif info_type=="frecuencia_max_reloj_sm":
        clock_sm_max=pynvml.nvmlDeviceGetMaxClockInfo(handle, pynvml.NVML_CLOCK_SM)
        return f"Frecuencia máxima reloj SM: {clock_sm_max} MHz"

    elif info_type=="frecuencia_max_reloj_memoria":
        clock_memory_max=pynvml.nvmlDeviceGetMaxClockInfo(handle, pynvml.NVML_CLOCK_MEM)
        return f"Frecuencia máxima reloj memoria: {clock_memory_max} MHz"

    elif info_type=="tx_throughput":
        tx=pynvml.nvmlDeviceGetPcieThroughput(handle, pynvml.NVML_PCIE_UTIL_TX_BYTES)
        if tx < 2**20:
            return f"TX Throughput: {tx / (2**10):.2f}KB/s"
        else:
            return f"TX Throughput: {tx / (2**20):.2f}MB/s"

    elif info_type=="rx_throughput":
        rx=pynvml.nvmlDeviceGetPcieThroughput(handle, pynvml.NVML_PCIE_UTIL_RX_BYTES)
        if rx < 2**20:
            return f"RX Throughput: {rx / (2**10):.2f}KB/s"
        else:
            return f"RX Throughput: {rx / (2**20):.2f}MB/s"

    elif info_type=="version_bios":
        bios_version=pynvml.nvmlDeviceGetVbiosVersion(handle)
        return f"Versión de la BIOS: {bios_version}"

    elif info_type=="estado_energia":
        power_state=pynvml.nvmlDeviceGetPowerState(handle)
        # Este mapeo es aproximado y puede necesitar ajustes según el modelo de GPU.
        descriptions = {
            0: "P0 - Máximo rendimiento",
            1: "P1 - Rendimiento muy alto",
            2: "P2 - Rendimiento alto",
            3: "P3 - Rendimiento moderado-alto",
            4: "P4 - Rendimiento moderado",
            5: "P5 - Bajo rendimiento",
            6: "P6 - Modo ahorro de energía",
            7: "P7 - Modo ahorro (intermedio)",
            8: "P8 - Estado de inactividad / muy bajo rendimiento",
            9: "P9 - (No documentado)",
            10: "P10 - (No documentado)",
            11: "P11 - (No documentado)",
            12: "P12 - (No documentado)",
            13: "P13 - (No documentado)",
            14: "P14 - (No documentado)",
            15: "P15 - Mínimo rendimiento / máximo ahorro",
        }
        return f"Estado de energía: {descriptions.get(power_state, 'Desconocido')}"

    else:
        return "Tipo de información no válido"



if __name__ == "__main__":
    try:
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        while True:
            user_input = input().strip().lower()
            if user_input == "exit":
                break
            result = get_gpu_info(user_input,handle)
            print(result)
    except pynvml.NVMLError as e:
        print(f"Error obteniendo la info: {str(e)}")
    finally:
        pynvml.nvmlShutdown()
