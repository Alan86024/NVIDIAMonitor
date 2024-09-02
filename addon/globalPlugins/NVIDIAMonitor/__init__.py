# NVIDIA Monitor add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file LICENSE for more details.
# Copyright (C) 2024 José Perez <perezhuancajose@gmail.com> and ayoub <ayoubelbak13@gmail.com>

import globalPluginHandler
from scriptHandler import script
import ui
import os
import subprocess
import globalVars

def disableInSecureMode(decoratedCls):
    if globalVars.appArgs.secure:
        return globalPluginHandler.GlobalPlugin
    return decoratedCls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super(GlobalPlugin, self).__init__()
        self.ruta = os.path.join(os.path.dirname(__file__), "scriptNvidia", "script.exe")


    script_category="NVIDIAMonitor"

    @script(description="Anuncia el nombre de la GPU", gesture="kb:NVDA+alt+g",category=script_category)
    def script_nombre_grafica(self, gesture):
        try:
            resultado = subprocess.run(
                [self.ruta, "nombre"],check=True ,capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            ui.message(resultado.stdout)
        except Exception as e:
            ui.message("Ocurrió un error al obtener información sobre la GPU")

    @script(description="Anuncia la carga de la GPU", gesture="kb:NVDA+alt+1",category=script_category)
    def script_carga(self,gesture):
        try:
            resultado = subprocess.run(
                [self.ruta, "carga"], check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            ui.message(resultado.stdout)
        except Exception as e:
            ui.message("Ocurrió un error al obtener información sobre la GPU")

    @script(description="Anuncia la memoria libre",gesture="kb:NVDA+alt+2",category=script_category)
    def script_memoria_libre(self,gesture):
        try:
            resultado = subprocess.run(
                [self.ruta, "memoria_libre"], check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            ui.message(resultado.stdout)
        except Exception as e:
            ui.message("Ocurrió un error al obtener información sobre la GPU")

    @script(description="Anuncia la memoria utilizada",gesture="kb:NVDA+alt+3",category=script_category)
    def script_memoria_usada(self,gesture):
        try:
            resultado = subprocess.run(
                [self.ruta, "memoria_usada"], check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            ui.message(resultado.stdout)
        except Exception as e:
            ui.message("Ocurrió un error al obtener información sobre la GPU")

    @script(description="Anuncia la memoria total",gesture="kb:NVDA+alt+4",category=script_category)
    def script_memoria_total(self,gesture):
        try:
            resultado = subprocess.run(
                [self.ruta, "memoria_total"], check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            ui.message(resultado.stdout)
        except Exception as e:
            ui.message("Ocurrió un error al obtener información sobre la GPU")

    @script("Anuncia la temperatura",gesture="kb:NVDA+alt+5", category=script_category)
    def script_temperatura(self,gesture):
        try:
            resultado = subprocess.run(
                [self.ruta, "temperatura"], check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            ui.message(resultado.stdout)
        except Exception as e:
            ui.message("Ocurrió un error al obtener información sobre la GPU")

    @script(description="Anuncia el consumo de energía",gesture="kb:NVDA+alt+6", category=script_category)
    def script_consumo(self,gesture):
        try:
            resultado = subprocess.run(
                [self.ruta, "consumo_energia"], check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            ui.message(resultado.stdout)
        except Exception as e:
            ui.message("Ocurrió un error al obtener información sobre la GPU")

    @script(description="Anuncia la velocidad del ventilador",gesture="kb:NVDA+alt+7", category=script_category)
    def script_ventilador(self,gesture):
        try:
            resultado = subprocess.run(
                [self.ruta, "velocidad_ventilador"], check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            ui.message(resultado.stdout)
        except Exception as e:
            ui.message("Ocurrió un error al obtener información sobre la GPU")

    @script(description="Anuncia la cantidad de procesos cuda", gesture="kb:NVDA+alt+8", category=script_category)
    def script_cudas(self,gesture):
        try:
            resultado = subprocess.run(
                [self.ruta, "procesos_cuda"], check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            ui.message(resultado.stdout)
        except Exception as e:
            ui.message("Ocurrió un error al obtener información sobre la GPU")

    @script(description="Anuncia la frecuencia del reloj", gesture="kb:NVDA+alt+9",category=script_category)
    def script_frecuencia(self,gesture):
        try:
            resultado = subprocess.run(
                [self.ruta, "frecuencia_reloj"], check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            ui.message(resultado.stdout)
        except Exception as e:
            ui.message("Ocurrió un error al obtener información sobre la GPU")
