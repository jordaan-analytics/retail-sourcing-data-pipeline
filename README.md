## Pipeline Architecture & ELT Strategy

Note on Data Quality: You will notice that `NaN` values and intentional anomalies are preserved in the raw data output of this script. This is by design. 

Rather than pre-cleaning the data in Python (ETL), I am generating raw, imperfect data to simulate a real-world ELT (Extract, Load, Transform) workflow. The raw data will be loaded directly into **Snowflake**, where the actual cleaning, anomaly filtering, and transformations will be handled using SQL. This mirrors modern enterprise data architecture and provides a realistic environment to practice advanced warehouse transformations.

## Future State: ELT Pipeline Architecture & Cloud Migration

To evolve this project from a local Python data-generation script into an enterprise-grade analytics pipeline, the next phase involves transitioning to an ELT (Extract, Load, Transform) framework:

1. **Data Staging (Snowflake Cloud Data Warehouse):** - The mock pipeline datasets (`raw_sap_purchase_orders`, `raw_retaillink_asns`, and `raw_warehouse_receipts`) will be loaded as raw tables into a structured Snowflake environment.
2. **Transformation & Semantic Layer (dbt Core):**
   - Utilizing SQL within dbt to handle heavy transformations, join disparate vendor datasets, build automated data quality tests, and construct the final compliance analytics models.

*Currently executing a dedicated sprint to master advanced SQL optimization techniques to prepare for building the Snowflake transformation layer.*