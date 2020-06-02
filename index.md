---
layout: home
title: Phenotypes
---

<!-- https://stackoverflow.com/questions/48529507/jekyll-show-post-count-for-sub-categories -->
{% assign size = site.phenotypes.size %}

## Welcome to the HDR UK CALIBER Phenotype Portal
A comprehensive, open-access resource providing the research community with information, tools and phenotyping algorithms for UK electronic health records data such as

The portal contains <big>{{ size }}</big> rule-based phenotyping algorithms based on national structured UK EHR data sources: 
* __primary care__: Clinical Practice Reseach Datalink GOLD and AURUM 
* __hospitalizations__: Hospital Episode Statistics
* __mortality__: Office for National Statistics
* __research__ cohorts: UK Biobank

Phenoypes have been extensively validated by generating six layers of evidence: aetiological, prognostic, case-note review, genetic, cross-EHR and cross-country replication.



{::options parse_block_html="true" /}
<div>
## Disease or syndrome
{: .table-title }
{% assign disease_phenotypes = site.phenotypes | where: "type", "Disease or Syndrome" | sort: "phenotype_id" %}

| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in disease_phenotypes %}
[{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources }} |{% endfor %}

[View all diseases and syndromes](/disease-or-syndrome){: .btn}
{: .btn-p}
</div>
{: .panel }


{::options parse_block_html="true" /}
<div>
## Biomarkers
{: .table-title }
{% assign biomarker_phenotypes = site.phenotypes | where: "type", "Biomarker" %}
| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in biomarker_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources }} |{% endfor %}

[View all biomarkers](/biomarkers){: .btn}
{: .btn-p}
</div>
{: .panel }


{::options parse_block_html="true" /}
<div>
## Lifestyle Risk factors
{: .table-title }
{% assign lifestyle_phenotypes = site.phenotypes | where: "type", "Lifestyle Risk Factor" %}
| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in lifestyle_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources }} |{% endfor %}

[View all lifestyle risk factors](/lifestyle-risk-factors){: .btn}
{: .btn-p}
</div>
{: .panel }