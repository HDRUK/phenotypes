---
layout: phenotype
title: End stage renal disease
name: End stage renal disease
phenotype_id: 656RD4TRGA4B7GHmaJzAzt 
type: Disease or Syndrome
group: Genitourinary
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
{% include csv.html csvdata=site.data.primary_care.CPRD_ESRD %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.secondary_care.ICD_ESRD %}
#### Procedures 
{% include csv.html csvdata=site.data.secondary_care.OPCS_ESRD %}
### Implementation 
<pre>At the specified date, a patient is defined as having had 'End stage renal disease' IF they meet the criteria for any of the following on or before the specified date. The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

Primary care
1. 'End stage renal disease' diagnosis or history of diagnosis or procedure during a consultation 
OR
2. Meets the following criteria (definitions as for CKD):
IF egfr_ckdepi recorded on or before specified date, THEN 
IF egfr_ckdepi <15 ml/min on the most recent date (index date) before the specified date
AND
IF egfr_ckdepi <15 ml/min on any date greater than 90 days BEFORE the index date above
THEN classify as having ESRD
Secondary care
1. ALL diagnoses of 'End stage renal disease' or history of diagnosis or procedure during a hospitalization
Secondary care (OPCS4)
1. ALL procedures for 'End stage renal disease' during a hospitalization</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>