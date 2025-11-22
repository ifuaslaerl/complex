# Complex

**Complex** é uma ferramenta Python para visualização de funções complexas. Ela gera:
- **Diagramas de Bode**: Resposta em frequência 2D (Magnitude e Fase).
- **Superfícies de Laplace**: Visualizações 3D da magnitude sobre o plano complexo, coloridas pela fase.

## Instalação

Requer Python 3.9+.

```bash
pip install .
```

## Criando Suas Próprias Funções

Para criar uma nova função, herde de `ComplexFunction` e implemente o método `f`. Note que `f` agora é um método de instância e deve aceitar `self`.

```python
import overrides
from complex_function import ComplexFunction

class MinhaFuncao(ComplexFunction):
    @overrides.overrides
    def f(self, s: complex) -> complex:
        # Exemplo: 1 / (s + 1)
        return 1 / (s + 1)

if __name__ == "__main__":
    # Instancia a função com resolução definida
    funcao = MinhaFuncao(resolution=1000, real_range=(-10, 10), imag_range=(-10, 10))
    
    # Gera os gráficos
    funcao.plot_bode()
    funcao.plot_laplace(mesh_resolution=60)
```

## Estrutura do Projeto

- `src/grafical/core.py`: Classe base `ComplexFunction` e lógica de plotagem.
