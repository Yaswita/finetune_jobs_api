#!/bin/bash
# Script to run all tests
#pytest tests/functionl/positive_tc/test_list_finetune_job.py
#pytest tests/functionl/positive_tc/test_get_finetune_job.py
#pytest tests/functionl/positive_tc/test_terminate_finetune_job.py
#pytest tests/functionl/positive_tc/test_delete_finetune_job.py

locust -f tests/performance/test_performance.py