---
layout: page
title: Phenotypes
permalink: /phenotypes/
---

## Chronological map of human health
We have produced the first chronological map of human health across 308 physical and mental health morbidities over time from birth to death.


- [Manuscript](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext) published in the Lancet Digital Health.

- [EHR phenotype definitions](https://caliberresearch.org/portal/phenotypes/chronological-map) for >300 mental/physical health conditions.

- EHR phenotype definitions in [machine-readable](https://github.com/spiros/chronological-map-phenotypes) format.

### Disease or syndrome
{% assign disease_phenotypes = site.phenotypes | where: "type", "Disease or Syndrome" | sort: "phenotype_id" %}

| ID | Phenotype | Data Sources | Validation |
|----|-----------|--------------|------------|{% for phenotype in disease_phenotypes %}
| [{{ phenotype.phenotype_id}}](/phenotypes/{{ phenotype.phenotype_id }}.json) | [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources }} | {{ phenotype.validation }} |{% endfor %}


### Biomarkers
{% assign biomarker_phenotypes = site.phenotypes | where: "type", "Biomarker" %}
| ID | Phenotype | Data Sources | Validation |
|----|-----------|--------------|------------|{% for phenotype in biomarker_phenotypes %}
| [{{ phenotype.phenotype_id}}]({{ phenotype.url }}) | [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources }} | {{ phenotype.validation }} |{% endfor %}


### Lifestyle Risk factors
{% assign lifestyle_phenotypes = site.phenotypes | where: "type", "Lifestyle Risk Factor" %}
| ID | Phenotype | Data Sources | Validation |
|----|-----------|--------------|------------|{% for phenotype in lifestyle_phenotypes %}
| [{{ phenotype.phenotype_id}}]({{ phenotype.url }}) | [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources }} | {{ phenotype.validation }} |{% endfor %}