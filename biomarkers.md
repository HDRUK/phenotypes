---
layout: page
title: Biomarkers
---

{% assign biomarker_phenotypes = site.phenotypes | where: "type", "Biomarker" %}
| Phenotype | Data Sources | Validation |
|-----------|--------------|------------|{% for phenotype in biomarker_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources }} | {{ phenotype.validation }} |{% endfor %}

