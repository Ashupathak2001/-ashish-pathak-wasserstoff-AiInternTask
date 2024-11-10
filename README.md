Domain-Specific PDF Summarization & Keyword Extraction Pipeline
This project is designed to create a dynamic, efficient pipeline that ingests and processes PDF documents from a specified folder, generates domain-specific summaries and keywords, and stores them in MongoDB. This solution is built to handle a variety of document lengths, efficiently process data with concurrency, and prioritize innovative approaches for PDF parsing, summarization, and keyword extraction.

Features
PDF Ingestion: Processes all PDF files in a designated folder, handling various document types and lengths.
Concurrent Processing: Uses concurrency for faster processing and resource management.
Summarization & Keyword Extraction: Abstractive summarization and domain-specific keyword extraction.
JSON-based MongoDB Storage: Saves summaries and keywords in a structured JSON format in MongoDB.
Error Logging: Captures errors during processing to avoid interruptions in the pipeline.
Table of Contents
Setup Instructions
System Requirements
Usage Guide
Code Structure
Performance Reports
Contributing
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/Devian158/AI-Internship-Task.git
cd AI-Internship-Task
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure MongoDB connection in config.py with your database credentials.

System Requirements
Python: Version 3.8+
MongoDB: Version 4.4+
Dependencies: Listed in requirements.txt
Usage Guide
Provide PDF Folder Path: In main.py, specify the folder path containing the PDFs.
Run the Pipeline: Execute main.py to start the pipeline.
bash
Copy code
python main.py
The pipeline will:
Ingest each PDF.
Store metadata in MongoDB.
Summarize content and extract keywords.
Update MongoDB with the generated summaries and keywords.
Code Structure
main.py: Coordinates the pipeline, calling all modules.
parsing.py: Manages PDF ingestion, parsing, and MongoDB metadata storage.
summarization.py: Implements abstractive summarization based on document length.
keyword.py: Extracts non-generic, domain-specific keywords.
docUpdation.py: Updates MongoDB with generated summaries and keywords.
Performance Reports
Concurrency: This pipeline processes documents in parallel, optimizing speed and resource usage.
Metrics: Logs time taken per document and overall speed. Detailed metrics can be found in the performance.log.
Contributing
Contributions are welcome! Please adhere to the coding standards outlined in the contribution guide.



