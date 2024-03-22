## Características [idiosincrásicas](./vimscript)
    - Cuando Thompson visitó UC Berkeley en 1976, trajo consigo un compilador Pascal para UNIX roto 
    que necesitaba ser reparado. 
    - Bill Joy, un estudiante de UC Berkeley, fue el encargado de arreglar el sistema Pascal de Thompson
        - Con el paso de los días, Joy notó que Ed lo estaba frenando.
    - También es importante mencionar que Bill Joy utilizó una terminal ADM-3A para desarrollar vi.
    - Muchos atajos de vi y teclas de navegación que todavía utilizamos hoy 
    se basaron en la distribución del teclado ADM-3A.
        - Las teclas hjkl tenía flechas. 
        - Naturalmente reutilizó las mismas teclas para [navegar](./navigation) y el resto es historia.
        - La historia sigue: - [tiling_window_manager](../linux/tiling_window_manager)
    - También debemos señalar que Bill Joy estaba desarrollando su editor conectado 
    a un módem extremadamente lento de 300 baudios.

## vi
    - Pero se puedes pensar en vi como si lanzara varios editores que funcionan de diferentes modos.
    - El avance de vi fue adaptar el conjunto de comandos de ed a un formato de editor de pantalla:
        - En lugar de hacer cosas en papel en una máquina de escribir, 
        vi mantiene una vista actual de una parte de un documento en la pantalla,
        mientras que los comandos se escriben en la línea inferior.
        - Mantiene una ventana constantemente actualizada sobre una parte del texto que se está editando.

## The standard Unix editor ed was first written by Ken Thompson for the PDP-7
    - Probablemente deberíamos comenzar con ed ([apacionados](./culture))
    - que era un editor de línea de comandos creado por Ken Thompson 
    diseñado para funcionar bien con teleimpresores en lugar de terminales de visualización.
    - [Ken](../linux/history) adopted the notion of multiple buffers to edit 
    - several files simultaneously and move and copy text among them, 
    and also the idea of executing a given buffer 
    as editor commands, thus providing [programmability](./autocmd)

## grep es útil y fácil de usar:
    - Es la razón por la que grep se incluye en la mayoría de lenguajes de programación: 
        - Antes de que fuera nombrado, 
        grep era una utilidad privada escrita por [Ken](../r/grep) Thompson 
        para buscar archivos en busca de ciertos patrones

## vim and neovim
    - It’s been around since 1991 (Neovim since 2014) so it has its own way of doing things.



