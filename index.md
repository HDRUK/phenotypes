---
layout: home
title: Phenotypes
---

<!-- Count the total number of terms and the total number of phenotypes -->
{% assign cd = 0 %}
{% for clist in site.data.codelists %}
        {% assign row = clist[1] %}
        {% for r in row %}
            {% capture cd %}{{cd | plus: 1 }}{% endcapture %}
        {% endfor %}
{% endfor %}

{% assign size = site.phenotypes.size %}

## Welcome to the HDR UK CALIBER Phenotype Portal
A comprehensive, open-access resource providing the research community with information, tools and phenotyping algorithms for UK electronic health records:

<hr class="hr">

<div class="container">
    <div class="row mt-4">
            <div class="col-sm-1">
        </div>
            <div class="col-sm-2 text-style-center">
                <div class="text-size-xxlarge text-color-medium">
                            {{ size }}
                            </div>
                <div class="text-size-small text-color-rich">
                    phenotyping algorithms
                </div>
            </div>
            <div class="col-sm-2 text-style-center">
                <div class="text-size-xxlarge text-color-medium">
                            {{ cd }}
                            </div>
                <div class="text-size-small text-color-rich">
                    clinical terminology terms
                </div>
            </div>
            <div class="col-sm-2 text-style-center">
                <div class="text-size-xxlarge text-color-medium">
                            10+
                            </div>
                <div class="text-size-small text-color-rich">
                    data sources
                </div>
            </div>
            <div class="col-sm-2 text-style-center">
                <div class="text-size-xxlarge text-color-medium">
                            100+
                            </div>
                <div class="text-size-small text-color-rich">
                    research papers
                </div>
            </div>
    </div>
</div>

<hr class="hr">

The portal curates rule-based phenotyping algorithms using national structured UK EHR data sources: 
* __Primary care__: Clinical Practice Reseach Datalink GOLD and AURUM, The Health Improvement Network
* __Hospital diagnoses and procedures__: Hospital Episode Statistics
* __Mortality__: Office for National Statistics
* __Research studies__: UK Biobank

Phenoypes have been extensively validated by generating six layers of evidence: aetiological, prognostic, case-note review, genetic, cross-EHR and cross-country replication.

{::options parse_block_html="true" /}
<div>
## Disease or syndrome
{: .table-title }
{% assign disease_phenotypes = site.phenotypes | where: "type", "Disease or Syndrome" | sort: "name" %}

| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in disease_phenotypes %}
[{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources | join: ", "}} |{% endfor %}

[View all diseases and syndromes](/disease-or-syndrome){: .btn}
{: .btn-p}
</div>
{: .panel }


{::options parse_block_html="true" /}
<div>
## Biomarkers
{: .table-title }
{% assign biomarker_phenotypes = site.phenotypes | where: "type", "Biomarker" | sort: "name" %}
| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in biomarker_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources | join: ", "}} |{% endfor %}

[View all biomarkers](/biomarkers){: .btn}
{: .btn-p}
</div>
{: .panel }


{::options parse_block_html="true" /}
<div>
## Lifestyle Risk factors
{: .table-title }
{% assign lifestyle_phenotypes = site.phenotypes | where: "type", "Lifestyle Risk Factor" | sort: "name" %}
| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in lifestyle_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources | join: ", "}} |{% endfor %}

[View all lifestyle risk factors](/lifestyle-risk-factors){: .btn}
{: .btn-p}
</div>
{: .panel }