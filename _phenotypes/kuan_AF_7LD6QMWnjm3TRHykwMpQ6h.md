---
layout: phenotype
title: Atrial fibrillation
name: Atrial fibrillation
phenotype_id: 7LD6QMWnjm3TRHykwMpQ6h 
type: Disease or Syndrome
group: Cardiovascular
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
{% include csv.html csvdata=site.data.primary_care.CPRD_AF %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.secondary_care.ICD_AF %}
### Implementation 
<pre>Use MODIFIED CALIBER 'Atrial fibrillation' phenotyping algorithm: 

At the specified date, a patient is considered to have had 'Atrial fibrillation' or flutter IF they meet any of the criteria below on or before the specified date. 

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:
1.	1.	Historical & Diagnosed: first recorded AF code indicates monitoring of an existing condition, or reference to a previous AF diagnosis, or a diagnosis code for AF; preference given to the earliest dated record rather than diagnosis source (i.e. no preference for primary versus secondary care).
    1.	af_gprd: category 1, 2, 3, 4, 5, 6, 7
    2.	af_hes: category 6</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>