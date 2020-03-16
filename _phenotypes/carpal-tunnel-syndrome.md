---
layout: phenotype
title: PHE00044 - Carpal Tunnel Syndrome
phenotype_id: PHE00044
name: Carpal Tunnel Syndrome
type: Disease or Syndrome
group: Musculoskeletal 
data_sources: Primary care (CPRD), Hospital Admission Data (HES), Mortality Data (ONS)
clinical_terminologies: Read, ICD-10, ICD-9, OPCS-4
validation: cross-source, casenote, aetiology, prognosis, genetic external
primary_care_code_lists: /primary_care/CPRD_carpal_tunnel.csv
secondary_care_code_lists: /secondary_care/ICD_carpal_tunnel.csv, /secondary_care/OPCS_carpal_tunnel.csv
valid_event_data_range: 01/01/1999 - 01/07/2016
sex: Female/Male
author: Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas
status: DRAFT
date: 2012-11-23
modified_date: 2012-11-23
version: Revision 2
---

### Primary Care

In the Clinical Practice Research Datalink (CPRD, primary care data) we ascertained {{ page.name }} cases by searching for Read terms related to an {{ page.name }} diagnosis or evidence of endovascular/transluminal procedures related to the emergency repair of an aneurysmal segment of the aorta.

{% include csv.html csvdata=site.data.primary_care.CPRD_carpal_tunnel %}

Read terms are hierarhically organized in top-level chapters i.e. chapter G....00 is related to Circulatory System Diseases and sub-headings i.e. heading G2...00 is related to Hypertensive Heart Disease while G3...00 is related to Ischaemic Heart Disease.

### Secondary Care

In Hospital Episode Statistics (HES, hospital admission data) we used ICD-10 terms (see below) for {{ page.name }} diagnosis when marked as the primary diagnosis i.e. the main condition treated or investigated during the relevant episode of healthcare. We used the date of admission to hospital as the date of the event. We additionally searched for OPCS-4 terms indicating the emergency repair of an aneurysmal segment of the aorta.

{% include csv.html csvdata=site.data.secondary_care.ICD_carpal_tunnel %}

{% include csv.html csvdata=site.data.secondary_care.OPCS_carpal_tunnel %}


### Death

### Implementation

**Combining evidence across sources to define and date phenotypes**

<pre>
At the specified date, a patient is defined as having had 'Carpal tunnel syndrome' IF they meet the criteria for any of the following on or before the specified date. The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

Primary care
1. 'Carpal tunnel syndrome' diagnosis, history of diagnosis or procedure during a consultation 
OR
Secondary care (ICD10)
1. ALL diagnoses of 'Carpal tunnel syndrome' or history of diagnosis during a hospitalization
OR
Secondary care (OPCS4)
1. ALL procedures for 'Carpal tunnel syndrome' or history of diagnosis during a hospitalization
</pre>

### Validations

### Publications

