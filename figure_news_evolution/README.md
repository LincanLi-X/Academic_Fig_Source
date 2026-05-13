# Recreated experimental figures for EMNLP2025 Multi-Agent News Evolution

> The Stepwise Deception: Simulating the Evolution from True News to Fake News with LLM Agents

This folder contains one Python script per experimental-result figure from the paper body/appendix figures used in the experimental analysis.
The scripts use a small pure-Python SVG helper so they can run without third-party dependencies.

## Files included in git

- `svg_utils.py`: shared pure-Python SVG drawing helpers.
- `plot_fig3_fuse_eval.py`: recreates Figure 3.
- `plot_fig4_ablation_intervention.py`: recreates Figure 4.
- `plot_fig5_factor_contribution.py`: recreates Figure 5.
- `plot_fig6_simulation_scenarios.py`: recreates Figure 6.
- `plot_fig8_backbone.py`: recreates Figure 8.
- `figures/*.svg`: generated, text-based SVG outputs.
- `requirements.txt`: documents that no third-party dependencies are needed.
- `package_artifacts.py`: recreates the local zip archive.

## Install requirements

No external packages are required. The scripts use only the Python standard library.
For completeness, you can inspect the requirements file:

```bash
cat figure_news_evolution/requirements.txt
```

## Regenerate all figures

Run all scripts from the repository root:

```bash
python figure_news_evolution/plot_fig3_fuse_eval.py
python figure_news_evolution/plot_fig4_ablation_intervention.py
python figure_news_evolution/plot_fig5_factor_contribution.py
python figure_news_evolution/plot_fig6_simulation_scenarios.py
python figure_news_evolution/plot_fig8_backbone.py
```

Outputs are written to `figure_news_evolution/figures/*.svg`.

## Package the local zip artifact

The binary zip file is intentionally **not committed** because Codex/GitHub PR creation does not support binary files in the diff.
To create the same archive locally at the repository root, run:

```bash
python figure_news_evolution/package_artifacts.py
```

This creates:

```text
figure_news_evolution_artifacts.zip
```

You can verify the archive with:

```bash
python -m zipfile -t figure_news_evolution_artifacts.zip
python -m zipfile -l figure_news_evolution_artifacts.zip
```
