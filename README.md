## Pipeline Architecture & ELT Strategy

Note on Data Quality: You will notice that `NaN` values and intentional anomalies are preserved in the raw data output of this script. This is by design. 

Rather than pre-cleaning the data in Python (ETL), I am generating raw, imperfect data to simulate a real-world ELT (Extract, Load, Transform) workflow. The raw data will be loaded directly into **Snowflake**, where the actual cleaning, anomaly filtering, and transformations will be handled using SQL. This mirrors modern enterprise data architecture and provides a realistic environment to practice advanced warehouse transformations.