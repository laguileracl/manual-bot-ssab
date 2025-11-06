# 🎉 Libro Quarto - Manual de Usuario Bot SSAB Chile

## ✅ Lo que se ha creado

Se ha generado un **libro profesional con Quarto** que será publicado como sitio web en GitHub Pages.

### 📁 Estructura del Proyecto

```
quarto-book/
├── 📝 Archivos de configuración
│   ├── _quarto.yml           # Configuración principal del libro
│   ├── custom.scss            # Estilos SSAB (colores corporativos)
│   ├── references.bib         # Bibliografía
│   └── .gitignore            # Archivos a ignorar
│
├── 📖 Capítulos del libro (10 archivos .qmd)
│   ├── index.qmd             # Página de inicio con bienvenida
│   ├── intro.qmd             # Introducción y beneficios
│   ├── requisitos.qmd        # Requisitos previos
│   ├── inicio.qmd            # Inicio y acceso al bot
│   ├── clientes.qmd          # Gestión de clientes
│   ├── fichas.qmd            # Fichas técnicas
│   ├── cuentas.qmd           # Cuentas por cobrar
│   ├── info-ssab.qmd         # Información SSAB
│   ├── casos-uso.qmd         # Casos de uso prácticos
│   └── faq.qmd              # Preguntas frecuentes
│   └── references.qmd        # Referencias y contacto
│
├── 🖼️ Assets
│   └── assets/               # 12 capturas de pantalla
│
├── 🔧 Scripts y utilidades
│   ├── convert_manual_to_quarto.py  # Convierte GUIA_USUARIO.md → capítulos .qmd
│   └── publish.sh                    # Script para publicar en GitHub Pages
│
├── 📚 Documentación
│   ├── README.md             # Guía rápida
│   ├── PUBLICACION.md        # Guía detallada de publicación
│   └── ESTRUCTURA.txt        # Esta estructura
│
└── 🌐 Sitio generado
    └── _book/                # Sitio web HTML (generado con `quarto render`)
```

---

## 🎨 Características del Sitio Web

### Diseño Profesional
- ✅ Colores corporativos SSAB (azul #002F6C, rojo #E2001A)
- ✅ Tema responsive (funciona en desktop, tablet y móvil)
- ✅ Navegación lateral con todos los capítulos
- ✅ Búsqueda integrada (🔍)
- ✅ Emojis preservados en todo el contenido

### Funcionalidades
- ✅ Tabla de contenidos automática
- ✅ Numeración de secciones
- ✅ Enlaces internos entre capítulos
- ✅ Imágenes con sombras y bordes redondeados
- ✅ Botón de GitHub en la barra superior
- ✅ Pie de página con marca SSAB

### Formatos de Salida
- ✅ **HTML**: Sitio web interactivo
- ✅ **PDF**: Documento descargable (opcional)

---

## 🚀 Cómo Usar

### 1. Ver Localmente

```bash
cd "/Users/laa/Projects/ssabchilebot RAILWAY/ssabchilebot/docs/user-guide/quarto-book"

# Renderizar el libro
quarto render

# Abrir en el navegador
open _book/index.html
```

### 2. Publicar en GitHub Pages

**Opción A: Automático (Recomendado)**

```bash
./publish.sh
```

Este script:
1. Renderiza el libro
2. Copia los archivos al repo público
3. Configura GitHub Actions
4. Hace commit y push
5. GitHub Actions desplegará automáticamente

**Opción B: Manual**

```bash
quarto publish gh-pages
```

Ver instrucciones completas en [PUBLICACION.md](PUBLICACION.md)

### 3. Actualizar Contenido

Cuando edites el manual:

```bash
# 1. Editar el manual principal
vim ../GUIA_USUARIO.md

# 2. Regenerar capítulos
python3 convert_manual_to_quarto.py

# 3. Renderizar
quarto render

# 4. Publicar
./publish.sh
```

---

## 🌐 URL del Sitio Publicado

Una vez publicado en GitHub Pages, el sitio estará disponible en:

**https://laguileracl.github.io/manual-bot-ssab/**

---

## 📊 Ventajas de Quarto vs HTML Simple

| Característica | HTML Simple | Quarto Book |
|----------------|-------------|-------------|
| Navegación por capítulos | ❌ | ✅ |
| Búsqueda integrada | ❌ | ✅ |
| Tabla de contenidos | Manual | Automática |
| Responsive design | Manual | Automático |
| Temas predefinidos | ❌ | ✅ (25 temas) |
| Generación PDF | Manual | Automática |
| Referencias cruzadas | Manual | Automáticas |
| Numeración secciones | Manual | Automática |
| Actualización | Difícil | Fácil (scripts) |
| SEO y metadata | Manual | Automático |

---

## 🎯 Próximos Pasos

1. **Ver el sitio localmente**
   ```bash
   quarto render
   open _book/index.html
   ```

2. **Si te gusta, publicar en GitHub Pages**
   ```bash
   ./publish.sh
   ```

3. **Configurar GitHub Pages** (si no está configurado)
   - Ve a Settings → Pages
   - Source: GitHub Actions
   - Guarda

4. **Esperar 1-2 minutos** y visitar:
   https://laguileracl.github.io/manual-bot-ssab/

---

## 🆘 Ayuda

- **README.md**: Guía rápida
- **PUBLICACION.md**: Instrucciones detalladas de publicación
- **Documentación Quarto**: https://quarto.org/docs/books/

---

## 📝 Notas

- Los archivos `.qmd` son archivos Quarto Markdown (similar a Markdown pero con superpoderes)
- El directorio `_book/` se genera automáticamente (no editarlo manualmente)
- El directorio `.quarto/` es temporal (cache de Quarto)
- Los estilos personalizados están en `custom.scss`
- La configuración principal está en `_quarto.yml`

---

**¡Listo para publicar! 🚀**
