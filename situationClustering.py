import os
import sys
import json
from collections import OrderedDict

input_path = sys.argv[1] #'ll_nepal/'
doc_list = os.listdir(input_path)

clusters = []
process = {}
for doc_name in doc_list:
    if 'json' not in doc_name:
        continue
    cur_doc = json.loads(open(input_path + doc_name).read())
    id_ = cur_doc['id']
    if 'geoLocations' in cur_doc:
        cur_loc = cur_doc['geoLocations'][0]['geohash']
        if cur_loc not in process:
            process[cur_loc] = {}
        if 'topics' in cur_doc:
            cur_topics = cur_doc['topics']
            for topic in cur_topics:
                if topic not in process[cur_loc]:
                    process[cur_loc][topic] = []
                process[cur_loc][topic].append(cur_doc['id'])
        else:
            # if 'variousLocation' not in process:
            #     process['variousLocation'] = {}
            # if 'noTopicInfo' not in process['variousLocation']:
            #     process['variousLocation']['noTopicInfo'] = []
            # process['variousLocation']['noTopicInfo'].append(cur_doc['id'])
            if 'noTopicInfo' not in process[cur_loc]:
                process[cur_loc]['noTopicInfo'] = []
            process[cur_loc]['noTopicInfo'].append(cur_doc['id'])
    elif 'topics' in cur_doc:
        cur_loc = 'noLocationInfo'
        if cur_loc not in process:
            process[cur_loc] = {}
        cur_topics = cur_doc['topics']
        for topic in cur_topics:
            if topic not in process[cur_loc]:
                process[cur_loc][topic] = []
            process[cur_loc][topic].append(cur_doc['id'])
    else:
        if 'noLocationInfo' not in process:
            process['noLocationInfo'] = {}
        if 'noTopicInfo' not in process['noLocationInfo']:
            process['noLocationInfo']['noTopicInfo'] = []
        process['noLocationInfo']['noTopicInfo'].append(cur_doc['id'])
# print process
# with open('cluster_process.json', 'w') as f:
#     f.write(json.dumps(process))

for location in process:
    for topic in process[location]:
        temp = OrderedDict()
        temp['Symbol'] = {}
        temp['Symbol']['Location'] = location
        temp['Symbol']['Topic'] = topic
        temp['Documents'] = process[location][topic]
        clusters.append(temp)
print 'We got %d clusters in total!' % len(clusters)

output_path = sys.argv[2] # 'll_nepal_output/'
if not os.path.exists(output_path):
	os.makedirs(output_path)
for cluster in clusters:
    output_file = cluster['Symbol']['Location'] + '_' + cluster['Symbol']['Topic'] + '.json'
    with open(output_path + output_file, 'w') as f:
        f.write(json.dumps(cluster))
