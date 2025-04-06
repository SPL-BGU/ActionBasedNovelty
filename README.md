# Action-Based Novelty

We propose domain-independent heuristics that prioritize nodes based on the novelty of the actions that lead to them and the novelty of the actions they enable.

We implemented our heuristics into NYX [(Piotrowski and Perez 2024)](https://arxiv.org/abs/2402.11901), a versatile, Python-based, domain-independent planner [(link to the origianl code)](https://gitlab.com/wmgp9/nyx).

## Planner execution
```Shell
python nyx.py ex/minecraft/advanced_minecraft_domain.pddl ex/minecraft/advanced_minecraft_problem.pddl -search:dfs -dl:20
```

use flag ```-h``` for usage and planner option information.

## Dependencies
- numba

## Current limitations of the planner
- No support for object subtypes
