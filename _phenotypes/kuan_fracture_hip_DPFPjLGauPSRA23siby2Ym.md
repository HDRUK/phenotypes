---
layout: phenotype
title: Fracture of hip
name: Fracture of hip
phenotype_id: DPFPjLGauPSRA23siby2Ym 
type: Disease or Syndrome
group: Musculoskeletal
data_sources: Primary care (Clinical Practice Research Datalink)<br>Hospitalizations (Hospital Episode Statistics) 
clinical_terminologies: ICD-10, OPCS-4, Read Version 2 
validation: cross-source
primary_care_code_lists: /primary_care/CPRD_acne.csv
secondary_care_code_lists: /secondary_care/ICD_acne.csv
valid_event_data_range: 01/01/1999 - 01/07/2016
sex: Female/Male
author: Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al.
status: FINAL
date: 2019-05-20
modified_date: 2019-05-20
version: 1
---
### Primary care 
{% include csv.html csvdata=site.data.primary_care.CPRD_fracture_hip %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.secondary_care.ICD_fracture_hip %}
#### Procedures 
{% include csv.html csvdata=site.data.secondary_care.OPCS_fracture_hip %}
### Implementation 
<pre>At the specified date, a patient is defined as having had Fracture of hip IF they meet the criteria for any of the following on or before the specified date. The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

Primary care
1. Fracture of hip diagnosis or history of diagnosis or procedure during a consultation 
OR
Secondary care (ICD10)
1. ALL diagnoses of Fracture of hip or history of diagnosis during a hospitalization
OR
Secondary care (OPCS4)
1. ALL procedures for Fracture of hip during a hospitalization</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>