from cx_Freeze import setup, Executable

# Define la configuración del ejecutable
setup(
    name="nvidiaScript",
    version="0.1",
    description="Script NVIDIA",
    executables=[Executable("script.py")],
)
