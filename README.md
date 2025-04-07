# Action-Based Novelty

We propose domain-independent heuristics that prioritize nodes based on the novelty of the actions that lead to them and the novelty of the actions they enable.

These heuristics implemented into NYX [(Piotrowski and Perez 2024)](https://arxiv.org/abs/2402.11901), a versatile, Python-based, domain-independent planner [(link to the original code)](https://gitlab.com/wmgp9/nyx).

We started to develop these domain-independent heuristics in order to solve Minecraft PDDL domain instances better. The code of the PDDL Problem Generator for Minecraft Domain is in that [link](https://github.com/SPL-BGU/PDDL-Minecraft).

## Planner execution
```Shell
python nyx.py ex/minecraft/advanced_minecraft_domain.pddl ex/minecraft/advanced_minecraft_problem.pddl -search:dfs -dl:20
```

Use flag ```-h``` for usage and planner option information.


## Custom heuristics and using the precondition tree option
To see our custom heuristics, please check the heuristic_function method inside [heuristic_functions.py](heuristic_functions.py), to use the diffrent heuristics, run the planner with the '-custom_h:...' flag with the corresponding heuristic index. 

```Shell
python nyx.py ex/minecraft/advanced_minecraft_domain.pddl ex/minecraft/advanced_minecraft_problem.pddl -search:gbfs -pt -custom_h:4 -dblh
```

Use flag ```-dblh``` to check heuristic once again when popping from the open list.
This option is crucial for novelty-based heuristics, which can change during the search and lead to outdated expansions.

Use flag ```-pt``` to use the precondition tree option.
This mechanism uses a precondition tree instead of an array to store preconditions, allowing an efficient and fast way to prune actions with falsified preconditions, thereby reducing the need for repeated linear checks of the preconditions.

## Dependencies
- numba

## Current limitations of the planner
- No support for object subtypes

## Current limitations of the heuristics
- Need more testing and referment in order to work on domains other than Minecraft

# Citations

If you find our work interesting or the repo useful, please consider citing [this paper](https://doi.org/10.1609/socs.v17i1.31571):
```
@inproceedings{benyamin2024crafting,
 title={Crafting a Pogo Stick in Minecraft with Heuristic Search},
 author={Benyamin, Yarin and Mordoch, Argaman and Shperberg, Shahaf and Piotrowski, Wiktor and Stern, Roni},
 booktitle={Proceedings of the International Symposium on Combinatorial Search},
 volume={17},
 pages={261--262},
 year={2024}
}
```
