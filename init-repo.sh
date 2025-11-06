#!/bin/bash

# Script para inicializar el repositorio público de GitHub
# Manual de Usuario - Bot SSAB Chile

echo "========================================="
echo "📦 Inicializando Repositorio GitHub"
echo "========================================="
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -f "README.md" ]; then
    echo "❌ Error: No se encuentra README.md"
    echo "   Ejecuta este script desde el directorio repo-publico/"
    exit 1
fi

echo "✅ Directorio correcto verificado"
echo ""

# Inicializar git si no existe
if [ ! -d ".git" ]; then
    echo "📝 Inicializando repositorio Git..."
    git init
    echo "✅ Git inicializado"
else
    echo "✅ Repositorio Git ya existe"
fi

echo ""
echo "📋 Configurando Git..."

# Configurar nombre de rama principal
git branch -M main

echo "✅ Rama principal configurada: main"
echo ""

# Agregar todos los archivos
echo "📁 Agregando archivos..."
git add .
echo "✅ Archivos agregados"
echo ""

# Hacer commit inicial
echo "💾 Creando commit inicial..."
git commit -m "docs: manual de usuario bot SSAB Chile v2.0

- Manual completo en Markdown
- Versión HTML interactiva
- Presentación PowerPoint
- 12 capturas de pantalla
- Casos de uso prácticos
- FAQ completo
- Información de soporte y contacto"

echo "✅ Commit inicial creado"
echo ""

echo "========================================="
echo "🎯 SIGUIENTE PASO: Crear Repositorio en GitHub"
echo "========================================="
echo ""
echo "1. Ve a: https://github.com/new"
echo ""
echo "2. Configuración recomendada:"
echo "   • Repository name: manual-bot-ssab"
echo "   • Description: Manual de Usuario - Bot de Gestión Comercial SSAB Chile"
echo "   • Public ✅"
echo "   • NO marcar 'Add README' (ya lo tenemos)"
echo "   • NO marcar 'Add .gitignore' (ya lo tenemos)"
echo "   • License: MIT (ya incluida)"
echo ""
echo "3. Luego ejecuta estos comandos:"
echo ""
echo "   git remote add origin https://github.com/laguileracl/manual-bot-ssab.git"
echo "   git push -u origin main"
echo ""
echo "========================================="
echo "✅ Repositorio local listo para publicar"
echo "========================================="
