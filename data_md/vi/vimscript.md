## Does Vimscript have an official name?:
    - The name VimL appeared in the documentation in July 2013
    - It's actually really tough to find its history!:
        - Per Wikipedia, "basic scripting" was [added](./vim_history) on Feb 19, 1998 
        so it's no older than that. 

## VimScript es realmente malo debido a una combinación de:
        - Características [idiosincrásicas](./herencia)
        - Falta de coherencia. 
    - Al ser un lenguaje que se ha implementado lentamente y con una aplicación muy limitada en mente, 
    carece de todas las buenas características de cualquier lenguaje de programación decente. 
    - Vimscript es un lenguaje de dominio específico para realizar cosas muy específicas de Vim, 
    como la configuración.
    - VimScript9 es una bonita curita, pero eso es todo:
        - https://vimhelp.org/usr_41.txt.html
    - Optar por un [lenguaje](../go/lua_history) más maduro y robusto 
    fue un gran paso por parte de la comunidad NeoVim:
        - Cuando intente programar lógica complicada, un lenguaje de programación normal 
        será una opción mucho mejor debido a:
            - La familiaridad
            - La sintaxis
            - Características generales
            - Bibliotecas generales.

## let vs set
    - :set is for setting options 
    - :let for assigning a value to a variable

## :echo command:
    - vim-airline shows this information
    - :echo &filetype
    - :echo &fileformat
        - Vim recognizes three file formats (unix, dos, mac) 
        that determine what line ending characters (line terminators) 
        are removed from each line when a file is read, 
        or are added to each line when a file is written.
        - when you try execute file.r in DOS fileformat:
            - /usr/bin/env: ‘Rscript\r’: No such file or directory
        - :set fileformat=unix    # to convert from Dos to Unix

## You can use the built-in :help to learn about a specific option:
    - Vim's online documentation is fantastic if you know how to navigate it.
    - :helpgrep pattern
    - Search all help text files and make a list of lines in which {pattern} matches:
        - Devuelve demasiadas cosas

## Don't use short names in .vimrc
    - Vim offers short names for most commands and options 
    to help with quickly inputting them within a running Vim instance
        - typing :set ts=8 noet is a lot faster than typing :set tabstop=8 noexpandtab.

## Use noremap in .vimrc
    - This helps guarantee that your maps actually do what you intend, 
    since allowing recursion means some other maps (maybe from plugins) can affect your maps' behavior.
    - :[nore]map covers normal mode, visual mode, select mode, and operator-pending mode

## Vim language
    - snippet hg "[firma](./snippets)" w
    - -- Horacio Galan <galanh@gmail.com>  `!v strftime('%d %b %Y')`
    - endsnippet
The backticked text use the interpolation feature of Ultisnips. 
!v means to use Vim language interpolation, and 
it should be followed by valid Vim [script](../latex/snippet) expressions, like the one given above

## How define a function

