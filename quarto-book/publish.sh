#!/bin/bash
# Script para publicar el libro Quarto en GitHub Pages

set -e  # Exit on error

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_PUBLICO="$SCRIPT_DIR/../repo-publico"

echo "📚 Publicación del Libro Quarto - Manual Bot SSAB Chile"
echo "========================================================="
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -f "$SCRIPT_DIR/_quarto.yml" ]; then
    echo "❌ Error: No se encuentra _quarto.yml"
    echo "   Asegúrate de ejecutar este script desde quarto-book/"
    exit 1
fi

# Paso 1: Renderizar el libro
echo "📝 Paso 1: Renderizando el libro..."
quarto render
echo "✅ Libro renderizado exitosamente"
echo ""

# Paso 2: Copiar al repositorio público
echo "📦 Paso 2: Preparando para publicación..."

# Verificar que existe el repo público
if [ ! -d "$REPO_PUBLICO" ]; then
    echo "❌ Error: No se encuentra el repositorio público en:"
    echo "   $REPO_PUBLICO"
    exit 1
fi

cd "$REPO_PUBLICO"

# Verificar que es un repositorio git
if [ ! -d ".git" ]; then
    echo "❌ Error: $REPO_PUBLICO no es un repositorio git"
    exit 1
fi

# Crear directorio para el libro
echo "   Creando directorio quarto-book..."
mkdir -p quarto-book

# Copiar archivos (excepto _book y .quarto que se generarán en GitHub)
echo "   Copiando archivos del libro..."
rsync -av --delete \
    --exclude='_book' \
    --exclude='.quarto' \
    --exclude='*.pyc' \
    --exclude='__pycache__' \
    --exclude='.DS_Store' \
    "$SCRIPT_DIR/" quarto-book/

# Mover el workflow a la ubicación correcta
echo "   Configurando GitHub Actions..."
mkdir -p .github/workflows

if [ -f "quarto-book/.github/workflows/quarto-publish.yml" ]; then
    cp quarto-book/.github/workflows/quarto-publish.yml .github/workflows/
    rm -rf quarto-book/.github
    echo "   ✅ Workflow de GitHub Actions configurado"
fi

echo "✅ Archivos preparados"
echo ""

# Paso 3: Mostrar cambios
echo "📋 Paso 3: Cambios detectados:"
git status --short
echo ""

# Paso 4: Confirmar publicación
read -p "¿Deseas continuar con la publicación? (s/N): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Ss]$ ]]; then
    echo "❌ Publicación cancelada"
    exit 0
fi

# Paso 5: Commit y push
echo "🚀 Paso 4: Publicando en GitHub..."

git add .

# Mensaje de commit personalizado o por defecto
read -p "Mensaje de commit (Enter para usar por defecto): " COMMIT_MSG

if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="docs: update Quarto book for GitHub Pages"
fi

git commit -m "$COMMIT_MSG" || {
    echo "⚠️  No hay cambios para commitear"
    exit 0
}

git push origin main

echo ""
echo "✅ ¡Publicación completada exitosamente!"
echo ""
echo "🌐 El sitio web se actualizará en unos minutos en:"
echo "   https://laguileracl.github.io/manual-bot-ssab/"
echo ""
echo "📊 Puedes ver el progreso en:"
echo "   https://github.com/laguileracl/manual-bot-ssab/actions"
echo ""
echo "⏱️  El despliegue usualmente toma 1-2 minutos"
