# Planilla de Turnos de Empresa

Generador automatico de plantillas de turnos de empresa en Python. Convierte datos de turnos (manana, tarde, noche) con puestos (jefe de turno, salidas, llegadas) en una hoja de calculo lista para imprimir.

## Caracteristicas

- **Generacion automatica de plantillas** en formato Excel
- **Personalizable**: Anade puestos o turnos segun tus necesidades
- **Estructura organizada**: Datos organizados por filas (Turno - Puesto - Empleados)
- **Plantilla vacia o con ejemplo** para usar como referencia
- **Facil de usar**: API simple y clara
- **Flexible**: Personaliza los turnos y puestos base

## Instalacion

### Prerequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clona el repositorio**:
```bash
git clone https://github.com/tu-usuario/planilla-turnos-empresa.git
cd planilla-turnos-empresa
```

2. **Instala las dependencias**:
```bash
pip install -r requirements.txt
```

## Uso Rapido

### Opcion 1: Ejecutar el programa principal

```bash
python planilla_turnos.py
```

Esto generara tres plantillas Excel automaticamente:
- `plantilla_turnos_empresa.xlsx` - Plantilla vacia
- `plantilla_turnos_ejemplo.xlsx` - Plantilla con datos de ejemplo
- `plantilla_turnos_personalizada.xlsx` - Plantilla con puestos adicionales

### Opcion 2: Ejecutar los ejemplos

```bash
python ejemplo_uso.py
```

Verás 4 ejemplos diferentes de cómo usar el generador.

## Uso Avanzado

### En tu propio codigo Python

```python
from planilla_turnos import GeneradorPlanillaTurnos

# Crear una instancia del generador
generador = GeneradorPlanillaTurnos()

# Crear una plantilla vacia
generador.crear_plantilla_vacia('mi_plantilla.xlsx')

# Crear una plantilla con puestos adicionales
puestos_extra = ['Control', 'Vigilancia', 'Mantenimiento']
generador.agregar_puestos_personalizados(
    output_file='plantilla_completa.xlsx',
    puestos_adicionales=puestos_extra
)
```

## Estructura del Proyecto

```
planilla-turnos-empresa/
├── README.md                           # Este archivo
├── requirements.txt                    # Dependencias del proyecto
├── planilla_turnos.py                  # Modulo principal
├── ejemplo_uso.py                      # Ejemplos de uso
```

## Dependencias

- **pandas** (>=1.3.0): Para manipulacion de datos
- **openpyxl** (>=3.6.0): Para trabajar con archivos Excel

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto esta bajo la Licencia MIT.

## Autor

Creado para ayudar a simplificar la gestion de turnos de empresa.

---

**Ultima actualizacion:** Noviembre 2024
