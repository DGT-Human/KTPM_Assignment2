import os
import subprocess
import time

# Đường dẫn tới thư mục chứa các tập lệnh Selenium
TEST_FOLDER = "./tests"

# File kết quả
RESULTS_FILE = "batch_execution_results.txt"

def run_batch_tests():
    test_results = []
    start_time = time.time()

    # Kiểm tra nếu thư mục tồn tại
    if not os.path.exists(TEST_FOLDER):
        print(f"Error: Thư mục {TEST_FOLDER} không tồn tại.")
        return

    for filename in os.listdir(TEST_FOLDER):
        if filename.endswith(".py"):
            filepath = os.path.join(TEST_FOLDER, filename)
            print(f"Running: {filename}")

            # Chạy tập lệnh và bắt kết quả
            try:
                result = subprocess.run(
                    ["python", filepath],
                    capture_output=True, text=True
                )
                status = "Pass" if result.returncode == 0 else "Fail"
                error_log = result.stderr if result.stderr else "No Errors"

                # Ghi kết quả của từng test
                test_results.append({
                    "name": filename,
                    "status": status,
                    "error_log": error_log
                })
            except Exception as e:
                print(f"Error when running {filename}: {e}")
                test_results.append({
                    "name": filename,
                    "status": "Fail",
                    "error_log": str(e)
                })

    end_time = time.time()

    # Ghi tất cả kết quả vào file
    with open(RESULTS_FILE, "w") as f:
        total_time = end_time - start_time
        f.write(f"Batch Execution Summary - Total Time: {total_time:.2f} seconds\n\n")
        for result in test_results:
            f.write(f"Test: {result['name']} | Status: {result['status']}\n")
            if result["status"] == "Fail":
                f.write(f"Error Log:\n{result['error_log']}\n")
            f.write("\n")

    # In kết quả ra màn hình
    print("Batch Execution Results:")
    for result in test_results:
        print(f"Test: {result['name']} | Status: {result['status']}")
        if result["status"] == "Fail":
            print(f"Error Log:\n{result['error_log']}\n")

if __name__ == "__main__":
    run_batch_tests()