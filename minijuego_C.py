from PySide6.QtCore import QSize , QTimer ,QThread , Signal

class ActualizacionPuntosThread(QThread):
    actualizarPuntos = Signal()
    def run(self):
        while True:
            self.actualizarPuntos.emit()
            self.msleep(1000)


class minijuegoControlador:

    def __init__(self , miniJuego_V):

        #INSTANCIA DE MINIJUEGO-VISTA
        self.mini_V = miniJuego_V

        #TAMAÑOS DEL GIF
        self.primeraFase_W = 190
        self.primeraFase_H = 225

        self.segundaFase_W = 290
        self.segundaFase_H = 325

        self.terceraFase_W = 390
        self.terceraFase_H = 425

        #VARIABLES
        self.puntuacionTotal = 0
        self.puntuacionPorSegundo = 0
        self.nivel = 0
        self.cantCastros = 0
        self.cantMbappes = 0
        self.cantHallands = 0
        self.cantCristianos = 0
        self.cantMessis = 0

        #TIMER PARA LA ACTUALIZACION DEL TAMAÑO DEL GIF
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.restaurarTamano)



        #CREAMOS EL HILO Y CONECTAMOS AL METODO QUE ACTUALIZA LOS PUNTOS
        self.actualizacionThread = ActualizacionPuntosThread()
        self.actualizacionThread.actualizarPuntos.connect(self.aplicarPuntos)
        self.actualizacionThread.start()




    #METODO QUE VA ACTUALIZANDO LOS PUNTOS
    def aplicarPuntos(self):
        puntosS = 0

        puntosS += (self.cantCastros * 3) + (self.cantMbappes * 10) + (self.cantHallands * 20) + (self.cantCristianos * 30) + (self.cantMessis * 50)

        self.puntuacionTotal += puntosS
        self.puntuacionPorSegundo = puntosS

        self.mini_V.labelPuntuacion.setText(f"PUNTUACION : {self.puntuacionTotal}")
        self.mini_V.labelPuntosSeg.setText(f"PUNTOS/s : {self.puntuacionPorSegundo}")

        if self.puntuacionTotal > 3000000:
            self.nuevoNivel()
        elif self.puntuacionTotal > 2000000:
            self.mini_V.movie.setScaledSize(QSize(self.terceraFase_W, self.terceraFase_H))
        elif self.puntuacionTotal > 1000000:
            self.mini_V.movie.setScaledSize(QSize(self.segundaFase_W, self.segundaFase_H))
        else :
            self.mini_V.movie.setScaledSize(QSize(self.primeraFase_W, self.primeraFase_H))


    #METODOS PARA CLICKAR EL BALON Y SU AUMENTO DE TAMAÑO CON EL CLICK
    def clickarBalon(self):
        self.puntuacionTotal += 1
        self.mini_V.labelPuntuacion.setText(f"PUNTUACION : {self.puntuacionTotal}")
        if self.puntuacionTotal > 3000000:
            self.nuevoNivel()
        elif self.puntuacionTotal > 2000000:
            self.actualizarTamanio(self.terceraFase_W + 50, self.terceraFase_H + 50)
        elif self.puntuacionTotal > 1000000:
            self.actualizarTamanio(self.segundaFase_W + 50, self.segundaFase_W + 50)
        else :
            self.actualizarTamanio(self.primeraFase_W + 50, self.primeraFase_H + 50)

    def actualizarTamanio(self, width, height):
        self.mini_V.movie.setScaledSize(QSize(width, height))
        self.timer.start(100)         

    def restaurarTamano(self):
        if self.puntuacionTotal <= 1000000:
            self.mini_V.movie.setScaledSize(QSize(self.primeraFase_W, self.primeraFase_H))
        elif self.puntuacionTotal <= 2000000:
            self.mini_V.movie.setScaledSize(QSize(self.segundaFase_W, self.segundaFase_H))
        else:
            self.mini_V.movie.setScaledSize(QSize(self.terceraFase_W, self.terceraFase_H))        


    #METODO PARA UN REINICIO GENERAL
    def reinicioGeneral(self):
        self.puntuacionTotal = 0
        self.mini_V.labelPuntuacion.setText(f"PUNTUACION : {self.puntuacionTotal}")
        self.puntuacionPorSegundo = 0
        self.mini_V.labelPuntosSeg.setText(f"PUNTOS/s : {self.puntuacionPorSegundo}")
        self.nivel = 0
        self.mini_V.labelLevel.setText(f"NIVEL : {self.nivel}")
        self.cantCastros = 0
        self.mini_V.labelContCastro.setText("0")
        self.cantMbappes = 0
        self.mini_V.labelContMbappe.setText("0")
        self.cantHallands = 0
        self.mini_V.labelContHalland.setText("0")
        self.cantCristianos = 0
        self.mini_V.labelContCristiano.setText("0")
        self.cantMessis = 0
        self.mini_V.labelContMessi.setText("0")
        self.mini_V.movie.setScaledSize(QSize(self.primeraFase_W, self.primeraFase_H))


    #METODO PARA AGREGAR NUEVO NIVEL
    def nuevoNivel(self):
        self.puntuacionTotal = 0
        self.puntuacionPorSegundo = 0
        self.nivel += 1
        self.mini_V.labelLevel.setText(f"NIVEL : {self.nivel}")
        self.cantCastros = 0
        self.mini_V.labelContCastro.setText("0")
        self.cantMbappes = 0
        self.mini_V.labelContMbappe.setText("0")
        self.cantHallands = 0
        self.mini_V.labelContHalland.setText("0")
        self.cantCristianos = 0
        self.mini_V.labelContCristiano.setText("0")
        self.cantMessis = 0
        self.mini_V.labelContMessi.setText("0")
        self.mini_V.movie.setScaledSize(QSize(self.primeraFase_W, self.primeraFase_H))


    #METODO PARA SUMAR UN CASTRO
    def sumarCastro(self):
        if self.puntuacionTotal >= 50:
            self.cantCastros += 1
            self.mini_V.labelContCastro.setText(str(self.cantCastros))
            self.puntuacionTotal -= 50
            self.mini_V.labelPuntuacion.setText(f"PUNTUACION : {self.puntuacionTotal}")

    #METODO PARA SUMAR UN MBAPPE
    def sumarMbappe(self):
        if self.puntuacionTotal >= 500:
            self.cantMbappes += 1
            self.mini_V.labelContMbappe.setText(str(self.cantMbappes))
            self.puntuacionTotal -= 500
            self.mini_V.labelPuntuacion.setText(f"PUNTUACION : {self.puntuacionTotal}")

    #METODO PARA SUMAR UN HALLAND
    def sumarHalland(self):
        if self.puntuacionTotal >= 1000:
            self.cantHallands += 1
            self.mini_V.labelContHalland.setText(str(self.cantHallands))
            self.puntuacionTotal -= 1000
            self.mini_V.labelPuntuacion.setText(f"PUNTUACION : {self.puntuacionTotal}")

    #METODO PARA SUMAR UN CRISTIANO
    def sumarCristiano(self):
        if self.puntuacionTotal >= 10000:
            self.cantCristianos += 1
            self.mini_V.labelContCristiano.setText(str(self.cantCristianos))
            self.puntuacionTotal -= 10000
            self.mini_V.labelPuntuacion.setText(f"PUNTUACION : {self.puntuacionTotal}")

    #METODO PARA SUMAR UN MESSI
    def sumarMessi(self):
        if self.puntuacionTotal >= 100000:
            self.cantMessis += 1
            self.mini_V.labelContMessi.setText(str(self.cantMessis))
            self.puntuacionTotal -= 100000
            self.mini_V.labelPuntuacion.setText(f"PUNTUACION : {self.puntuacionTotal}")                