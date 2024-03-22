## As Lua was intended to be a general embeddable extension language:
    - the designers of Lua focused on improving its speed, portability, extensibility 
    and ease-of-use in development 
    
## Brasil:
    - From 1977 until 1992, Brazil had a policy of strong trade barriers 
    - (called a market reserve) for computer hardware and software, 
    believing that Brazil could and should produce its own hardware and software. 
    
## VimScript VS Lua:
    ## VimScript realmente no es un lenguaje tan malo 
    y creo que sus deficiencias han sido muy exageradas, 
    y Vim9Script solucionó la mayoría de las rarezas que había allí.
    - Lua, por otro lado, no me dará un error si escribo mal el nombre de una variable, 
    y el ecosistema realmente no tiene buenas herramientas de análisis estático 
    para detectar este tipo de errores tontos.
    - La historia del versionado y la compatibilidad también es molesta 
    (es básicamente una historia de Python 2/3 con cada versión de Lua).
    - No es que Lua sea horrible, pero la adulación por parte de algunas personas de Neovim 
    es algo que siempre me pareció curioso, como si fuera un lenguaje fantástico y brillante.
    - No es que VimScript sea perfecto de ninguna manera, 
    pero en general creo que es un DSL bastante decente para un editor.
    ## Durante mucho tiempo sin avance en vim:
    - Me quedé con mi .vimrc de una década de antigüedad
    - NeoVim apenas estaba comenzando a lanzar su integración LSP nativa
    - Por capricho, decidí intentarlo. Terminé quedándome con eso. 
    - Ahora tendría que haber una gran razón para regresar. Nunca disfruté de [Vimscript](../vi/vimscript)
    - Siento que el ecosistema de NeoVim está traspasando los límites mucho más que Vim 
    - ¿ Quieren seguir siendo el editor de texto conservador y lento ?
    - Creo que Bram aprendió de la bifurcación neovim:
        - Neovim reforzó el soporte lua al reducir la impedancia entre el lenguaje lua y el host vim
        - Mucha gente disfruta escribiendo lua más que vimscript, 
        pero el valor agregado no ha resultado lo suficientemente convincente 
        para las personas a las que no les importaba vimscript. 
        - El repositorio oficial de neovim todavía tiene el doble de código vimscript que código lua.
    
    
