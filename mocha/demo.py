def demo() -> None:
    """
    Run demo. Jetfuel must be initialized first.
    """
    from .profiler import Profiler
    from concurrent.futures import ThreadPoolExecutor
    import random
    import time

    tasks = [
        "Workspace Creation (New Customer)",
        "Dataset Join - 259 GB",
        "ETL Snowflake -> Amazon Glacier",
        "CI/CD full build",
        "Terraform Prod Deployment",
    ]

    demo_running = True

    def run_task(task) -> None:
        while demo_running:
            with Profiler(task):
                time.sleep(random.random())

    try:
        with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
            for task in tasks:
                executor.submit(run_task, task=task)
    except:
        # Catch keyboard interrupt (or any other exception), then stop demo
        demo_running = False
