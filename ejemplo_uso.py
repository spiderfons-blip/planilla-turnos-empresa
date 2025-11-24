#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejemplos de uso del generador de plantillas de turnos.

Este archivo muestra cómo usar la clase GeneradorPlanillaTurnos
para crear diferentes tipos de plantillas.
"""

from planilla_turnos import GeneradorPlanillaTurnos


def ejemplo_1_plantilla_vacia():
    """
    Ejemplo 1: Crear una plantilla vacía.
    Uso: cuando necesitas una plantilla en blanco para rellenar.
    """
    print("\n" + "="*50)
    print("EJEMPLO 1: Plantilla vacía")
    print("="*50)
    
    generador = GeneradorPlanillaTurnos()
    generador.crear_plantilla_vacia('plantilla_vacia.xlsx')
    print("\n✓ Plantilla vacía creada en: plantilla_vacia.xlsx")


def ejemplo_2_plantilla_con_ejemplo():
    """
    Ejemplo 2: Crear una plantilla con datos de ejemplo.
    Uso: como referencia o para ver la estructura con datos reales.
    """
    print("\n" + "="*50)
    print("EJEMPLO 2: Plantilla con datos de ejemplo")
    print("="*50)
    
    generador = GeneradorPlanillaTurnos()
    generador.crear_plantilla_con_ejemplo('plantilla_ejemplo.xlsx')
    print("\n✓ Plantilla con ejemplo creada en: plantilla_ejemplo.xlsx")


def ejemplo_3_plantilla_personalizada():
    """
    Ejemplo 3: Crear una plantilla con puestos personalizados.
    Uso: cuando tu empresa tiene puestos adicionales además de los estándar.
    """
    print("\n" + "="*50)
    print("EJEMPLO 3: Plantilla personalizada con puestos adicionales")
    print("="*50)
    
    generador = GeneradorPlanillaTurnos()
    
    # Definir puestos adicionales según tu empresa
    puestos_adicionales = [
        'Control de calidad',
        'Vigilancia',
        'Mantenimiento',
        'Limpieza'
    ]
    
    generador.agregar_puestos_personalizados(
        output_file='plantilla_personalizada.xlsx',
        puestos_adicionales=puestos_adicionales
    )
    print("\n✓ Plantilla personalizada creada en: plantilla_personalizada.xlsx")


def ejemplo_4_personalizar_clase():
    """
    Ejemplo 4: Personalizar los turnos y puestos base.
    Uso: cuando tu empresa tiene diferentes turnos o puestos base.
    """
    print("\n" + "="*50)
    print("EJEMPLO 4: Personalizar turnos y puestos base")
    print("="*50)
    
    # Crear generador personalizado
    generador = GeneradorPlanillaTurnos()
    
    # Personalizar turnos (por ejemplo, solo 2 turnos)
    generador.turnos = ['Matutino', 'Vespertino']
    
    # Personalizar puestos base
    generador.puestos_base = [
        'Encargado',
        'Personal de entrada',
        'Personal de salida',
        'Operador'
    ]
    
    generador.crear_plantilla_vacia('plantilla_personalizada2.xlsx')
    print("\n✓ Plantilla personalizada creada en: plantilla_personalizada2.xlsx")
    print("  Turnos: Matutino, Vespertino")
    print("  Puestos: Encargado, Personal de entrada, Personal de salida, Operador")


if __name__ == '__main__':
    print("\n" + "#"*50)
    print("# EJEMPLOS DE USO - GENERADOR DE PLANTILLAS DE TURNOS")
    print("#"*50)
    
    # Ejecutar todos los ejemplos
    ejemplo_1_plantilla_vacia()
    ejemplo_2_plantilla_con_ejemplo()
    ejemplo_3_plantilla_personalizada()
    ejemplo_4_personalizar_clase()
    
    print("\n" + "#"*50)
    print("# ✓ TODOS LOS EJEMPLOS SE HAN EJECUTADO CORRECTAMENTE")
    print("#"*50)
    print("\nArchivos generados:")
    print("  - plantilla_vacia.xlsx")
    print("  - plantilla_ejemplo.xlsx")
    print("  - plantilla_personalizada.xlsx")
    print("  - plantilla_personalizada2.xlsx")
    print("\nAbra cualquiera de estos archivos en Excel para ver el resultado.\n")
