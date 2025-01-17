# Digest Transform 
The Digest  transforms serves as a simple exemplar to demonstrate the development
of an annotator transform.  

Please see the set of [transform project conventions](../../README.md#transform-project-conventions) for details on general project conventions, transform configuration, testing and IDE set up.

## Summary 
This transform will calculate the hash value for the content column in a parquet file

## Contributors

- Maroun Touma (touma@us.ibm.com)

## Configuration and command line Options

The set of dictionary keys holding [DigetTransform](dpk_digest/transform.py) 
configuration for values are as follows:

| Key name  | Default  | Description |
|------------|----------|--------------|
| _digest_algorithm_ | _sha256_ | specifies the algorithm to use for calculating the hash value. Can be any of sha256, sha512 or MD5 |

## Running

### Launched Command Line Options 
The following command line arguments are available in addition to 
the options provided by 
the [python launcher options](../../../data-processing-lib/doc/python-launcher-options.md).
| Parameter | Value | Description |
---|---|---|
| --digest_algorithm | DIGEST_ALGORITHM |   the algorithm to use for calculating the hash value.|

Example:
```
python -m dpk_digest.runtime --digest_algorithm sha256 --data_local_config "{ 'input_folder' : 'test-data/input', 'output_folder' : 'test-data/output'}"
```
### Code example
Here is a sample [notebook](digest.ipynb)

## Troubleshooting guide

### Transforming data using the transform image

Missing

# Language Identification Ray Transform 

Not Applicable

## Launched Command Line Options 

Not Applicable

### Transforming data using the transform image

Not Applicable

