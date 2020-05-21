---
layout: phenotype
title: Diabetes
name: Diabetes
phenotype_id: bYMFsBEu7tVB6YkrQ8aBvk 
type: Disease or Syndrome
group: Endocrine
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
{% include csv.html csvdata=site.data.primary_care.CPRD_diabetes %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.secondary_care.ICD_diabetes %}
### Implementation 
<pre>Use MODIFIED CALIBER 'Diabetes' phenotyping algorithm for 
1.	T1DM, 
2.	T2DM, 
3.	'Diabetes' other or uncertain type:

IF there is at least one record for code for type 2 'Diabetes' (diabdiag_gprd = 4)
    and no record for type 1 'Diabetes' (no record with diabdiag_gprd = 3)
    then classify the patient as type 2 'Diabetes'

ELSE if there is at least one record for code for type I 'Diabetes' (diabdiag_gprd = 3)
    and no record for type 2 'Diabetes' (no record with diabdiag_gprd = 4)
    then classify the patient as type 1 'Diabetes'

ELSE if there is at least one record of type 1 'Diabetes' (diabdiag_gprd = 3)
    and type 2 'Diabetes' (diabdiag_gprd = 4)
    then classify as 'Diabetes' other or uncertain type

ELSE if there are no diabdiag_gprd records for this patient:

    If there is at least one record for Non-insulin-dependent 'Diabetes' mellitus (NIDDM) (dm_gprd = 4 or dm_hes = 4)
        and no record for IDDM (no record with dm_gprd = 3 or dm_hes = 3)
        then classify the patient as type 2 'Diabetes'

    ELSE if there is at least one record for Insulin-dependent 'Diabetes' mellitus (IDDM) (dm_gprd = 3 or dm_hes = 3)
        and no record for NIDDM (no record with dm_gprd = 4 or dm_hes = 4)
        then classify the patient as type 1 'Diabetes'

    ELSE if there is at least one record of 'Diabetes' (dm_gprd or dm_hes category 3, 4, 5 or 6)
        then classify as 'Diabetes' other or uncertain type

ELSE classify as no 'Diabetes'</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>