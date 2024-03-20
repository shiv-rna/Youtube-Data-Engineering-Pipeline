# Youtube-Data-Engineering-Pipeline 📺
## 📝 Overview
Embark on a transformative journey with the YouTube Data Engineering Pipeline repository! This project offers a robust solution meticulously crafted to efficiently manage, process, and analyze YouTube video data leveraging the power of AWS services. Whether you're diving into structured statistics or exploring the nuances of trending key metrics, this pipeline is engineered to handle it all with finesse.
## 🎯 Pipeline Goals
- **Data Ingestion**: Forge a resilient data ingestion mechanism capable of harmonizing data from disparate sources, prioritizing reliability.
- **ETL Excellence**: Engineer an Extract, Transform, Load (ETL) system to streamline the transformation of raw data into a standardized format.
- **Data Lake Mastery**: Establish a centralized data repository leveraging Amazon S3, ensuring optimal efficiency in housing diverse datasets.
- **Scalability**: Architect the system to seamlessly scale alongside burgeoning data volumes, guaranteeing uninterrupted performance.
- **Cloud Empowerment**: Harness the prowess of AWS cloud infrastructure to efficiently process and analyze extensive datasets.
- **Insightful Reporting**: Craft interactive dashboards in Amazon QuickSight, for visualization & analysis to drive informed decision-making.

## 💼 Services Utilized
1. **Amazon S3 (Simple Storage Service)**:
   - Serves as the primary data lake solution, offering highly scalable, durable, and secure object storage.
   - Leverages S3's RESTful API for seamless storing and retrieval of structured and unstructured data.
   - Multi-region replication and versioning capabilities ensure data durability and availability.
   - Features like lifecycle policies enable cost-effective data management strategies.

2. **AWS IAM (Identity and Access Management)**:
   - Provides robust identity and access management controls to safeguard resources.
   - Enforces least privilege access through fine-grained policies and roles.
   - Role-based access control (RBAC) and temporary security credentials enable secure delegation of permissions.
   - IAM policies facilitate granular control over API actions, enhancing the overall security posture.

3. **Amazon QuickSight**:
   - Serves as the cloud-native business intelligence tool, enabling interactive exploration and visualization of data.
   - Leverages QuickSight's in-memory engine and SPICE architecture for near-real-time analytics at scale.
   - Integration with AWS data sources like Amazon S3 and Athena allows seamless data ingestion and analysis.
   - Extensible API facilitates custom dashboarding and reporting solutions.

4. **AWS Glue**:
   - Acts as the fully managed ETL (Extract, Transform, Load) service, automating the process of data discovery, transformation, and integration.
   - Dynamic data catalog and schema inference capabilities streamline the identification and classification of data.
   - Serverless architecture scales automatically to handle varying workloads.
   - Integration with services like Amazon S3 and Athena ensures seamless data movement and querying across the analytics pipeline.

5. **AWS Lambda**:
   - Powers the serverless computing infrastructure, enabling event-driven data processing and analysis.
   - Executes code in response to triggers such as data ingestion events or scheduled tasks.
   - Pay-per-use pricing model and automatic scaling capabilities optimize cost-efficiency and resource utilization.
   - Leverages Lambda functions to perform tasks such as data validation, enrichment, and notification, seamlessly integrating with other AWS services within the pipeline architecture.

6. **Amazon Athena**:
   - Provides an interactive query service for analyzing data stored in Amazon S3 using standard SQL.
   - Leveraging Athena's distributed query processing engine, execute ad-hoc queries on data with minimal setup and management overhead.
   - Serverless architecture eliminates the need for infrastructure provisioning.
   - Integration with AWS Glue data catalog simplifies schema management and query optimization, enabling rapid insights generation from the centralized data lake.

## Dataset
The project utilizes a Kaggle dataset containing statistics on daily popular YouTube videos. Each file includes metadata such as video title, channel title, publication time, tags, views, likes, dislikes, description, comment count, and category ID.

