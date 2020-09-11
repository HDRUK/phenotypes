#!/usr/bin/env python
# usage: generate_indexes.py
__author__ = "Susheel Varma"
__copyright__ = "Copyright (c) 2019-2020 Susheel Varma All Rights Reserved."
__email__ = "susheel.varma@hdruk.ac.uk"
__license__ = "Apache 2"

import os
import csv
import json
import markdown
from slugify import slugify
from pprint import pprint


def write_csv(filename, data, fieldnames=None):
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def get_phenotype_files(dir):
    phenotype_files = []
    for file in os.listdir(dir):
        if file.endswith(".md"):
            phenotype_files.append(os.path.join(dir, file))
    return phenotype_files

def get_data_sources():
    import yaml
    with open("_data/data_sources.yml", 'r', encoding="utf-8") as yml_file:
        yaml_text = yml_file.read()
        return yaml.safe_load(yaml_text)

def get_phenotype(file):
    filename = os.path.basename(file)
    url = "https://portal.caliberresearch.org/phenotypes/" + slugify(os.path.splitext(filename)[0])
    with open(file, 'r', encoding="utf-8") as md_file:
        text = md_file.read()
        md = markdown.Markdown(extensions=['meta', 'toc'])
        html = md.convert(text)
        
        meta = md.Meta
        codelists = meta.get('codelists', [''])
        codelists = [c.replace('- ', '') for c in codelists[1:]]
        # data_sources = meta.get('data_sources', [])
        toc = ["Metadata"]
        toc.extend([t['name'] for t in md.toc_tokens])
        data_sources = []
        for ds in meta['data_sources']:
            if ds != '':
                if ds.startswith("- "):
                    data_sources.append(ds.split("- ")[1])
                else:
                    data_sources.append(ds)
    return {
        'name': meta['name'][0],
        'type': meta['type'][0],
        'id': meta['phenotype_id'][0],
        'data_sources': data_sources,
        'codelists': codelists,
        'filename': filename,
        'url': url,
        'toc': toc,
        'data_sources': data_sources
    }

def get_phenotypes(dir="_phenotypes"):
    phenotypes =[]
    DATA_SOURCES = get_data_sources()
    files = get_phenotype_files(dir)
    for file in files:
        pt = get_phenotype(file)
        resolved_data_sources = []
        for ds in pt['data_sources']:
            if ds in DATA_SOURCES.keys():
                resolved_data_sources.append(DATA_SOURCES[ds])
            else:
                resolved_data_sources.append(ds)
        pt.pop('data_sources')
        pt['data_sources'] = resolved_data_sources
        phenotypes.append(pt)
    return phenotypes

def export_phenotype2datasets(phenotypes, filename="_data/phenotype2datasets.json"):
    phenotype2datasets = {}
    for p in phenotypes:
        name = p['name']
        if name not in phenotype2datasets.keys():
            phenotype2datasets[name] = []
        for ds in p['data_sources']:
            if type(ds) is dict:
                phenotype2datasets[name].append(ds)
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(phenotype2datasets, indent=2))

def export_dataset2phenotypes(phenotypes, filename="_data/dataset2phenotypes.json"):
    dataset2phenotypes = {}
    for p in phenotypes:
        for ds in p['data_sources']:
            if type(ds) is dict:
                if ds['id'] not in dataset2phenotypes.keys():
                    dataset2phenotypes[ds['id']] = []
                dataset2phenotypes[ds['id']].append({
                    'name': p['name'],
                    'type': p['type'],
                    'id': p['id'],
                    'url': p['url']
                })
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(dataset2phenotypes, indent=2))

def export_graph(phenotypes, filename="_data/graph.json"):
    graph = {}
    for p in phenotypes:
        type = p['type']
        if type not in graph.keys():
            graph[type] = {
                'name': type,
                'children': []
            }
        p_graph = {
            'name': p['name'],
            'children': []
        }
        for ds in p['data_sources']:
            ds_children = []
            toc_length = len(p['toc'])
            for i, t in enumerate(p['toc']):
                ds_children.append({
                    'name': t,
                    'value': (toc_length - i) * 100
                })
            p_graph['children'].append({
                'name': ds,
                'children': ds_children
            })
        graph[type]['children'].append(p_graph)
    with open(filename, 'w') as graph_json:
        graph_json.write(json.dumps(graph, indent=2))
    return graph

def export_catalogue(phenotypes):
    DATA = []
    for p in phenotypes:
        data_sources = [ds['name'] for ds in p['data_sources'] if type(ds) is dict]
        row = {
            'phenotype': p['name'],
            'phenotype_id': p['id'],
            'primary_care': [],
            'secondary_care': [],
        }
        if len(data_sources):
            row['data_sources'] = "; ".join(data_sources)
        for c in p['codelists']:
            if "read" in c.lower():
                row['primary_care'].append(c)
            elif "icd" in c.lower():
                row['secondary_care'].append(c)
            elif "snomed" in c.lower():
                row['secondary_care'].append(c)
            elif "opcs" in c.lower():
                row['secondary_care'].append(c)
        if len(row['primary_care']): row['primary_care'] = "; ".join(row['primary_care'])
        if len(row['secondary_care']): row['secondary_care'] = "; ".join(row['secondary_care'])
        DATA.append(row)
    headers = ['phenotype', 'phenotype_id', 'data_sources', "primary_care", 'secondary_care']
    write_csv("_data/phenotypes.csv", DATA, fieldnames=headers)

def main():
    phenotypes = get_phenotypes()
    # pprint(phenotypes[0])
    export_catalogue(phenotypes)
    # export_graph(phenotypes)
    # export_phenotype2datasets(phenotypes)
    # export_dataset2phenotypes(phenotypes)

if __name__ == "__main__":
    main()
