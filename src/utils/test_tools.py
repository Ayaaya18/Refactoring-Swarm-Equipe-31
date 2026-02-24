import subprocess

def run_tests(test_dir):
    result = subprocess.run(["pytest", test_dir, "--maxfail=1", "--disable-warnings", "--tb=short"], capture_output=True, text=True)
    success = result.returncode == 0
    return {"success": success, "output": result.stdout}
