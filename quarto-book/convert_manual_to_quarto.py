#!/usr/bin/env python3
"""
Convierte GUIA_USUARIO.md en capítulos Quarto separados
"""
import re
from pathlib import Path

def split_manual_into_chapters():
    """Lee el manual y lo divide en capítulos Quarto"""
    
    # Leer el manual completo
    manual_path = Path("../GUIA_USUARIO.md")
    content = manual_path.read_text(encoding="utf-8")
    
    # Definir los capítulos y sus archivos
    chapters = [
        {
            "file": "intro.qmd",
            "title": "Introducción",
            "start_marker": "## 🎯 Introducción",
            "end_marker": "## 🔑 Requisitos Previos"
        },
        {
            "file": "requisitos.qmd",
            "title": "Requisitos Previos",
            "start_marker": "## 🔑 Requisitos Previos",
            "end_marker": "## 🚀 Inicio y Acceso"
        },
        {
            "file": "inicio.qmd",
            "title": "Inicio y Acceso",
            "start_marker": "## 🚀 Inicio y Acceso",
            "end_marker": "## 🎮 Funcionalidades Principales"
        },
        {
            "file": "clientes.qmd",
            "title": "Gestión de Clientes",
            "start_marker": "## 👥 Gestión de Clientes",
            "end_marker": "## 📋 Fichas Técnicas"
        },
        {
            "file": "fichas.qmd",
            "title": "Fichas Técnicas",
            "start_marker": "## 📋 Fichas Técnicas",
            "end_marker": "## 💰 Cuentas por Cobrar"
        },
        {
            "file": "cuentas.qmd",
            "title": "Cuentas por Cobrar",
            "start_marker": "## 💰 Cuentas por Cobrar",
            "end_marker": "## ℹ️ Información sobre SSAB"
        },
        {
            "file": "info-ssab.qmd",
            "title": "Información sobre SSAB",
            "start_marker": "## ℹ️ Información SSAB",
            "end_marker": "## 💼 Casos de Uso Prácticos"
        },
        {
            "file": "casos-uso.qmd",
            "title": "Casos de Uso",
            "start_marker": "## 💼 Casos de Uso Prácticos",
            "end_marker": "## ❓ Preguntas Frecuentes"
        },
        {
            "file": "faq.qmd",
            "title": "Preguntas Frecuentes",
            "start_marker": "## ❓ Preguntas Frecuentes",
            "end_marker": "## 👤 Soporte y Contacto"
        }
    ]
    
    # Procesar cada capítulo
    for chapter in chapters:
        # Encontrar el contenido del capítulo
        start_idx = content.find(chapter["start_marker"])
        end_idx = content.find(chapter["end_marker"]) if chapter["end_marker"] else len(content)
        
        if start_idx == -1:
            print(f"⚠️  No se encontró: {chapter['title']}")
            continue
            
        chapter_content = content[start_idx:end_idx].strip()
        
        # Convertir ## a # (Quarto usa # para títulos de capítulo)
        chapter_content = re.sub(r'^## ', '# ', chapter_content, count=1, flags=re.MULTILINE)
        
        # Convertir rutas de imágenes
        chapter_content = re.sub(
            r'\!\[(.*?)\]\(assets/',
            r'![\1](../assets/',
            chapter_content
        )
        
        # Convertir bloques de código de ticks simples a callouts cuando sea apropiado
        # Detectar "Nota:" o "Consejo:" y convertir a callouts
        chapter_content = re.sub(
            r'^> \*\*(Nota|Consejo|Importante|Advertencia):\*\* (.*?)$',
            lambda m: f':::{{\\.callout-{"note" if m.group(1) == "Nota" else "tip" if m.group(1) == "Consejo" else "important" if m.group(1) == "Importante" else "warning"}}}\n## {m.group(1)}\n{m.group(2)}\n:::',
            chapter_content,
            flags=re.MULTILINE
        )
        
        # Escribir el archivo del capítulo
        chapter_path = Path(chapter["file"])
        chapter_path.write_text(chapter_content, encoding="utf-8")
        print(f"✅ Creado: {chapter['file']}")
    
    # Crear el capítulo de referencias
    references_content = """# Referencias {.unnumbered}

## Soporte y Contacto

Si necesitas ayuda adicional o tienes preguntas sobre el uso del bot:

**Luis Aguilera**  
Administrador del Sistema

- 📧 Email: [luis.aguilera@ssab.com](mailto:luis.aguilera@ssab.com)
- 📱 WhatsApp: [+56 9 7388 1390](https://wa.me/56973881390)
- 🏢 Empresa: SSAB Chile

## Enlaces Útiles

- [SSAB Global](https://www.ssab.com)
- [SSAB América Latina](https://www.ssab.com/es-cl)
- [Productos SSAB](https://www.ssab.com/es-cl/productos)

## Sobre SSAB

SSAB es un fabricante global líder de acero de alta resistencia, especializado en:

- Acero ultra-alta resistencia (UHSS)
- Acero resistente al desgaste (Hardox)
- Acero estructural (Strenx)
- Soluciones sostenibles de acero

## Historial de Versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 2.0 | Nov 2025 | Manual completo en formato Quarto |
| 1.0 | Nov 2025 | Primera versión del manual |

## Agradecimientos

Este manual fue desarrollado para facilitar el uso del Bot de Gestión Comercial SSAB Chile y mejorar la eficiencia del equipo comercial.

---

*Documento generado con [Quarto](https://quarto.org)*
"""
    
    Path("references.qmd").write_text(references_content, encoding="utf-8")
    print("✅ Creado: references.qmd")
    
    print("\n🎉 Conversión completada!")
    print("📝 Archivos creados en la carpeta quarto-book/")

if __name__ == "__main__":
    split_manual_into_chapters()
