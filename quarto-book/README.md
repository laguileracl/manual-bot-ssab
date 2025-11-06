# 📚 Quarto Book - Manual de Usuario Bot SSAB Chile

Este directorio contiene el código fuente del libro Quarto para el manual de usuario.

## 🚀 Inicio Rápido

### Ver el libro localmente

```bash
# Renderizar y abrir en el navegador
quarto render
open _book/index.html
```

### Publicar en GitHub Pages

```bash
# Opción fácil: usa el script automatizado
./publish.sh

# O manualmente:
quarto render
# Luego copiar al repo público y hacer push
```

Ver [PUBLICACION.md](PUBLICACION.md) para instrucciones detalladas.

## 📖 Formatos Disponibles

### HTML (para web)

```bash
quarto render
```

El sitio web se generará en `_book/`

### PDF

```bash
quarto render --to pdf
```

El PDF se generará en `_book/Manual-de-Usuario---Bot-SSAB-Chile.pdf`

## 📁 Estructura

```
quarto-book/
├── _quarto.yml           # Configuración principal del libro
├── custom.scss           # Estilos personalizados SSAB
├── index.qmd            # Página de inicio
├── intro.qmd            # Introducción
├── requisitos.qmd       # Requisitos previos
├── inicio.qmd           # Inicio y acceso
├── clientes.qmd         # Gestión de clientes
├── fichas.qmd           # Fichas técnicas
├── cuentas.qmd          # Cuentas por cobrar
├── info-ssab.qmd        # Información SSAB
├── casos-uso.qmd        # Casos de uso
├── faq.qmd              # Preguntas frecuentes
├── references.qmd       # Referencias y contacto
├── references.bib       # Bibliografía
├── assets/              # Capturas de pantalla
└── _book/               # Sitio generado (HTML)
```

## 🌐 Publicar en GitHub Pages

### Opción 1: GitHub Actions (Automático)

1. Crear `.github/workflows/quarto-publish.yml`:

```yaml
name: Publish Quarto Book

on:
  push:
    branches: [main]
    paths:
      - 'docs/user-guide/quarto-book/**'

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        
      - name: Render Quarto Book
        run: |
          cd docs/user-guide/quarto-book
          quarto render
          
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs/user-guide/quarto-book/_book
```

### Opción 2: Manual

```bash
# 1. Renderizar el libro
quarto render

# 2. Publicar (desde el directorio quarto-book)
quarto publish gh-pages
```

## 🎨 Personalización

### Colores SSAB

Los colores corporativos están definidos en `custom.scss`:

- **Primario**: #002F6C (azul SSAB)
- **Secundario**: #E2001A (rojo SSAB)

### Temas

Puedes cambiar el tema en `_quarto.yml`:

```yaml
format:
  html:
    theme: [cosmo, custom.scss]  # Cambiar 'cosmo' por otro tema
```

Temas disponibles: cosmo, flatly, journal, litera, lumen, lux, materia, minty, pulse, sandstone, simplex, sketchy, slate, solar, spacelab, superhero, united, yeti, zephyr

## 📝 Actualizar Contenido

Para actualizar el contenido:

1. Editar `GUIA_USUARIO.md` (un nivel arriba)
2. Ejecutar `python3 convert_manual_to_quarto.py`
3. Renderizar: `quarto render`

## 🔗 Enlaces

- [Quarto Documentation](https://quarto.org)
- [Quarto Books](https://quarto.org/docs/books/)
- [GitHub Pages](https://pages.github.com/)
