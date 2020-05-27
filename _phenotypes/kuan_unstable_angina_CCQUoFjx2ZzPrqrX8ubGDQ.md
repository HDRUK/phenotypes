---
layout: phenotype
title: Unstable Angina
name: Unstable Angina
phenotype_id: CCQUoFjx2ZzPrqrX8ubGDQ 
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
{% include csv.html csvdata=site.data.primary_care.CPRD_unstable_angina %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.secondary_care.ICD_unstable_angina %}
### Implementation 
<pre>Use MODIFIED CALIBER 'Unstable Angina' phenotyping algorithm:

At the specified date, a patient is considered to have had 'Unstable Angina' IF they meet the criteria for any of the following on or before the specified date: 
A hospitalization with the non-specific diagnosis of 'angina' as the primary diagnosis, where there is no procedure giving a reason for admission (PCI or CABG), is considered to be 'Unstable Angina'.

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:
1.	Primary care
    a)	Diagnosis of 'Unstable Angina'; unangina_gprd,  category 2, 3
    b)	Diagnosis of acute coronary syndrome not otherwise specified; acs_gprd, category 3
2.	Secondary care
    a)	Primary or secondary diagnosis of unspecified angina (ICD-10 I20.9) during a hospitalization that did not have a PCI or CABG procedure performed
    b)	Primary or secondary diagnosis of acute ischaemic heart disease during a hospitalization; acute_ihd_hes, category 3
    c)	Primary or secondary diagnosis of 'Unstable Angina' during a hospitalization; uangina_hes, category 1</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>