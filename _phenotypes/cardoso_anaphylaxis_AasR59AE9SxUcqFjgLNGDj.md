---
layout: phenotype
title: Anaphylaxis
name: Anaphylaxis
phenotype_id: AasR59AE9SxUcqFjgLNGDj 
type: Disease or Syndrome
group: Disease or Syndrome
data_sources: 
    - The Health Improvement Network (THIN)
    - Hospital Episode Statistics
clinical_terminologies: 
    - Read Version 2
    - ICD-10
validation: 
    - cross-source
codelists:    
    - cardoso_anaphylaxis_AasR59AE9SxUcqFjgLNGDj_Read2.csv
    - cardoso_anaphylaxis_AasR59AE9SxUcqFjgLNGDj_ICD10.csv
valid_event_data_range: 01/01/1901-31/12/2019
sex: 
    - Female
    - Male
author: 
    - Cardoso V.
    - Nirantharakumar K.
    - Gkoutos G
status: FINAL
date: 2020-06-03
modified_date: 2020-06-03
version: 1
---

### Primary care 
{% include csv.html csvdata=site.data.codelists.cardoso_anaphylaxis_AasR59AE9SxUcqFjgLNGDj_Read2 %}

### Secondary care 

#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.cardoso_anaphylaxis_AasR59AE9SxUcqFjgLNGDj_ICD10 %}