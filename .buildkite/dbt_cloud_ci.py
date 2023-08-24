# python/dbt_cloud.py

from urllib.request import Request, urlopen
import argparse
import json
import time
import os

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--steps", type=str, nargs="+")
args = parser.parse_args()

# fmt: off 
#TODO: Refactor environment variables
api_base        = os.getenv("DBT_CLOUD_URL", "https://au.dbt.com")
job_cause       = os.getenv("DBT_CLOUD_JOB_CAUSE", "github_actions_pull_request")
git_branch      = os.getenv("DBT_CLOUD_JOB_BRANCH", None)
schema_override = os.getenv("DBT_CLOUD_JOB_SCHEMA_OVERRIDE", None)
api_token       = "dbtc_DGsfFAw-Bh4PYkSQ6XYbhpL2aYHLH3hchiJwahmxJVixcLxd14"
account_id      = "20"
project_id      = "3518"
job_id          = "3605"

job_config = f"""
Request configuration:
    api_base: {api_base}
    job_cause: {job_cause}
    git_branch: {git_branch}
    schema_override: {schema_override}
    account_id: {account_id}
    project_id: {project_id}
    job_id: {job_id}
"""
# fmt: on

req_auth_header = {
    "Authorization": f"Token {api_token}",
    "Content-Type": "application/json",
}
req_job_url = f"{api_base}/api/v2/accounts/{account_id}/jobs/{job_id}/run/"
run_status_map = {
    1: "Queued",
    2: "Starting",
    3: "Running",
    10: "Success",
    20: "Error",
    30: "Cancelled",
}


def run_dbt_cloud_job(
    url,
    headers,
    cause,
    branch=None,
    schema_override=None,
    steps=None,
) -> int:
    """Trigger a dbt Cloud job and returns the job id."""

    req_payload = {"cause": cause}
    if branch:
        req_payload["git_branch"] = branch.replace("refs/heads/", "")
    if schema_override:
        req_payload["schema_override"] = schema_override.replace("-", "_")
    if steps:
        req_payload["steps_override"] = steps
    print(f"Triggering job:\n    url: {url}\n    payload: {req_payload}\n")

    data = json.dumps(req_payload).encode()

    request = Request(method="POST", data=data, headers=headers, url=url)
    with urlopen(request) as req:
        response = req.read().decode("utf-8")
        run_job_resp = json.loads(response)

    return run_job_resp["data"]["id"]


def get_run_status(url, headers) -> str:
    """Get the status of a running dbt Cloud job."""

    request = Request(headers=headers, url=url)

    with urlopen(request) as req:
        response = req.read().decode("utf-8")
        req_status_resp = json.loads(response)

    run_status_code = req_status_resp["data"]["status"]
    run_status = run_status_map[run_status_code]

    return run_status


def main():
    print(job_config)

    job_steps = args.steps
    run_id: int = None

    try:
        run_id = run_dbt_cloud_job(
            url=req_job_url,
            headers=req_auth_header,
            cause=job_cause,
            branch=git_branch,
            schema_override=schema_override,
            steps=job_steps,
        )
    except Exception as e:
        print(f"ERROR! - Could not trigger dbt Cloud job:\n{e}")
        raise

    req_status_url = f"{api_base}/api/v2/accounts/{account_id}/runs/{run_id}/"
    run_status_link = (
        f"{api_base}/#/accounts/{account_id}/projects/{project_id}/runs/{run_id}/"
    )

    time.sleep(30)

    while True:
        run_status = get_run_status(req_status_url, req_auth_header)
        print(f"Run status -> {run_status}")

        if run_status in ["Error", "Cancelled"]:
            raise Exception(f"Run failed or cancelled. See why at {run_status_link}")

        if run_status == "Success":
            print(f"Job completed successfully! See details at {run_status_link}")
            return

        time.sleep(10)


if __name__ == "__main__":
    main()