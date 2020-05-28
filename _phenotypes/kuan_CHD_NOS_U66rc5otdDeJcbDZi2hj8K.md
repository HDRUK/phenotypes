---
layout: phenotype
title: Coronary heart disease not otherwise specified
name: Coronary heart disease not otherwise specified
phenotype_id: U66rc5otdDeJcbDZi2hj8K 
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
{% include csv.html csvdata=site.data.primary_care.CPRD_CHD_NOS %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.secondary_care.ICD_CHD_NOS %}
### Implementation 
<pre>Use MODIFIED CALIBER 'Coronary heart disease not otherwise specified' phenotyping algorithm

At the specified date, a patient is considered to have had 'Coronary heart disease not otherwise specified' IF they meet any of the criteria below on or before the specified date. 

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date. 
1.	No previous records meeting the criteria for stable angina OR unstable angina OR myocardial infarction 
AND {
2.	Primary care:  chd_nos_gprd: category 1, 3
    a)	IF Read code in chd_nos_gprd list, THEN chd_nos_gprd= appropriate category
    b)	OR IF enttype = 16, chd_nos_gprd = 1
OR
3.	Secondary care: chd_nos_hes: category 3 }</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>