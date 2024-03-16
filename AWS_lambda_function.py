"""
aws Lambda Function to process JSON data stored in an S3 bucket,
transform it into a Pandas DataFrame, normalize the DataFrame, and write
the resulting DataFrame to a Parquet file stored in another S3 bucket,
optionally registering it as a table in AWS Glue catalog.
"""

import urllib.parse
import os

import awswrangler as wr
import pandas as pd

os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']


def lambda_handler(event, context):
    """
    Lambda function to process JSON data stored in an S3 bucket, transform it into a Pandas DataFrame,
    normalize the DataFrame, and write the resulting DataFrame to a Parquet file stored in another S3 bucket,
    optionally registering it as a table in AWS Glue catalog.

    Parameters:
    - event (dict): A dictionary containing information about the S3 event that triggered the Lambda function.
                    Typically includes details about the S3 bucket and object.
    - context (LambdaContext): An object providing runtime information about the Lambda function invocation.

    Returns:
    - dict: A dictionary containing the response from the AWS Data Wrangler write operation.

    Raises:
    - Exception: If there is an error processing the S3 object or writing to S3.
                 This exception is raised to trigger AWS Lambda's error handling.

    Notes:
    - This Lambda function expects JSON data stored in the specified S3 bucket, reads it into a Pandas DataFrame,
      extracts required columns, and writes the resulting DataFrame to another S3 bucket in Parquet format.
    - It optionally registers the Parquet file as a table in the specified AWS Glue catalog database.
    - Make sure that the required environment variables (s3_cleansed_layer, glue_catalog_db_name,
      glue_catalog_table_name, write_data_operation) are properly set before invoking this Lambda function.
    """
    # Get the object from the event & show its content type -->
    # getting the bucket name & key path to the object
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:

        # Creating DF from the content
        df_raw = wr.s3.read_json('s3://{}/{}'.format(bucket, key))

        # Extract the required column of items:
        df_step_1 = pd.json_normalize(df_raw['items'])

        # Write to S3
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name,
            mode=os_input_write_data_operation
        )

        return wr_response

    except Exception as e:
        print(e)
        print('Error getting object {} from the bucket {}. Make sure they exist & your bucket is in the same region as this function.'.format(key, bucket))
        raise e
