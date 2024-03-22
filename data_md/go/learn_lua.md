## Strings in Lua can contain the following C-like escape sequences:
\a	bell
\b	back space
\f	form feed
\n	newline
\r	carriage return
\t	horizontal tab
\v	vertical tab
\\	backslash
\"	double quote
\'	single quote
\[	left square bracket
\]	right square bracket

    - Lua considers both zero and the empty string as true in conditional tests 

[[ [Double](./lua_neovim_function) brackets
       start and end
       multi-line strings.]]

-- Blocks are denoted with keywords like [do](./lua_neovim) / end:
while num < 50 do
  num = num + 1  -- No ++ or += type operators.
end

## [tablas](lua_estructuras):
a = {}
> a
table: 0x5fadd6271860
> for i=1,1000 do a[i] = i*2 end
> a[10]
20
> a["x"] = 10
> a["x"]
10
> a[10]
20
> a["y"]
nil

## require()
    - Lua ofrece una función de alto nivel para cargar módulos, llamada require()
    - Esta función intenta mantener al mínimo sus suposiciones sobre qué es un módulo:
        - Un módulo es simplemente cualquier fragmento de código que define algunos valores 
        como funciones o tablas que contienen funciones
        - Ejemplo: Dentro de una funcion usamos require() para llamar una funcion de un modulo
            - { "<leader>pf", function() require("telescope.builtin").find_files() end, "n" }
   ## Entender como funcionan los modulos y require():
    - Se supone que los módulos Lua funcionan colocando funciones en una tabla, que luego devuelven.
    - Esto permite que el código que recupera el módulo decida cómo se accederá 
    a las funciones de ese módulo:
        - local mod = {}                        -- crea la tabla
        - function mod.map_generate() ... end   -- introduce la funcion en la tabla
        - return mod                            -- devueve la tabla
        - Ahora puede hacer require de este modulo y usar la funcion:
            [[file:/home/gato/bin/modulo_crear.lua]]
            [[file:/home/gato/bin/scrip_require.lua]]
            > require("modulo_crear")
            true	./modulo_crear.lua
            > modulo_uno
            table: 0x58801fbf4df0
            > modulo_uno.hola()
            Hola como les va ?

## package.path
    /usr/local/share/lua/5.4/?.lua
    /usr/local/share/lua/5.4/?/init.lua
    /usr/local/lib/lua/5.4/?.lua
    /usr/local/lib/lua/5.4/?/init.lua
    /usr/share/lua/5.4/?.lua
    /usr/share/lua/5.4/?/init.lua
    ./?.lua
    ./?/init.lua



