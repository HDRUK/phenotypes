---
layout: phenotype
title: Other nervous system infections
name: Other nervous system infections
phenotype_id: g68fb5w3rkcPXQTCt6V35E 
type: Disease or Syndrome
group: Infections
data_sources: Hospitalizations (Hospital Episode Statistics) 
clinical_terminologies: ICD-10 
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
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.secondary_care.ICD_oth_nerv_sys %}
### Implementation 
<pre>At the specified date, a patient is defined as having had Other nervous system infections IF they meet the criteria for any of the following on or before the specified date. The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

Secondary care
1. ALL diagnoses of Other nervous system infections or history of diagnosis during a hospitalization
OR
2. ALL possible diagnosis of Other nervous system infections during a hospitalization IF NO record satisfying criteria for Meningitis or Encephalitis 30 days before or 30 days after the first event date for Other nervous system infections.</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>