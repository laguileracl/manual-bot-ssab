# 📚 Guía de Publicación en GitHub Pages

Esta guía te ayudará a publicar el libro Quarto del manual de usuario en GitHub Pages.

## 🎯 Opción 1: Publicación Automática con GitHub Actions (Recomendada)

### Paso 1: Configurar GitHub Pages

1. Ve a tu repositorio en GitHub: `https://github.com/laguileracl/manual-bot-ssab`
2. Click en **Settings** (Configuración)
3. En el menú lateral, click en **Pages**
4. En **Source**, selecciona **GitHub Actions**
5. Guarda los cambios

### Paso 2: Copiar el Workflow

Ya está creado el archivo `.github/workflows/quarto-publish.yml` en el directorio `quarto-book`.

Necesitas moverlo a la raíz del proyecto:

```bash
cd "/Users/laa/Projects/ssabchilebot RAILWAY/ssabchilebot"
mkdir -p .github/workflows
cp docs/user-guide/quarto-book/.github/workflows/quarto-publish.yml .github/workflows/
```

### Paso 3: Publicar

Ahora copia todo el contenido de quarto-book al repositorio público:

```bash
# Ir al repositorio público
cd "/Users/laa/Projects/ssabchilebot RAILWAY/ssabchilebot/docs/user-guide/repo-publico"

# Crear directorio para el libro Quarto
mkdir -p quarto-book

# Copiar todo excepto _book (se generará en GitHub)
rsync -av --exclude='_book' --exclude='.quarto' \
  ../quarto-book/ quarto-book/

# Mover el workflow a la ubicación correcta
mkdir -p .github/workflows
mv quarto-book/.github/workflows/quarto-publish.yml .github/workflows/

# Agregar y commitear
git add .
git commit -m "docs: add Quarto book for GitHub Pages

- Add complete Quarto book structure
- Add GitHub Actions workflow for automatic publishing
- Include all chapters and assets
- Configure SSAB branding and styles"

# Publicar
git push origin main
```

### Paso 4: Verificar la Publicación

1. Ve a tu repositorio en GitHub
2. Click en la pestaña **Actions**
3. Deberías ver el workflow "Publish Quarto Book to GitHub Pages" ejecutándose
4. Una vez completado (✅), ve a **Settings** → **Pages**
5. Verás la URL de tu sitio: `https://laguileracl.github.io/manual-bot-ssab/`

---

## 🎯 Opción 2: Publicación Manual con Quarto CLI

Si prefieres publicar manualmente:

```bash
cd "/Users/laa/Projects/ssabchilebot RAILWAY/ssabchilebot/docs/user-guide/quarto-book"

# Publicar directamente desde Quarto
quarto publish gh-pages
```

Quarto te pedirá confirmación y luego:
1. Renderizará el libro
2. Creará/actualizará la rama `gh-pages`
3. Hará push automáticamente

---

## 🎯 Opción 3: Publicación Manual con Git

```bash
# 1. Renderizar el libro
cd "/Users/laa/Projects/ssabchilebot RAILWAY/ssabchilebot/docs/user-guide/quarto-book"
quarto render

# 2. Ir al repositorio público
cd ../repo-publico

# 3. Crear/actualizar rama gh-pages
git checkout --orphan gh-pages 2>/dev/null || git checkout gh-pages

# 4. Limpiar todo
git rm -rf . 2>/dev/null || true
rm -rf *

# 5. Copiar el contenido renderizado
cp -r ../quarto-book/_book/* .

# 6. Crear .nojekyll (importante para GitHub Pages)
touch .nojekyll

# 7. Commit y push
git add .
git commit -m "docs: update Quarto book site"
git push origin gh-pages --force

# 8. Volver a main
git checkout main
```

---

## 📝 Actualizar el Libro

### Cuando edites el contenido:

1. **Editar el manual principal:**
   ```bash
   cd "/Users/laa/Projects/ssabchilebot RAILWAY/ssabchilebot/docs/user-guide"
   # Editar GUIA_USUARIO.md
   ```

2. **Regenerar capítulos Quarto:**
   ```bash
   cd quarto-book
   python3 convert_manual_to_quarto.py
   ```

3. **Renderizar localmente para probar:**
   ```bash
   quarto render
   open _book/index.html
   ```

4. **Publicar:**
   - **Con GitHub Actions:** Solo haz commit y push al repo público
   - **Manual:** Ejecuta `quarto publish gh-pages`

---

## 🎨 Personalización del Sitio

### Cambiar Colores

Edita `custom.scss`:

```scss
$primary: #002F6C;    // Azul SSAB
$secondary: #E2001A;  // Rojo SSAB
```

### Cambiar Tema

Edita `_quarto.yml`:

```yaml
format:
  html:
    theme: [cosmo, custom.scss]  # Cambiar 'cosmo'
```

Temas disponibles: cosmo, flatly, journal, litera, lumen, lux, materia, minty, pulse, sandstone, simplex, sketchy, slate, solar, spacelab, superhero, united, yeti, zephyr

### Agregar Logo

1. Agregar imagen del logo a `assets/ssab-logo.png`
2. Editar `_quarto.yml`:

```yaml
book:
  title: "Manual de Usuario - Bot SSAB Chile"
  cover-image: assets/ssab-logo.png
```

---

## 🔗 Enlaces Útiles

- [Quarto Books](https://quarto.org/docs/books/)
- [Quarto Publishing](https://quarto.org/docs/publishing/github-pages.html)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## ❓ Solución de Problemas

### El sitio no se actualiza

1. Verifica que GitHub Pages esté habilitado en Settings → Pages
2. Revisa que la fuente sea "GitHub Actions"
3. Mira los logs en la pestaña Actions para ver errores
4. Espera 1-2 minutos después del push para que se actualice

### Error 404

1. Verifica que `.nojekyll` existe en la rama gh-pages
2. Asegúrate que el contenido está en la raíz de gh-pages
3. Verifica la URL: debe ser `https://laguileracl.github.io/manual-bot-ssab/`

### Las imágenes no se ven

1. Verifica que las rutas en los .qmd usen `assets/` correctamente
2. Asegúrate que las imágenes estén en `quarto-book/assets/`
3. Re-renderiza: `quarto render`

### Warnings de Citeproc

Son normales para `@usuario`, `@oxcl_bot`, etc. No afectan la generación.
Para eliminarlos, usa comillas invertidas: `` `@usuario` ``

---

## 📊 Resultado Final

Una vez publicado, tendrás:

- 🌐 Sitio web profesional en `https://laguileracl.github.io/manual-bot-ssab/`
- 📱 Diseño responsive (funciona en móvil)
- 🔍 Búsqueda integrada
- 📖 Navegación por capítulos
- 🎨 Branding SSAB (colores corporativos)
- 📄 Versión PDF descargable
- 🔄 Actualización automática con cada push (si usas GitHub Actions)
