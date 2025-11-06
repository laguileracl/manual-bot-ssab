# Manual de Usuario - Bot SSAB Chile

Este repositorio contiene la documentación completa del Bot de Gestión Comercial SSAB Chile.

## 📦 Contenido del Repositorio

```
manual-bot-ssab/
├── README.md                           # Este archivo
├── LICENSE                             # Licencia MIT
├── GUIA_USUARIO.md                     # Manual completo en Markdown
├── Manual_Usuario_SSAB_Final.html      # Versión HTML
├── Manual_Usuario_Bot_SSAB_v2.pptx     # Presentación PowerPoint
├── assets/                             # Capturas de pantalla
│   ├── 01-buscar-bot.png
│   ├── 02-inicio-bot.png
│   ├── 03-menu-principal.png
│   ├── 04-busqueda-nombre.png
│   ├── 04-menu-clientes.png
│   ├── 05-ficha-cliente.png
│   ├── 06-catalogo.png
│   ├── 07-ficha-tecnica-01.png
│   ├── 07-ficha-tecnica-02.png
│   ├── 08-menu-cxc.png
│   ├── 09-vencidas.png
│   └── 10-por-vencer.png
├── docs/                               # Documentación modular
│   ├── 01-introduccion.md
│   ├── 02-requisitos.md
│   ├── 03-inicio-acceso.md
│   ├── 04-gestion-clientes.md
│   ├── 05-fichas-tecnicas.md
│   ├── 06-cuentas-cobrar.md
│   ├── 07-casos-uso.md
│   └── 08-faq.md
└── .gitignore

```

## 🚀 Cómo Usar Este Repositorio

### Ver Online

Visita: [https://github.com/laguileracl/manual-bot-ssab](https://github.com/laguileracl/manual-bot-ssab)

### Clonar Localmente

```bash
git clone https://github.com/laguileracl/manual-bot-ssab.git
cd manual-bot-ssab
```

### Abrir el Manual

**Formato HTML (recomendado):**
```bash
open Manual_Usuario_SSAB_Final.html
```

**Formato Markdown:**
```bash
# En VS Code
code GUIA_USUARIO.md

# O cualquier editor Markdown
```

**Formato PowerPoint:**
```bash
open Manual_Usuario_Bot_SSAB_v2.pptx
```

## 📝 Generar PDF desde HTML

Puedes generar un PDF profesional desde el archivo HTML:

### Opción 1: Desde el Navegador (Chrome/Edge)

1. Abrir `Manual_Usuario_SSAB_Final.html` en Chrome
2. Presionar `Cmd + P` (Mac) o `Ctrl + P` (Windows)
3. Destino: **Guardar como PDF**
4. ✅ Activar **"Gráficos de fondo"**
5. Guardar

### Opción 2: Usando Pandoc

```bash
pandoc GUIA_USUARIO.md -o Manual_Usuario.pdf \
  --pdf-engine=xelatex \
  -V lang=es \
  --toc
```

## 🛠️ Personalización

### Actualizar Screenshots

Reemplaza las imágenes en `assets/` manteniendo los mismos nombres.

### Modificar Contenido

Edita `GUIA_USUARIO.md` y regenera los formatos:

```bash
# Regenerar HTML
pandoc GUIA_USUARIO.md -o Manual_Usuario_SSAB_Final.html \
  --standalone --toc --toc-depth=2 \
  -V lang=es \
  --css=style.css

# Regenerar PowerPoint (requiere Python)
python generate_ppt_from_template.py
```

## 🤝 Contribuir

Las contribuciones son bienvenidas:

1. Fork este repositorio
2. Crea una rama: `git checkout -b feature/mejora`
3. Commit: `git commit -m 'Agregar nueva sección'`
4. Push: `git push origin feature/mejora`
5. Abre un Pull Request

## 📞 Contacto

**Luis Aguilera**  
📧 luis.aguilera@ssab.com  
📱 [WhatsApp](https://wa.me/56973881390)

## ⭐ Dar Estrella

Si este manual te fue útil, considera darle una ⭐ en GitHub!

## 📄 Licencia

MIT License - ver [LICENSE](LICENSE) para más detalles.
