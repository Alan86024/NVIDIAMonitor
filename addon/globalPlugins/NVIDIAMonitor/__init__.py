# NVIDIA Monitor add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file LICENSE for more details.
# Copyright (C) 2024 José Perez <perezhuancajose@gmail.com> and ayoub <ayoubelbak13@gmail.com>

import globalPluginHandler
from scriptHandler import script,getLastScriptRepeatCount
import ui
import os
import subprocess
import globalVars
import api
import winVersion
import addonHandler
from logHandler import log


#For translators
try:
    addonHandler.initTranslation()
except addonHandler.AddonError:
    log.warning("Unable to initialise translations. This may be because the addon is running from NVDA scratchpad.")


def disableInSecureMode(decoratedCls):
    if globalVars.appArgs.secure:
        return globalPluginHandler.GlobalPlugin
    return decoratedCls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super(GlobalPlugin, self).__init__()
        self.ruta = os.path.join(os.path.dirname(__file__), "scriptNvidia", "script.exe")


    #For translators
    script_category=_("NVIDIAMonitor")
    script_descripcion=_("Si se pulsa dos veces, copia esta información al portapapeles.")

    def ejecutar_comando(self,comando):
        try:
            resultado=subprocess.run(
                [self.ruta, comando],check=True ,capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW
            )
            return resultado.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode} {e.cmd}"


    #For translators
    @script(description=_(f"Anuncia el nombre de la GPU. {script_descripcion}"), gesture="kb:NVDA+alt+g",category=script_category)
    def script_nombre_grafica(self, gesture):
        if winVersion.getWinVer().processorArchitecture=="AMD64":
            if getLastScriptRepeatCount() ==0:
                resultado=self.ejecutar_comando("nombre")
                ui.message(resultado)
            else:
                resultado=self.ejecutar_comando("nombre")
                api.copyToClip(resultado,notify=True)
        else:
            ui.message(_("Error: la arquitectura de tu procesador no es compatible"))


    #For translators
    @script(description=_(f"Anuncia la carga de la GPU. {script_descripcion}"), gesture="kb:NVDA+alt+1",category=script_category)
    def script_carga(self,gesture):
        if winVersion.getWinVer().processorArchitecture=="AMD64":
            if getLastScriptRepeatCount() ==0:
                resultado=self.ejecutar_comando("carga")
                ui.message(resultado)
            else:
                resultado=self.ejecutar_comando("carga")
                api.copyToClip(resultado,notify=True)
        else:
            ui.message(_("Error: la arquitectura de tu procesador no es compatible"))



    #For translators
    @script(description=_(f"Anuncia la memoria libre. {script_descripcion}"),gesture="kb:NVDA+alt+2",category=script_category)
    def script_memoria_libre(self,gesture):
        if winVersion.getWinVer().processorArchitecture=="AMD64":
            if getLastScriptRepeatCount() ==0:
                resultado=self.ejecutar_comando("memoria_libre")
                ui.message(resultado)
            else:
                resultado=self.ejecutar_comando("memoria_libre")
                api.copyToClip(resultado,notify=True)
        else:
            ui.message(_("Error: la arquitectura de tu procesador no es compatible"))



    #For translators
    @script(description=_(f"Anuncia la memoria utilizada. {script_descripcion}"),gesture="kb:NVDA+alt+3",category=script_category)
    def script_memoria_usada(self,gesture):
        if winVersion.getWinVer().processorArchitecture=="AMD64":
            if getLastScriptRepeatCount() ==0:
                resultado=self.ejecutar_comando("memoria_usada")
                ui.message(resultado)
            else:
                resultado=self.ejecutar_comando("memoria_usada")
                api.copyToClip(resultado,notify=True)
        else:
            ui.message(_("Error: la arquitectura de tu procesador no es compatible"))



    #For translators
    @script(description=_(f"Anuncia la memoria total. {script_descripcion}"),gesture="kb:NVDA+alt+4",category=script_category)
    def script_memoria_total(self,gesture):
        if winVersion.getWinVer().processorArchitecture=="AMD64":
            if getLastScriptRepeatCount() ==0:
                resultado=self.ejecutar_comando("memoria_total")
                ui.message(resultado)
            else:
                resultado=self.ejecutar_comando("memoria_total")
                api.copyToClip(resultado,notify=True)
        else:
            ui.message(_("Error: la arquitectura de tu procesador no es compatible"))



    #For translators
    @script(description=_(f"Anuncia la temperatura. {script_descripcion}"),gesture="kb:NVDA+alt+5", category=script_category)
    def script_temperatura(self,gesture):
        if winVersion.getWinVer().processorArchitecture=="AMD64":
            if getLastScriptRepeatCount() ==0:
                resultado=self.ejecutar_comando("temperatura")
                ui.message(resultado)
            else:
                resultado=self.ejecutar_comando("temperatura")
                api.copyToClip(resultado,notify=True)
        else:
            ui.message(_("Error: la arquitectura de tu procesador no es compatible"))



    #For translators
    @script(description=_(f"Anuncia el consumo de energía. {script_descripcion}"),gesture="kb:NVDA+alt+6", category=script_category)
    def script_consumo(self,gesture):
        if winVersion.getWinVer().processorArchitecture=="AMD64":
            if getLastScriptRepeatCount() ==0:
                resultado=self.ejecutar_comando("consumo_energia")
                ui.message(resultado)
            else:
                resultado=self.ejecutar_comando("consumo_energia")
                api.copyToClip(resultado,notify=True)
        else:
            ui.message(_("Error: la arquitectura de tu procesador no es compatible"))



    #For translators
    @script(description=_(f"Anuncia la velocidad del ventilador. {script_descripcion}"),gesture="kb:NVDA+alt+7", category=script_category)
    def script_ventilador(self,gesture):
        if winVersion.getWinVer().processorArchitecture=="AMD64":
            if getLastScriptRepeatCount() ==0:
                resultado=self.ejecutar_comando("velocidad_ventilador")
                ui.message(resultado)
            else:
                resultado=self.ejecutar_comando("velocidad_ventilador")
                api.copyToClip(resultado,notify=True)
        else:
            ui.message(_("Error: la arquitectura de tu procesador no es compatible"))



    #For translators
    @script(description=_(f"Anuncia la cantidad de procesos cuda. {script_descripcion}"), gesture="kb:NVDA+alt+8", category=script_category)
    def script_cudas(self,gesture):
        if winVersion.getWinVer().processorArchitecture=="AMD64":
            if getLastScriptRepeatCount() ==0:
                resultado=self.ejecutar_comando("procesos_cuda")
                ui.message(resultado)
            else:
                resultado=self.ejecutar_comando("procesos_cuda")
                api.copyToClip(resultado,notify=True)
        else:
            ui.message(_("Error: la arquitectura de tu procesador no es compatible"))



    #For translators
    @script(description=_(f"Anuncia la frecuencia del reloj. {script_descripcion}"), gesture="kb:NVDA+alt+9",category=script_category)
    def script_frecuencia(self,gesture):
        if winVersion.getWinVer().processorArchitecture=="AMD64":
            if getLastScriptRepeatCount() ==0:
                resultado=self.ejecutar_comando("frecuencia_reloj")
                ui.message(resultado)
            else:
                resultado=self.ejecutar_comando("frecuencia_reloj")
                api.copyToClip(resultado,notify=True)
        else:
            ui.message(_("Error: la arquitectura de tu procesador no es compatible"))
