---
layout: phenotype
title: Endometrial hyperplasia and hypertrophy
name: Endometrial hyperplasia and hypertrophy
phenotype_id: X877B8Y2f3gJMtXhYe5q4j 
type: Disease or Syndrome
group: Genitourinary
data_sources: Primary care (Clinical Practice Research Datalink)<br>Hospitalizations (Hospital Episode Statistics) 
clinical_terminologies: ICD-10, Read Version 2 
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
{% include csv.html csvdata=site.data.primary_care.CPRD_endometrial_hyper %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.secondary_care.ICD_endometrial_hyper %}
### Implementation 
<pre>At the specified date, a patient is defined as having had 'Endometrial hyperplasia and hypertrophy' and hypertrophy IF they meet the criteria for any of the following on or before the specified date. The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

Primary care
1. 'Endometrial hyperplasia and hypertrophy' and hypertrophy diagnosis or history of diagnosis during a consultation 
OR
Secondary care
1. ALL diagnoses of 'Endometrial hyperplasia and hypertrophy' and hypertrophy or history of diagnosis during a hospitalization</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>