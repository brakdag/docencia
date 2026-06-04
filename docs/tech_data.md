# Guías de Trabajos Prácticos (LaTeX)

Este repositorio contiene el código fuente de las guías de trabajos prácticos
desarrolladas íntegramente en **LaTeX**. El flujo de trabajo está optimizado
para su edición en **Linux Debian 13 (Trixie)** utilizando **Neovim** con la
suite **LazyVim** y el plugin **VimTeX**.

---

## 🛠 Entorno de Desarrollo Recomendado

Para asegurar una compilación fluida, se sugiere el siguiente
stack:

### 1. Sistema Operativo y Dependencias

- **Distribución TeX:** `texlive-full`
- **Utilidades:** `latexmk`, `biber` (para bibliografía), `zathura` (visor PDF ligero).

```bash
sudo apt update
sudo apt install texlive-full latexmk biber zathura neovim
```
