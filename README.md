# finetune_jobs_api

## Setup Instructions
(note: Create the finetune job using UI before running the scripts - https://studio.tune.app/finetuning)

### Run Functinal Tests 
- Contains both positive and negative test cases
1. Run run_test.bat - it runs the scripts and generates a log report in local
2. Navigate to location (C:\Users\YASWITA\finetune_jobs_api) to open the report 

Sample Report = https://github.com/Yaswita/finetune_jobs_api/blob/main/finetune_report.html, download raw file and open it 
              https://docs.google.com/document/d/1waiR8_y2ICD9wXvDI5bW5BEHtbFrhJ5qiSqnbhx6T6U/edit?usp=sharing

### Run Performance Tests
- Contains performance test case using locusts
1. Run run_performance_test.bat in performance folder under fine_tune_api.
2. It will generate a link - http://localhost:8089, open it and give start 
3. You can navigate to charts tab to see visual representation of the testing
4. Can download the data required from download data tab



