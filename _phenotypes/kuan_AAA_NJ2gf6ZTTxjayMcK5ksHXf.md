---
layout: phenotype
title: Abdominal aortic aneurysm
name: Abdominal aortic aneurysm
phenotype_id: NJ2gf6ZTTxjayMcK5ksHXf 
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
{% include csv.html csvdata=site.data.primary_care.CPRD_AAA %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.secondary_care.ICD_AAA %}
### Implementation 
<pre>Use MODIFIED CALIBER 'Abdominal aortic aneurysm' phenotyping algorithm:

At the specified date, a patient is considered to have an 'Abdominal aortic aneurysm' IF they meet any of the criteria below on or before the specified date. 

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:
1.	Primary care 
    1.	Diagnosis of AAA during a consultation: arterial_gprd: category 4
    2.	Performance of emergency AAA repair procedure recording during a consultation: aaa_ops_gprd: category 3
    3.	History of AAA during a consultation. The following Read code from CPRD:
    1.	Read:14AE.00	Medcode:16993	Descr:H/O: aortic aneurysm
2.	Secondary care 
    1.	Diagnosis of AAA as the primary or secondary diagnosis of any hospitalization: arterial_hes: category 4
    2.	Performance of emergency AAA repair procedure recorded: aaa_ops_opcs: category 3</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>