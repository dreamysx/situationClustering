# Situation Clustering
Situation clustering aims at clustering documents based on real world information it contains.
This first version is developed for dataset **ll_Nepal** only. Clustering is based on location and topic information document has.

### Explain ll_Nepal
* All input documents are in **json** format.
* **Topic information** comes from field `topics` of sample data, 9498 out of 29946 documents have this field, totally 11 kinds of topics.
* **Location information** comes from field `geoLocations`/`geohash`, 24834 out of 29946 documents have this field, totally 346 kinds of locations. Sample data also have a field `LOC`, basically each `LOC` value is corresponding to a `geohash` value. But, only 5384 out of 29946 documents have `LOC`. So, we choose `geohash` over `LOC` to represent location information.
* Documents which have exactly same location and have at least one common topic are seen to belong to same cluster.

### Usage
Git clone package with the following command:
```
$ git clone https://github.com/dreamysx/situationClustering.git
```
Execute the following command to run the code:
```
python [code-file-name] [input-path] [output-path]
```
For example:
```
$ python situationClustering.py sampleInput/ sampleOutput/
```