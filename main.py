import sys
import os

# Configurar la variable de entorno para que Matplotlib sepa que debe usar PySide6
os.environ['QT_API'] = 'pyside6'

import numpy as np
import matplotlib

# Indicarle a Matplotlib que el motor de renderizado gráfico será Qt
matplotlib.use('QtAgg')

# Importar la clase que convierte la figura de Matplotlib en un widget compatible con Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

# Importar la clase que crea el lienzo o contenedor gráfico general
from matplotlib.figure import Figure

# Importar las herramientas base de PySide6 para la ventana y el diseño
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout

# Importar la clase visual generada desde el archivo .ui compilado
from nuevo import Ui_MainWindow


class AnalizadorApp(QMainWindow, Ui_MainWindow):

    # QMainWindow: Es una clase base de PySide6 que representa una ventana principal.
    # Ui_MainWindow: Es la clase de diseño creada a partir del archivo analizador.ui.
    # AnalizadorApp: Es una nueva clase que hereda las propiedades de ambas clases.

    def __init__(self):
        super().__init__()

        # Cargar los componentes visuales de la interfaz en esta ventana
        self.setupUi(self)

        # Establecer los valores predeterminados en las cajas de texto
        # textEdit corresponde a la amplitud
        self.textEdit.setPlainText("1.0")

        # textEdit_2 corresponde a la frecuencia
        self.textEdit_2.setPlainText("2.0")

        # Crear la figura gráfica con fondo blanco
        self.figure = Figure(facecolor='#FFFFFF')

        # Empaquetar la figura en un lienzo compatible con Qt
        self.canvas = FigureCanvas(self.figure)

        # Añadir un sistema de ejes cartesiano 2D sobre la figura
        self.ax = self.figure.add_subplot(111)

        # Crear un layout vertical dentro del widget contenedor
        layout = QVBoxLayout(self.widget)

        # Eliminar márgenes alrededor del lienzo
        layout.setContentsMargins(0, 0, 0, 0)

        # Insertar el gráfico de Matplotlib dentro del widget
        layout.addWidget(self.canvas)

        # Conectar el botón con el método de actualización del gráfico
        self.MainWindow_2.clicked.connect(self.actualizar_grafico)

        # Renderizar la gráfica inicial al abrir la aplicación
        self.actualizar_grafico()

    def actualizar_grafico(self):

        # Obtener y convertir la amplitud ingresada
        try:
            amplitud = float(self.textEdit.toPlainText().strip())
        except ValueError:
            amplitud = 1.0

        # Obtener y convertir la frecuencia ingresada
        try:
            frecuencia = float(self.textEdit_2.toPlainText().strip())
        except ValueError:
            frecuencia = 2.0

        # Generar vector de tiempo de 0 a 2 segundos con 1000 puntos
        t = np.linspace(0, 2, 1000)

        # Calcular los valores de la onda senoidal:
        # y(t) = A * sin(2 * pi * f * t)
        y = amplitud * np.sin(2 * np.pi * frecuencia * t)

        # Limpiar los trazos y ejes de la gráfica anterior
        self.ax.clear()

        # Establecer el color de fondo del área de trazado en blanco
        self.ax.set_facecolor('#FFFFFF')

        # Trazar la señal senoidal
        self.ax.plot(t, y, color='#00a2ff', linewidth=2.5)

        # Definir etiquetas de los ejes X e Y
        self.ax.set_xlabel('Tiempo (s)', color='black', fontsize=11)
        self.ax.set_ylabel('Amplitud', color='black', fontsize=11)

        # Configurar en negro los números y marcas de los ejes
        self.ax.tick_params(colors='black')

        # Activar la rejilla punteada
        self.ax.grid(True, linestyle='--', alpha=0.5, color='gray')

        # Recorrer los cuatro bordes del gráfico y pintarlos de negro
        for spine in self.ax.spines.values():
            spine.set_color('black')

        # Reajustar automáticamente los márgenes internos
        self.figure.tight_layout()

        # Redibujar la figura en pantalla
        self.canvas.draw()


if __name__ == "__main__":

    # Inicializar el administrador de la aplicación Qt
    app = QApplication(sys.argv)

    # Crear una instancia de la ventana principal
    window = AnalizadorApp()

    # Mostrar la ventana en pantalla
    window.show()

    # Iniciar el bucle de eventos
    sys.exit(app.exec())