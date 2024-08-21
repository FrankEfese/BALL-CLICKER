from PySide6.QtWidgets import QApplication , QWidget , QVBoxLayout , QHBoxLayout , QLabel , QPushButton , QSpacerItem , QSizePolicy
from PySide6.QtGui import QIcon , QColor, QPainter , QLinearGradient , QPen , QMovie
from PySide6.QtCore import Qt , QSize , Signal
from minijuego_C import minijuegoControlador 

class clickarBalon(QLabel):
    clicked = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)


class minijuegoActivityVista(QWidget):

    def __init__(self):
        super().__init__()        

        #CARACTERISTICAS DE LA VENTANA
        self.setWindowTitle("BALL CLICKER")
        self.setGeometry(100,50 ,1200 , 600)
        self.setMinimumSize(1000,600)
        self.setWindowIcon(QIcon("img/icono_app"))

        estilo = '''

            QLabel{
            height:30px;
            font-size:15px;
            background-color: white;
            margin-bottom: 5px;
            margin-top:5px;
            padding: 10px;
            font-weight:bold;
            font-family: "Bahnschrift SemiBold";
            border: 2px solid black;
            border-radius: 15px; 
        }

        QPushButton{
            text-align: left;
            min-height:50px;
            padding: 10px;
            font-size: 20px;
            border-radius: 15px; 
            border: 3px solid black;
            margin-bottom: 5px;
            margin-top:5px;
            background-color: black;
            color: white;
            font-weight:bold;
            font-family: "Bahnschrift SemiBold";
        }

        QPushButton:hover{
            background-color: grey;
        }

        '''

        self.setStyleSheet(estilo)
        self.paintEvent = self.dibujarFondoDegradado

        #LAYOUTS / WIDGET
        self.layoutVertPrin = QVBoxLayout()

        self.layoutPuntosLevel = QHBoxLayout()

        self.layoutBotones = QVBoxLayout()
        self.widgetBotones = QWidget()
        self.widgetBotones.setStyleSheet("max-width:450px;")
        self.widgetBotones.paintEvent = self.dibujarFondoDegradadoWidgetBotones

        self.layoutCastro = QHBoxLayout()
        self.layoutMbappe = QHBoxLayout()
        self.layoutHalland = QHBoxLayout()
        self.layoutCristiano = QHBoxLayout()
        self.layoutMessi = QHBoxLayout()

        self.widgetImg = QWidget()
        self.widgetImg.paintEvent = self.dibujarCampo
        self.layoutImg = QVBoxLayout()

        self.layoutContenido = QHBoxLayout()

        #COMPONENTES
        self.labelPuntuacion = QLabel("PUNTUACION : ")
        self.labelPuntuacion.setAlignment(Qt.AlignCenter)
        self.labelPuntuacion.setStyleSheet("max-height:25px;")
        self.layoutPuntosLevel.addWidget(self.labelPuntuacion)

        self.labelPuntosSeg = QLabel("PUNTOS/s : 0")
        self.labelPuntosSeg.setAlignment(Qt.AlignCenter)
        self.labelPuntosSeg.setStyleSheet("max-height:25px;")
        self.layoutPuntosLevel.addWidget(self.labelPuntosSeg)

        self.labelLevel = QLabel("NIVEL : 0")
        self.labelLevel.setAlignment(Qt.AlignCenter)
        self.labelLevel.setStyleSheet("max-height:25px;")
        self.layoutPuntosLevel.addWidget(self.labelLevel)

        self.btnReinicio = QPushButton()
        iconoRecarga = QIcon("img/icono_recarga.png")
        self.btnReinicio.setIcon(iconoRecarga)
        self.btnReinicio.setIconSize(QSize(28,28))
        self.btnReinicio.setCursor(Qt.PointingHandCursor)
        self.btnReinicio.setStyleSheet("min-height:25px; max-width:25px; padding: 10px; ")
        self.layoutPuntosLevel.addWidget(self.btnReinicio)

        self.labelImagenBalon = clickarBalon()
        self.labelImagenBalon.setAlignment(Qt.AlignCenter)
        self.labelImagenBalon.setStyleSheet("background-color : rgba(255, 255, 255, 0); border:none;")
        self.layoutImg.addWidget(self.labelImagenBalon)
        self.widgetImg.setLayout(self.layoutImg)
        self.movie = QMovie("img/balon.gif")
        self.movie.setScaledSize(QSize(190, 225))  # Scale the GIF to the desired size
        self.labelImagenBalon.setMovie(self.movie)
        self.movie.start()

        self.opciones = QLabel("--- COMPRAS ---")
        self.opciones.setAlignment(Qt.AlignCenter)
        self.opciones.setStyleSheet("background-color: white; color:black; font-size: 30px;")
        self.layoutBotones.addWidget(self.opciones)


        #BOTON RUBEN CASTRO
        self.btnCastro = QPushButton("R.CASTRO = 3p/s  (50P)")
        iconoCastro = QIcon("img/castro.png")
        self.btnCastro.setIcon(iconoCastro)
        self.btnCastro.setIconSize(QSize(75,75))
        self.btnCastro.setCursor(Qt.PointingHandCursor)

        self.labelContCastro = QLabel("0")
        self.labelContCastro.setStyleSheet("background-color: black; color:white; max-width:40px;")
        self.labelContCastro.setAlignment(Qt.AlignCenter)

        self.layoutCastro.addWidget(self.btnCastro)
        self.layoutCastro.addWidget(self.labelContCastro)
        self.layoutBotones.addLayout(self.layoutCastro)


        #BOTON MBAPPE
        self.btnMbappe = QPushButton("MBAPPE = 10p/s (500P)")
        iconoMbappe = QIcon("img/mbappe.png")
        self.btnMbappe.setIcon(iconoMbappe)
        self.btnMbappe.setIconSize(QSize(75,75))
        self.btnMbappe.setCursor(Qt.PointingHandCursor)

        self.labelContMbappe = QLabel("0")
        self.labelContMbappe.setStyleSheet("background-color: black; color:white; max-width:40px;")
        self.labelContMbappe.setAlignment(Qt.AlignCenter)

        self.layoutMbappe.addWidget(self.btnMbappe)
        self.layoutMbappe.addWidget(self.labelContMbappe)
        self.layoutBotones.addLayout(self.layoutMbappe)


        #BOTON HALLAND
        self.btnHalland = QPushButton("  HALLAND = 20p/s (1000P)")
        iconoHalland = QIcon("img/halland.png")
        self.btnHalland.setIcon(iconoHalland)
        self.btnHalland.setIconSize(QSize(75,75))
        self.btnHalland.setCursor(Qt.PointingHandCursor)

        self.labelContHalland = QLabel("0")
        self.labelContHalland.setStyleSheet("background-color: black; color:white; max-width:40px;")
        self.labelContHalland.setAlignment(Qt.AlignCenter)

        self.layoutHalland.addWidget(self.btnHalland)
        self.layoutHalland.addWidget(self.labelContHalland)
        self.layoutBotones.addLayout(self.layoutHalland)


        #BOTON CRISTIANO
        self.btnCristiano = QPushButton("  CRISTIANO = 30p/s (10000P)")
        iconoCristiano = QIcon("img/cristiano.png")
        self.btnCristiano.setIcon(iconoCristiano)
        self.btnCristiano.setIconSize(QSize(75,75))
        self.btnCristiano.setCursor(Qt.PointingHandCursor)

        self.labelContCristiano = QLabel("0")
        self.labelContCristiano.setStyleSheet("background-color: black; color:white; max-width:40px;")
        self.labelContCristiano.setAlignment(Qt.AlignCenter)

        self.layoutCristiano.addWidget(self.btnCristiano)
        self.layoutCristiano.addWidget(self.labelContCristiano)
        self.layoutBotones.addLayout(self.layoutCristiano)


        #BOTON MESSI
        self.btnMessi = QPushButton("  MESSI = 50p/s (100000P)")
        iconoMessi = QIcon("img/messi.png")
        self.btnMessi.setIcon(iconoMessi)
        self.btnMessi.setIconSize(QSize(75,75))
        self.btnMessi.setCursor(Qt.PointingHandCursor)

        self.labelContMessi = QLabel("0")
        self.labelContMessi.setStyleSheet("background-color: black; color:white; max-width:40px;")
        self.labelContMessi.setAlignment(Qt.AlignCenter)

        self.layoutMessi.addWidget(self.btnMessi)
        self.layoutMessi.addWidget(self.labelContMessi)
        self.layoutBotones.addLayout(self.layoutMessi)


        #APLICAMOS COMPONENTES A LOS LAYOUT/WIDGET
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layoutBotones.addSpacerItem(self.verticalSpacer)

        self.widgetBotones.setLayout(self.layoutBotones)

        self.layoutContenido.addWidget(self.widgetImg)
        self.layoutContenido.addWidget(self.widgetBotones)

        self.layoutVertPrin.addLayout(self.layoutPuntosLevel)
        self.layoutVertPrin.addLayout(self.layoutContenido)

        self.setLayout(self.layoutVertPrin)

        #INSTANCIA DEL CONTROLADOR
        self.miniControlador = minijuegoControlador(self)

        #CONECTAMOS LAS SEÑALES A LOS METODOS
        self.labelImagenBalon.clicked.connect(self.miniControlador.clickarBalon)
        self.btnCastro.clicked.connect(self.miniControlador.sumarCastro)
        self.btnMbappe.clicked.connect(self.miniControlador.sumarMbappe)
        self.btnHalland.clicked.connect(self.miniControlador.sumarHalland)
        self.btnCristiano.clicked.connect(self.miniControlador.sumarCristiano)
        self.btnMessi.clicked.connect(self.miniControlador.sumarMessi)
        self.btnReinicio.clicked.connect(self.miniControlador.reinicioGeneral)


        #CENTRAMOS LA VENTANA
        self.centrarVentana()


    #BACKGROUND
    def dibujarFondoDegradado(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(255, 255, 255))  # Blanco
        gradient.setColorAt(0.7, QColor(200, 200, 200))  # Gris claro
        gradient.setColorAt(1, QColor(0, 0, 0))  # Negro
        painter.setBrush(gradient)
        painter.drawRect(self.rect()) 


    #BACKGROUND FOR WIDGET BOTONES
    def dibujarFondoDegradadoWidgetBotones(self, event):
        painter = QPainter(self.widgetBotones)
        gradient = QLinearGradient(0, 0, 0, self.widgetBotones.height())
        gradient.setColorAt(0, QColor(255, 255, 255))  # Blanco
        gradient.setColorAt(0.7, QColor(200, 200, 200))  # Gris claro
        gradient.setColorAt(1, QColor(0, 0, 0))  # Negro
        painter.setBrush(gradient)
        painter.drawRect(self.widgetBotones.rect())
        pen = QPen(QColor(128, 128, 128), 9)
        painter.setPen(pen)
        painter.drawRect(0, 0, self.widgetBotones.width(), self.widgetBotones.height())


    #CAMPO DE FUTBOL
    def dibujarCampo(self, event):
        painter = QPainter(self.widgetImg)

        # Color de fondo verde
        painter.fillRect(self.widgetImg.rect(), QColor(0, 128, 0))

        # Pen para las líneas blancas
        pen = QPen(QColor(255, 255, 255), 3)
        painter.setPen(pen)

        # Dimensiones del campo
        width = self.widgetImg.width()
        height = self.widgetImg.height()

        # Dibujar líneas de banda y de fondo
        painter.drawRect(10, 10, width - 20, height - 20)

        # Dibujar la línea central
        painter.drawLine(width // 2, 10, width // 2, height - 10)

        # Dibujar el círculo central
        center_circle_radius = min(width, height) * 0.06  # Ajustar el radio del círculo proporcionalmente
        painter.drawEllipse((width // 2) - center_circle_radius, (height // 2) - center_circle_radius, 2 * center_circle_radius, 2 * center_circle_radius)

        # Dibujar el punto de penalti
        penalty_point_radius = 3
        penalty_spot_distance = height * 0.15  # Ajustar la distancia del punto de penalti proporcionalmente

        # Zona de portería izquierda
        painter.drawEllipse(10 + penalty_spot_distance - penalty_point_radius, (height // 2) - penalty_point_radius, 2 * penalty_point_radius, 2 * penalty_point_radius)
        # Zona de portería derecha
        painter.drawEllipse(width - 10 - penalty_spot_distance - penalty_point_radius, (height // 2) - penalty_point_radius, 2 * penalty_point_radius, 2 * penalty_point_radius)

        # Dibujar las áreas de penalti
        penalty_area_width = width * 0.15  # Ajustar el ancho del área de penalti proporcionalmente
        penalty_area_height = height * 0.2  # Ajustar la altura del área de penalti proporcionalmente

        # Área de penalti izquierda
        painter.drawRect(10, (height // 2) - penalty_area_height // 2, penalty_area_width, penalty_area_height)
        # Área de penalti derecha
        painter.drawRect(width - 10 - penalty_area_width, (height // 2) - penalty_area_height // 2, penalty_area_width, penalty_area_height)

        # Dibujar las áreas pequeñas de portería
        goal_area_width = width * 0.06  # Ajustar el ancho del área pequeña de portería proporcionalmente
        goal_area_height = height * 0.1  # Ajustar la altura del área pequeña de portería proporcionalmente

        # Área pequeña de portería izquierda
        painter.drawRect(10, (height // 2) - goal_area_height // 2, goal_area_width, goal_area_height)
        # Área pequeña de portería derecha
        painter.drawRect(width - 10 - goal_area_width, (height // 2) - goal_area_height // 2, goal_area_width, goal_area_height)


    #METODO PARA CENTRAR LA VENTANA
    def centrarVentana(self):
        rect = self.frameGeometry()
        centro_pantalla = self.screen().availableGeometry().center()
        rect.moveCenter(centro_pantalla)
        self.move(rect.topLeft())    




if __name__=="__main__":
    app = QApplication()
    juego = minijuegoActivityVista()
    juego.show()
    app.exec()        

