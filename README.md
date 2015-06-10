# CDC Births Data

This data is drawn from the [USA Centers for Disease Control and Prevention](http://www.cdc.gov/nchs/data_access/Vitalstatsonline.htm), and was compiled via Google's [BigQuery Web UI](https://cloud.google.com/bigquery/bigquery-web-ui) using the following query:

    SELECT
      year, month, day,
      IF (is_male, 'M', 'F') AS gender,
      SUM(record_weight) as births,
      SUM(mother_age * record_weight) / SUM(record_weight) as mother_age,
      SUM(father_age * record_weight) / SUM(record_weight) as father_age
    FROM
      [publicdata:samples.natality]
    GROUP BY
      year, month, day, gender
    ORDER BY
      year, month, day, gender

It is aggregated so as to comply with their terms of use.
Data was accessed June 9th, 2015.