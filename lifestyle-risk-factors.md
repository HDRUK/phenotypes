---
layout: page
title: Lifestype Risk Factors
---

{% assign lifestyle_phenotypes = site.phenotypes | where: "type", "Lifestyle Risk Factor" %}
| ID | Phenotype | Data Sources | Validation |
|----|-----------|--------------|------------|{% for phenotype in lifestyle_phenotypes %}
| [{{ phenotype.phenotype_id}}]({{ phenotype.url }}) | [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources }} | {{ phenotype.validation }} |{% endfor %}
