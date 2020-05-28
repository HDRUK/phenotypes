---
layout: phenotype
title: Myocardial infarction
name: Myocardial infarction
phenotype_id: LG5FyDnaomHyfeNNKPx92J 
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
{% include csv.html csvdata=site.data.primary_care.CPRD_myocardial_infarction %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.secondary_care.ICD_myocardial_infarction %}
### Implementation 
<pre>Use MODIFIED CALIBER 'Myocardial infarction' phenotyping algorithm:

At the specified date, a patient is considered to have had a 'Myocardial infarction' IF they meet any of the criteria below on or before the specified date. 

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date. 
1.	Primary care diagnosis of MI: myo_infarct_gprd: category 1, category 2, category 3,  category 4, category 5, category 6, category 7
2.	Secondary care diagnosis of MI: myo_infarct_hes: category 1, category 5, category 6, category 7
3.	Secondary care procedure code for coronary thrombolysis: lysis_opcs category 2</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>