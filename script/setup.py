from cx_Freeze import setup, Executable

setup(
    name="scriptNvidia",
    version="0.1",
    description="Script para obtener información sobre las gráficas NVIDIA",
    executables=[Executable("script.py")]
)
