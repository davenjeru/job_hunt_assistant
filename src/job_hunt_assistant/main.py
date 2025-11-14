#!/usr/bin/env python
import sys
import warnings

from job_hunt_assistant.crew import JobHuntAssistant
from job_hunt_assistant.usajobs_api import fetch_usajobs

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """

    jobs = fetch_usajobs("business analyst")
    if len(jobs) == 0:
        print("No job posts found.")
        return

    first_job = jobs[0]['MatchedObjectDescriptor']
    job_description = first_job['UserArea']['Details']['JobSummary']

    inputs = {
        "job_description": job_description,
    }

    try:
        JobHuntAssistant().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()