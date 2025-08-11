# Flujo principal

```mermaid
flowchart TD
    A[Inicio] --> B[Menú: Jugar / Salir]
    B -->|Jugar| C[Leer N (impar)]
    B -->|Salir| O[Fin]
    C --> D[for ronda en 1..N]
    D --> E[Leer elección usuario]
    E --> F[Elección PC]
    F --> G[Comparar elecciones]
    G --> H{Resultado}
    H -->|Usuario| I[+1 Usuario]
    H -->|PC| J[+1 PC]
    H -->|Empate| K[Empates]
    I --> L{¿Alcanzó mayoría?}
    J --> L
    K --> D
    L -->|Sí| M[Fin del match]
    L -->|No| D
    M --> N[Mostrar marcador final]
```





