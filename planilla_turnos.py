import pandas as pd
from datetime import datetime
import os


class GeneradorPlanillaTurnos:
    """
    Generador automático de plantillas de turnos de empresa.
    Convierte datos de turnos en Excel listo para imprimir.
    """
    
    def __init__(self, archivo_entrada=None):
        """
        Inicializa el generador.
        
        Args:
            archivo_entrada (str): Ruta del archivo Excel de entrada (opcional)
        """
        self.turnos = ['Mañana', 'Tarde', 'Noche']
        self.puestos_base = [
            'Jefe de turno',
            'Salidas',
            'Llegadas',
        ]
        self.archivo_entrada = archivo_entrada
    
    def crear_plantilla_vacia(self, output_file='plantilla_turnos_empresa.xlsx'):
        """
        Crea una plantilla vacía lista para rellenar.
        
        Args:
            output_file (str): Nombre del archivo de salida
        """
        datos = []
        
        for turno in self.turnos:
            for puesto in self.puestos_base:
                datos.append({
                    'Turno': turno,
                    'Puesto': puesto,
                    'Empleados asignados': '',
                    'Observaciones': '',
                })
        
        df = pd.DataFrame(datos)
        df.to_excel(output_file, index=False, sheet_name='Plantilla Turnos')
        print(f"✓ Plantilla vacía creada: {output_file}")
        return df
    
    def crear_plantilla_con_ejemplo(self, output_file='plantilla_turnos_ejemplo.xlsx'):
        """
        Crea una plantilla con datos de ejemplo.
        
        Args:
            output_file (str): Nombre del archivo de salida
        """
        datos_ejemplo = [
            {'Turno': 'Mañana', 'Puesto': 'Jefe de turno', 'Empleados asignados': 'Juan García', 'Observaciones': ''},
            {'Turno': 'Mañana', 'Puesto': 'Salidas', 'Empleados asignados': 'María López, Carlos Ruiz', 'Observaciones': ''},
            {'Turno': 'Mañana', 'Puesto': 'Llegadas', 'Empleados asignados': 'Ana Martín', 'Observaciones': ''},
            
            {'Turno': 'Tarde', 'Puesto': 'Jefe de turno', 'Empleados asignados': 'Roberto Sánchez', 'Observaciones': ''},
            {'Turno': 'Tarde', 'Puesto': 'Salidas', 'Empleados asignados': 'Sofia Díaz, Miguel Soto', 'Observaciones': ''},
            {'Turno': 'Tarde', 'Puesto': 'Llegadas', 'Empleados asignados': 'Luis Fernández', 'Observaciones': ''},
            
            {'Turno': 'Noche', 'Puesto': 'Jefe de turno', 'Empleados asignados': 'Pedro Alonso', 'Observaciones': 'Vigilancia nocturna'},
            {'Turno': 'Noche', 'Puesto': 'Salidas', 'Empleados asignados': 'Javier Moreno', 'Observaciones': ''},
            {'Turno': 'Noche', 'Puesto': 'Llegadas', 'Empleados asignados': 'Elena Jiménez', 'Observaciones': ''},
        ]
        
        df = pd.DataFrame(datos_ejemplo)
        df.to_excel(output_file, index=False, sheet_name='Plantilla Turnos')
        print(f"✓ Plantilla con ejemplo creada: {output_file}")
        return df
    
    def leer_y_convertir(self, archivo_entrada, output_file='plantilla_turnos_convertida.xlsx'):
        """
        Lee un archivo Excel y lo convierte al formato estándar.
        
        Args:
            archivo_entrada (str): Ruta del archivo a convertir
            output_file (str): Nombre del archivo de salida
        """
        try:
            df = pd.read_excel(archivo_entrada)
            print(f"✓ Archivo leído: {archivo_entrada}")
            print(f"  Columnas encontradas: {list(df.columns)}")
            print(f"  Filas: {len(df)}")
            
            # Reorganizar según el formato estándar
            df_convertido = self._reorganizar_datos(df)
            
            df_convertido.to_excel(output_file, index=False, sheet_name='Plantilla Turnos')
            print(f"✓ Archivo convertido y guardado: {output_file}")
            return df_convertido
            
        except FileNotFoundError:
            print(f"✗ Error: No se encontró el archivo {archivo_entrada}")
            return None
        except Exception as e:
            print(f"✗ Error al procesar: {str(e)}")
            return None
    
    def _reorganizar_datos(self, df):
        """
        Reorganiza los datos al formato estándar de turnos.
        
        Args:
            df (DataFrame): DataFrame con datos originales
            
        Returns:
            DataFrame: Datos reorganizados
        """
        # Crear estructura estándar
        datos_reorganizados = []
        
        for turno in self.turnos:
            for puesto in self.puestos_base:
                datos_reorganizados.append({
                    'Turno': turno,
                    'Puesto': puesto,
                    'Empleados asignados': '',
                    'Observaciones': '',
                })
        
        return pd.DataFrame(datos_reorganizados)
    
    def agregar_puestos_personalizados(self, output_file='plantilla_turnos_personalizada.xlsx', 
                                       puestos_adicionales=None):
        """
        Crea una plantilla con puestos personalizados.
        
        Args:
            output_file (str): Nombre del archivo de salida
            puestos_adicionales (list): Lista de puestos adicionales
        """
        if puestos_adicionales is None:
            puestos_adicionales = []
        
        todos_puestos = self.puestos_base + puestos_adicionales
        datos = []
        
        for turno in self.turnos:
            for puesto in todos_puestos:
                datos.append({
                    'Turno': turno,
                    'Puesto': puesto,
                    'Empleados asignados': '',
                    'Observaciones': '',
                })
        
        df = pd.DataFrame(datos)
        df.to_excel(output_file, index=False, sheet_name='Plantilla Turnos')
        print(f"✓ Plantilla personalizada creada: {output_file}")
        print(f"  Puestos totales: {len(todos_puestos)}")
        return df


def main():
    """
    Función principal con ejemplos de uso.
    """
    print("="*60)
    print("GENERADOR DE PLANTILLAS DE TURNOS DE EMPRESA")
    print("="*60)
    
    # Crear instancia del generador
    generador = GeneradorPlanillaTurnos()
    
    # Ejemplo 1: Crear plantilla vacía
    print("\n[1] Creando plantilla vacía...")
    generador.crear_plantilla_vacia()
    
    # Ejemplo 2: Crear plantilla con ejemplo
    print("\n[2] Creando plantilla con ejemplo...")
    generador.crear_plantilla_con_ejemplo()
    
    # Ejemplo 3: Crear plantilla personalizada con puestos adicionales
    print("\n[3] Creando plantilla personalizada...")
    puestos_extra = ['Control', 'Vigilancia', 'Mantenimiento']
    generador.agregar_puestos_personalizados(
        output_file='plantilla_turnos_personalizada.xlsx',
        puestos_adicionales=puestos_extra
    )
    
    print("\n" + "="*60)
    print("✓ Proceso completado con éxito")
    print("="*60)


if __name__ == '__main__':
    main()
