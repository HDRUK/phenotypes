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

<hr class="hr mt-4">

<div class="row">
<div class="col-sm-99 text-style-center">
<div class="text-size-xlarge text-color-medium">What is a phenotyping algorithm?</div> 
    <div class="text-size-small text-color-rich">
When patients interact with physicians, or are admitted into hospital, information is collected electronically on their symptoms, diagnoses, laboratory test results, and prescriptions and stored in Electronic Health Records (EHR). EHR are a valuable resource for researchers and clinicians for improving health and healthcare. Phenotyping algorithms are complex computer programs that extract useful information from EHR so they can be used for health research.</div>
</div>

<div class="col-sm-99 text-style-center">
<div class="text-size-xlarge text-color-medium">What is the HDR UK Phenotype Portal?</div> 
    <div class="text-size-small text-color-rich">
The HDR UK Phenotype Portal is a a national platform for dissemination of citable algorithms (incl. validations) and tools which will reduce duplication of effort and improve research reproducibility. More information can be found on the <a href="https://www.hdruk.ac.uk/projects/national-phenomics-resource/">HDR website</a></div>
</div>
</div>

<hr class="hr mt-4">

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