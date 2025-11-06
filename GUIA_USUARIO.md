# 📱 Guía de Usuario - Bot de Gestión Comercial SSAB Chile

> **Versión:** 1.0 / **Fecha:** Noviembre 2025
> **Usuario:** @oxcl_bot

> 📸 **Nota:** Esta guía incluye 12 capturas de pantalla reales del bot. Algunas imágenes adicionales estarán disponibles en futuras actualizaciones.

---

## 🎯 Introducción

El **Bot de Gestión Comercial SSAB Chile** es una herramienta desarrollada para facilitar el acceso instantáneo a información crítica del negocio directamente desde Telegram. Diseñado específicamente para el equipo comercial, permite consultar datos de clientes, fichas técnicas de productos, estados de cuenta y análisis de cartera en tiempo real.

### ✨ Beneficios Clave

- ⚡ **Acceso Instantáneo**: Información disponible 24/7 desde cualquier dispositivo
- 📊 **Reportes Profesionales**: Generación automática de Excel con datos actualizados
- 🎯 **Búsqueda Inteligente**: Encuentra clientes y productos rápidamente
- 📈 **Análisis de Cartera**: Visualización completa del estado de cuentas por cobrar
- 🔒 **Seguridad**: Acceso controlado solo para usuarios autorizados

---

## 🔑 Requisitos Previos

### Antes de Comenzar

1. **Telegram Instalado**

   - Versión móvil (iOS/Android) o desktop
   - Cuenta Telegram activa
2. **Acceso Autorizado**

   - Contactar al administrador del sistema
   - Proporcionar tu usuario de Telegram (@usuario)
   - Esperar confirmación de acceso
3. **Conexión a Internet**

   - Necesaria para todas las operaciones
   - Conexión estable recomendada para descargas

---

## 🚀 Inicio y Acceso

### Paso 1: Buscar el Bot

1. Abrir Telegram y, en el buscador superior, escribir: `@oxcl_bot`
2. Seleccionar el bot de la lista de resultados.

![Búsqueda del Bot](assets/01-buscar-bot.png)

### Paso 2: Iniciar Conversación

1. Presionar el botón **"Iniciar"** o **"Start"**. El bot te enviará un mensaje de bienvenida.
2. Si no tienes acceso, recibirás instrucciones para solicitarlo.

![Inicio del Bot](assets/02-inicio-bot.png)

### Paso 3: Verificación de Acceso

El bot verificará automáticamente si tu usuario está autorizado:

- ✅ **Acceso Concedido**: Verás el menú principal
- ❌ **Acceso Denegado**: Contacta al administrador con tu @usuario

---

## 🎮 Funcionalidades Principales

### 📱 Menú Principal

Al iniciar, verás 4 opciones principales:

```
┌─────────────────────────────┐
│  MENÚ PRINCIPAL             │
├─────────────────────────────┤
│  👥 Clientes                │
│  📋 Fichas Técnicas         │
│  💰 Cuentas x Cobrar        │
│  ℹ️  Info SSAB              │
└─────────────────────────────┘
```

![Menú Principal](assets/03-menu-principal.png)

---

## 👥 Gestión de Clientes

### Búsqueda de Clientes

**Acceso:** Menú Principal → 👥 Clientes

#### Opción 1: Búsqueda por Nombre

1. Presionar **"🔍 Buscar por Nombre"**
2. Escribir el nombre del cliente (mínimo 3 letras)
3. Seleccionar de la lista de resultados

**Ejemplo:**

```
Usuario: "Tecno"
Bot: Encontrados 3 clientes:
     • Tecno Industrial S.A.
     • Tecnomaq Ltda.
     • Tecno Metales Chile
```

![Búsqueda por Nombre](assets/04-busqueda-nombre.png)

#### Opción 2: Búsqueda por Código

1. Presionar **"🔢 Buscar por Código"**
2. Ingresar el código SAP del cliente
3. Ver información detallada

**Ejemplo:**

```
Usuario: "C123456"
Bot: [Muestra ficha completa del cliente]
```

### Información del Cliente

Al seleccionar un cliente, obtienes:

```
╔══════════════════════════════════╗
║  INFORMACIÓN DEL CLIENTE         ║
╠══════════════════════════════════╣
║  📌 Nombre: Tecno Industrial S.A.║
║  🔢 Código: C123456              ║
║  👤 Ejecutivo: Juan Pérez        ║
║  📞 Teléfono: +56 9 8765 4321    ║
║  📧 Email: ventas@tecno.cl       ║
║  💳 Línea Crédito: $50.000.000   ║
║  📊 Usado: $32.500.000 (65%)     ║
║  🎯 Disponible: $17.500.000      ║
║  📅 Plazo Pago: 30 días          ║
╚══════════════════════════════════╝
```

![Ficha Cliente](assets/05-ficha-cliente.png)

### Acciones Disponibles

Desde la ficha del cliente puedes:

- 📊 **Ver Estado de Cuenta**: Facturas pendientes y saldos
- 📥 **Descargar Excel**: Reporte detallado en Excel
- 📇 **Exportar Contacto**: Archivo vCard para tu agenda
- 🔙 **Volver**: Regresar al menú anterior

---

## 📋 Fichas Técnicas

### Catálogo de Productos

**Acceso:** Menú Principal → 📋 Fichas Técnicas

#### Navegación por Categorías

El catálogo está organizado en 3 familias principales:

1. **💄 Labios** (Perfiles Labios)

   - Espesores disponibles
   - Dimensiones estándar
   - Aplicaciones
2. **🔲 Mainframe Liner**

   - Perfiles estructurales
   - Especificaciones técnicas
   - Cargas admisibles
3. **⚡ Ripper**

   - Aceros especiales
   - Grados y resistencias
   - Aplicaciones industriales

![Catálogo Productos](assets/06-catalogo.png)

### Búsqueda de Productos

#### Por Código/Nombre

1. Presionar **"🔍 Buscar Producto"**
2. Ingresar código o palabra clave
3. Ver resultados filtrados

**Ejemplo:**

```
Usuario: "LP200"
Bot: 📋 Labios LP200x4.5
     Espesor: 4.5mm
     Largo: 200mm
     [Ver Ficha Completa]
```

### Ficha Técnica Completa

Al seleccionar un producto:

```
╔════════════════════════════════════╗
║  FICHA TÉCNICA                     ║
╠════════════════════════════════════╣
║  📦 Producto: Labios LP200x4.5     ║
║  🔢 Código: LP200-45               ║
║  📏 Dimensiones:                   ║
║     • Largo: 200 mm                ║
║     • Espesor: 4.5 mm              ║
║     • Ancho: 150 mm                ║
║  ⚙️  Material: HARDOX 500          ║
║  💪 Dureza: 500 HBW                ║
║  📊 Peso: 12.5 kg/unidad           ║
║  💵 Precio: $145.000 + IVA         ║
║  📦 Stock: Disponible              ║
║  🚚 Entrega: 3-5 días hábiles      ║
╚════════════════════════════════════╝
```

![Ficha Técnica Parte 1](assets/07-ficha-tecnica-01.png)

![Ficha Técnica Parte 2](assets/07-ficha-tecnica-02.png)

### Acciones Disponibles

- 📄 **Descargar PDF**: Ficha técnica completa en PDF
- 🖼️ **Ver Planos**: Dibujos técnicos y dimensiones
- 💰 **Cotizar**: Generar cotización para cliente
- 📧 **Compartir**: Enviar ficha por email

---

## 💰 Cuentas por Cobrar

### Menú de Análisis

**Acceso:** Menú Principal → 💰 Cuentas x Cobrar

Opciones disponibles:

```
┌──────────────────────────────────┐
│  ANÁLISIS DE CARTERA             │
├──────────────────────────────────┤
│  1️⃣ Facturas Vencidas           │
│  2️⃣ Facturas por Vencer          │
│  3️⃣ Facturas No Vencidas         │
│  4️⃣ Facturas por Cliente         │
│  5️⃣ Top Clientes Morosos         │
│  6️⃣ Estado General Cartera       │
└──────────────────────────────────┘
```

![Menú Cuentas por Cobrar](assets/08-menu-cxc.png)

### 1️⃣ Facturas Vencidas

Visualiza todas las facturas con morosidad:

```
📉 FACTURAS VENCIDAS

Total: $125.340.500
Facturas: 87
Clientes: 23

┌─────────────┬──────────────┬─────────┐
│ Rango       │ Monto        │ % Total │
├─────────────┼──────────────┼─────────┤
│ 1-30 días   │ $45.200.000  │  36%    │
│ 31-60 días  │ $38.500.000  │  31%    │
│ 61-90 días  │ $25.340.500  │  20%    │
│ +90 días    │ $16.300.000  │  13%    │
└─────────────┴──────────────┴─────────┘
```

**Sub-opciones:**

- 👥 **Ver por RSM**: Agrupar por ejecutivo de ventas
- 📊 **Ver Detalle**: Lista completa de facturas
- 📥 **Descargar Excel**: Reporte detallado

![Facturas Vencidas](assets/09-vencidas.png)

### 2️⃣ Facturas por Vencer

Facturas próximas a vencer (próximos 30 días):

```
📅 FACTURAS POR VENCER

Total: $89.750.000
Facturas: 156
Clientes: 45

┌─────────────┬──────────────┬─────────┐
│ Vencimiento │ Monto        │ Factor. │
├─────────────┼──────────────┼─────────┤
│ 0-7 días    │ $32.100.000  │  42     │
│ 8-15 días   │ $28.450.000  │  38     │
│ 16-30 días  │ $29.200.000  │  76     │
└─────────────┴──────────────┴─────────┘
```

![Facturas por Vencer](assets/10-por-vencer.png)

### 3️⃣ Facturas No Vencidas

Facturas al día (vencimiento > 30 días):

```
📗 FACTURAS NO VENCIDAS

Total: $245.890.000
Facturas: 312
Clientes: 89

Promedio días para vencer: 68 días
```

### 4️⃣ Facturas por Cliente

Búsqueda individual del estado de cuenta:

1. Seleccionar **"Facturas por Cliente"**
2. Buscar el cliente
3. Ver estado de cuenta detallado

```
📊 ESTADO DE CUENTA
Cliente: Tecno Industrial S.A.

┌──────────┬────────────┬──────────────┬─────────┐
│ N° Fact. │ Fecha Venc │ Monto        │ Estado  │
├──────────┼────────────┼──────────────┼─────────┤
│ F-001234 │ 2025-11-15 │ $2.500.000   │ Al día  │
│ F-001189 │ 2025-11-08 │ $3.200.000   │ Al día  │
│ F-001045 │ 2025-10-25 │ $1.800.000   │ Vencida │
├──────────┼────────────┼──────────────┼─────────┤
│ TOTAL    │            │ $7.500.000   │         │
└──────────┴────────────┴──────────────┴─────────┘

Vencido: $1.800.000 (11 días mora)
Al día: $5.700.000
```

<!-- ![Estado Cuenta Cliente](assets/11-estado-cuenta.png) -->

> 📸 *Imagen disponible próximamente*

### 5️⃣ Top Clientes Morosos

Ranking de clientes con mayor morosidad:

```
🔴 TOP 10 CLIENTES MOROSOS

1. Cliente Alpha S.A.
   Deuda: $12.500.000 | Mora: 45 días
   
2. Industrias Beta Ltda.
   Deuda: $8.900.000 | Mora: 38 días
   
3. Comercial Gamma
   Deuda: $7.200.000 | Mora: 62 días

[... continúa hasta 10]
```

### 6️⃣ Estado General Cartera

**NUEVA FUNCIONALIDAD** - Vista panorámica completa:

```
📊 ESTADO GENERAL CARTERA

Total Cartera: $461.980.500
Facturas: 555
Clientes: 157

┌──────────────────┬──────────────┬────────┬──────┐
│ Categoría        │ Monto        │ Fact.  │ %    │
├──────────────────┼──────────────┼────────┼──────┤
│ 📗 No Vencidas   │ $245.890.000 │  312   │ 53%  │
│ 📙 0-30 días     │ $45.200.000  │   42   │ 10%  │
│ 📒 31-60 días    │ $38.500.000  │   28   │  8%  │
│ 📕 61-90 días    │ $25.340.500  │   12   │  5%  │
│ 🔴 91-120 días   │ $12.450.000  │    8   │  3%  │
│ ⚫ 121-365 días  │ $8.900.000   │    5   │  2%  │
│ 💀 +365 días     │ $2.700.000   │    3   │  1%  │
├──────────────────┼──────────────┼────────┼──────┤
│ 💰 TOTAL         │ $461.980.500 │  555   │ 100% │
└──────────────────┴──────────────┴────────┴──────┘
```

**Acciones:**

- 👥 **Ver por RSM**: Análisis agrupado por ejecutivo
- 📥 **Descargar Excel**: 5 hojas con detalle completo

<!-- ![Estado General Cartera](assets/12-estado-general.png) -->

> 📸 *Imagen disponible próximamente*

### Vista por RSM (Ejecutivo de Ventas)

Al seleccionar **"Ver por RSM"**:

```
📊 CARTERA POR RSM

┌───────────────────┬──────────────┬────────┬─────────┐
│ RSM               │ Total        │ Fact.  │ Client. │
├───────────────────┼──────────────┼────────┼─────────┤
│ Juan Pérez        │ $125.500.000 │  145   │   32    │
│ María González    │ $98.750.000  │  128   │   28    │
│ Carlos Ramírez    │ $87.230.500  │  106   │   24    │
│ Ana Martínez      │ $75.900.000  │   89   │   19    │
│ Pedro Silva       │ $74.600.000  │   87   │   22    │
├───────────────────┼──────────────┼────────┼─────────┤
│ 💰 TOTAL          │ $461.980.500 │  555   │  125    │
└───────────────────┴──────────────┴────────┴─────────┘
```

**Seleccionar RSM para:**

- 📥 Descargar Excel personalizado con 5 hojas:
  1. **Resumen**: Totales por categoría
  2. **Vencidas**: Facturas en mora
  3. **Por Vencer**: Próximas a vencer
  4. **No Vencidas**: Al día
  5. **Todas**: Detalle completo

<!-- ![Vista por RSM](assets/13-por-rsm.png) -->

> 📸 *Imagen disponible próximamente*

---

## ℹ️ Información SSAB

### Acceso Rápido a Datos Corporativos

**Acceso:** Menú Principal → ℹ️ Info SSAB

Información disponible:

```
┌─────────────────────────────────┐
│  INFORMACIÓN SSAB CHILE         │
├─────────────────────────────────┤
│  📞 Contacto                    │
│  📍 Dirección                   │
│  🏢 Sucursales                  │
│  📧 Emails Departamentos        │
│  🕐 Horarios Atención           │
│  🌐 Sitio Web                   │
└─────────────────────────────────┘
```

### Datos de Contacto

```
📞 CONTACTO SSAB CHILE

Casa Matriz:
📍 Av. Apoquindo 4800, Piso 11
   Las Condes, Santiago

📞 Teléfono: +56 2 2950 3000
📠 Fax: +56 2 2950 3099

📧 Emails:
   • Ventas: ventas@ssab.cl
   • Soporte: soporte@ssab.cl
   • Facturación: facturacion@ssab.cl

🕐 Horario:
   Lunes a Viernes: 08:30 - 18:00
   Sábado: Cerrado
   Domingo: Cerrado

🌐 www.ssab.com/es-cl
```

---

## 💼 Casos de Uso Prácticos

### Caso 1: Consulta Rápida de Cliente en Terreno

**Situación:** Estás visitando un cliente y necesitas verificar su línea de crédito disponible.

**Pasos:**

1. Abrir Telegram → @oxcl_bot
2. Menú Principal → 👥 Clientes
3. 🔍 Buscar por Nombre → Ingresar nombre
4. Ver **Línea Crédito** y **Disponible**

**Tiempo:** 15 segundos

<!-- ![Caso Uso 1](assets/caso-uso-1.png) -->

> 📸 *Imagen disponible próximamente*

---

### Caso 2: Generar Reporte de Morosidad para Reunión

**Situación:** Necesitas un reporte actualizado de clientes morosos para reunión gerencial.

**Pasos:**

1. Menú Principal → 💰 Cuentas x Cobrar
2. 1️⃣ Facturas Vencidas
3. 👥 Ver por RSM
4. Seleccionar tu nombre
5. 📥 Descargar Excel

**Tiempo:** 30 segundos
**Resultado:** Excel con 5 hojas detalladas

<!-- ![Caso Uso 2](assets/caso-uso-2.png) -->

> 📸 *Imagen disponible próximamente*

---

### Caso 3: Enviar Ficha Técnica a Cliente

**Situación:** Cliente solicita información técnica de un producto.

**Pasos:**

1. Menú Principal → 📋 Fichas Técnicas
2. 🔍 Buscar Producto → Ingresar código
3. Ver Ficha Completa
4. 📄 Descargar PDF
5. Compartir PDF con cliente vía WhatsApp/Email

**Tiempo:** 20 segundos

<!-- ![Caso Uso 3](assets/caso-uso-3.png) -->

> 📸 *Imagen disponible próximamente*

---

### Caso 4: Verificar Estado de Cuenta Específico

**Situación:** Cliente consulta sus facturas pendientes.

**Pasos:**

1. Menú Principal → 💰 Cuentas x Cobrar
2. 4️⃣ Facturas por Cliente
3. Buscar cliente
4. Ver estado completo
5. 📥 Descargar Excel si necesita
6. 📧 Enviar al cliente

**Tiempo:** 25 segundos

<!-- ![Caso Uso 4](assets/caso-uso-4.png) -->

> 📸 *Imagen disponible próximamente*

---

### Caso 5: Análisis Panorámico de Cartera

**Situación:** Necesitas visión general del estado de toda la cartera.

**Pasos:**

1. Menú Principal → 💰 Cuentas x Cobrar
2. 6️⃣ Estado General Cartera
3. Revisar distribución por rangos
4. 👥 Ver por RSM para análisis por vendedor
5. 📥 Descargar Excel consolidado

**Tiempo:** 20 segundos
**Resultado:** Vista completa de $461M+ en cartera

<!-- ![Caso Uso 5](assets/caso-uso-5.png) -->

> 📸 *Imagen disponible próximamente*

---

## ❓ Preguntas Frecuentes

### Acceso y Seguridad

**P: ¿Cómo obtengo acceso al bot?**
R: Contacta al administrador del sistema con tu usuario de Telegram (@usuario). El acceso se otorga según tu rol en la empresa.

**P: ¿Es seguro usar el bot?**
R: Sí. El bot tiene control de acceso por usuario, todas las comunicaciones van cifradas por Telegram, y no almacena información sensible localmente.

**P: ¿Puedo usar el bot desde mi celular personal?**
R: Sí, siempre que tu usuario de Telegram esté autorizado.

---

### Datos e Información

**P: ¿Qué tan actualizados están los datos?**
R: Los datos se actualizan diariamente desde el sistema SAP. La información de cartera refleja el cierre del día anterior.

**P: ¿Los precios en las fichas técnicas incluyen IVA?**
R: No, todos los precios mostrados son netos (sin IVA).

**P: ¿Puedo ver facturas pagadas?**
R: Actualmente el bot solo muestra facturas pendientes (por cobrar).

---

### Reportes y Exportaciones

**P: ¿En qué formato se descargan los reportes?**
R: Excel (.xlsx) para reportes de datos, PDF para fichas técnicas, y vCard (.vcf) para contactos.

**P: ¿Cuánto tiempo permanecen los archivos disponibles?**
R: Los archivos generados están disponibles por 24 horas. Después debes volver a generarlos.

**P: ¿Puedo personalizar los reportes?**
R: Actualmente los reportes tienen formatos predefinidos. Para reportes personalizados, contacta al administrador.

---

### Funcionalidades

**P: ¿Puedo registrar pagos desde el bot?**
R: No, el bot es solo de consulta. Los pagos deben registrarse en SAP.

**P: ¿El bot envía notificaciones automáticas?**
R: Actualmente no. Debes ingresar al bot para consultar información.

**P: ¿Puedo solicitar que se agreguen nuevas funcionalidades?**
R: Sí, envía tus sugerencias al administrador del sistema.

---

### Problemas Técnicos

**P: El bot no responde, ¿qué hago?**R:

1. Verifica tu conexión a internet
2. Cierra y abre Telegram
3. Intenta comando /start
4. Si persiste, contacta soporte

**P: ¿Qué hago si un reporte no se genera?**R: Puede deberse a alto volumen de datos. Intenta:

- Filtrar por rango más pequeño
- Usar la opción por RSM individual
- Intentar en horario de menor demanda

**P: Los datos no coinciden con SAP, ¿por qué?**R: Si hay discrepancia, puede deberse a:

- Actualización en proceso (espera 30 min)
- Cambios muy recientes en SAP
- Contacta al administrador si persiste

---

## 📞 Soporte y Contacto

### Canales de Soporte

#### Administrador del Sistema / Soporte Técnico

- 👤 Nombre: Luis Aguilera
- 📧 Email: luis.aguilera@ssab.com
- 📞 WhatsApp: https://wa.me/56973881390

#### Capacitaciones

Para solicitar capacitación del bot para tu equipo:

- 📧 capacitacion@ssab.cl
- 📅 Sesiones grupales cada primer jueves del mes

---

## 📚 Recursos Adicionales

### Documentación Técnica

- [Manual de Administración](../admin/ADMIN_GUIDE.md)
- [Guía de Desarrollo](../dev/DEVELOPER_GUIDE.md)
- [API Reference](../api/API_DOCS.md)

### Videos Tutoriales

- [YouTube: Introducción al Bot](https://youtube.com/ssab-bot-intro)
- [YouTube: Reportes de Cartera](https://youtube.com/ssab-bot-cartera)
- [YouTube: Fichas Técnicas](https://youtube.com/ssab-bot-fichas)

### Actualizaciones

Suscríbete al canal de novedades:

- 📢 Telegram: @ssab_bot_updates
- 📧 Newsletter mensual

---

## 📝 Notas Importantes

### Privacidad y Confidencialidad

⚠️ **IMPORTANTE:**

- La información del bot es confidencial y de uso exclusivo SSAB Chile
- No compartir credenciales de acceso
- No distribuir reportes fuera de la organización
- Usar solo para fines laborales

### Mejores Prácticas

✅ **Recomendaciones:**

- Verificar datos críticos contra SAP antes de decisiones importantes
- Descargar reportes cuando necesites conservar histórico
- Reportar inconsistencias al administrador
- Sugerir mejoras basadas en tu experiencia de uso

---

## 📄 Historial de Versiones

| Versión | Fecha    | Cambios Principales                                                             |
| -------- | -------- | ------------------------------------------------------------------------------- |
| 2.0      | Nov 2025 | • Estado General Cartera `<br>`• Vista por RSM `<br>`• Excel con 5 hojas |
| 1.5      | Oct 2025 | • Top Clientes Morosos `<br>`• Mejoras UI                                   |
| 1.0      | Sep 2025 | • Lanzamiento inicial `<br>`• Funciones básicas                            |

---

## ✅ Checklist de Inicio Rápido

Usa esta lista para verificar que dominas las funciones esenciales:

- [ ] He iniciado conversación con @oxcl_bot
- [ ] Puedo buscar un cliente por nombre
- [ ] Puedo ver la línea de crédito de un cliente
- [ ] Sé cómo buscar una ficha técnica
- [ ] Puedo descargar un PDF de producto
- [ ] Entiendo los rangos de morosidad
- [ ] Sé generar reporte de facturas vencidas
- [ ] Puedo usar la vista Estado General Cartera
- [ ] Sé filtrar por mi RSM
- [ ] Puedo descargar reportes Excel

**Si has completado todos los ítems, ¡estás listo para usar el bot profesionalmente! 🎉**

---

<div align="center">

**Bot de Gestión Comercial SSAB Chile**
*Versión 2.0 - Noviembre 2025*

---

*Para más información, contacta a soporte.bot@ssab.cl*

</div>
