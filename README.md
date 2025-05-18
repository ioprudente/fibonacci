#  Espiral Dourada — Visualização Didática

<p align="center">
  <img src="https://raw.githubusercontent.com/ioprudente/fibonacci/main/espiral-fibonacci.jpeg" alt="Espiral de Fibonacci com linha de sombra" width="600"/>
</p>

Uma visualização animada da **espiral dourada**, inspirada na sequência de Fibonacci. O projeto tem foco didático: exibe a fórmula em tempo real, mostra o crescimento iterativo da espiral e traz uma linha de sombra que acompanha sua trajetória, como um radar.

---

## 📜 Sobre Fibonacci

No século XIII, o matemático italiano **Leonardo Fibonacci** introduziu uma sequência numérica simples, mas poderosa:

    1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Cada número é a soma dos dois anteriores. Essa sequência aparece frequentemente:

- Na natureza 🌻
- Em conchas, flores, galáxias
- Na arte e arquitetura
- Em algoritmos de computação e otimização

A espiral de Fibonacci é uma aproximação visual da **espiral logarítmica**, descrita pela fórmula:

    r(θ) = a · e^(bθ)


Onde:

- `r`: raio
- `θ`: ângulo (em radianos)
- `a`: raio base
- `b = ln(φ) / (π / 2)`
- `φ ≈ 1.618`: o número áureo

---

## 🎨 Funcionalidades

- Espiral animada com trajetória pontilhada
- Linha de sombra estilo radar que acompanha o ponto atual
- Fórmula `r(θ) = a · e^(bθ)` exibida com os valores ao vivo
- Contador de iterações com destaque gráfico
- Interface responsiva (a janela pode ser redimensionada)
- Fundo matemático minimalista

---

## 🧰 Tecnologias usadas

- **Python 3**
- **Pygame**

---

## 🚀 Como executar

1. Instale o Python 3, se ainda não tiver.
2. Instale a biblioteca necessária:

```bash
pip install pygame

