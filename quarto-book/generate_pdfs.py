#!/usr/bin/env python3
"""
Genera PDFs individuales para cada capítulo del libro Quarto
"""
import subprocess
import sys
from pathlib import Path

def generate_chapter_pdfs():
    """Genera un PDF para cada capítulo"""
    
    # Lista de capítulos
    chapters = [
        {"file": "index.qmd", "title": "Bienvenida"},
        {"file": "intro.qmd", "title": "01-Introduccion"},
        {"file": "requisitos.qmd", "title": "02-Requisitos"},
        {"file": "inicio.qmd", "title": "03-Inicio-Acceso"},
        {"file": "clientes.qmd", "title": "04-Gestion-Clientes"},
        {"file": "fichas.qmd", "title": "05-Fichas-Tecnicas"},
        {"file": "cuentas.qmd", "title": "06-Cuentas-por-Cobrar"},
        {"file": "info-ssab.qmd", "title": "07-Informacion-SSAB"},
        {"file": "casos-uso.qmd", "title": "08-Casos-de-Uso"},
        {"file": "faq.qmd", "title": "09-Preguntas-Frecuentes"},
        {"file": "references.qmd", "title": "10-Referencias"},
    ]
    
    # Crear directorio para PDFs
    pdf_dir = Path("_book/pdfs")
    pdf_dir.mkdir(parents=True, exist_ok=True)
    
    print("📄 Generando PDFs individuales por capítulo...")
    print("=" * 60)
    
    success_count = 0
    failed_chapters = []
    
    for chapter in chapters:
        chapter_file = Path(chapter["file"])
        
        if not chapter_file.exists():
            print(f"⚠️  Saltando {chapter['title']}: archivo no encontrado")
            failed_chapters.append(chapter["title"])
            continue
        
        pdf_name = f"{chapter['title']}.pdf"
        pdf_path = pdf_dir / pdf_name
        
        print(f"\n📝 Procesando: {chapter['title']}")
        print(f"   Archivo: {chapter_file}")
        print(f"   PDF: {pdf_path}")
        
        try:
            # Comando quarto render para generar PDF individual
            cmd = [
                "quarto",
                "render",
                str(chapter_file),
                "--to", "pdf",
                "--output", str(pdf_path),
                "--metadata", "title=Manual Bot SSAB Chile",
                "--metadata", f"subtitle={chapter['title'].replace('-', ' ')}",
                "--metadata", "author=Luis Aguilera A.",
                "--metadata", "date=2025-11-06",
                "--quiet"
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0 and pdf_path.exists():
                size_kb = pdf_path.stat().st_size / 1024
                print(f"   ✅ Generado exitosamente ({size_kb:.1f} KB)")
                success_count += 1
            else:
                print(f"   ❌ Error al generar PDF")
                if result.stderr:
                    print(f"   Error: {result.stderr[:200]}")
                failed_chapters.append(chapter["title"])
                
        except Exception as e:
            print(f"   ❌ Excepción: {str(e)}")
            failed_chapters.append(chapter["title"])
    
    # Resumen
    print("\n" + "=" * 60)
    print(f"\n📊 Resumen de Generación:")
    print(f"   ✅ Exitosos: {success_count}/{len(chapters)}")
    print(f"   ❌ Fallidos: {len(failed_chapters)}/{len(chapters)}")
    
    if failed_chapters:
        print(f"\n⚠️  Capítulos con errores:")
        for title in failed_chapters:
            print(f"   - {title}")
    
    print(f"\n📁 PDFs guardados en: {pdf_dir.absolute()}")
    print("\n🎉 Proceso completado!")
    
    return success_count, len(failed_chapters)

if __name__ == "__main__":
    try:
        success, failed = generate_chapter_pdfs()
        sys.exit(0 if failed == 0 else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Proceso interrumpido por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        sys.exit(1)
