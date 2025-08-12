# Flujo principal

```mermaid
flowchart TD
    A[Inicio] --> B[Menu: Jugar/Salir];
    B -->|Jugar| C[Leer N (impar)];
    B -->|Salir| Z[Fin];
    C --> D[for ronda en 1..N];
    D --> E[Leer eleccion usuario];
    E --> F[Eleccion PC];
    F --> G[Comparar elecciones];
    G --> H{Resultado};
    H -->|Usuario| IU[+1 Usuario];
    H -->|PC| IP[+1 PC];
    H -->|Empate| IE[Empates];
    IU --> L{Alcanzo mayoria?};
    IP --> L;
    IE --> D;
    L -->|Si| M[Fin del match];
    L -->|No| D;
    M --> N[Mostrar marcador final];
```