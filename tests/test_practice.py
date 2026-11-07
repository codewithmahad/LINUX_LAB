"""Exercise the scripts through Bash, including the inputs that exposed bugs."""

from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
BASICS = "practice/bash-scripting/01-basics"
LOOPS = "practice/bash-scripting/03-loops"
ARRAYS = "practice/bash-scripting/04-arrays"


class PracticeTests(unittest.TestCase):
    def run_script(self, path, input_text="", args=(), status=0):
        result = subprocess.run(
            ["bash", str(ROOT / path), *args],
            input=input_text,
            text=True,
            capture_output=True,
            cwd=ROOT,
            timeout=5,
        )
        self.assertEqual(result.returncode, status, result.stderr)
        if status == 0:
            self.assertEqual(result.stderr, "")
        return result

    def test_system_report_preserves_project_text(self):
        result = self.run_script(
            f"{BASICS}/01-system-report.sh", "  API service\\local  \n"
        )
        self.assertIn("Project   :   API service\\local  \n", result.stdout)
        self.assertIn(f"Directory : {ROOT}\n", result.stdout)

    def test_audit_prints_the_running_bash_version(self):
        version = subprocess.run(
            ["bash", "-c", 'printf "%s" "$BASH_VERSION"'],
            capture_output=True, text=True, check=True,
        ).stdout
        result = self.run_script(
            f"{BASICS}/02-session-audit.sh", "api service\\local\n  development  \n"
        )
        self.assertIn(f"Bash Version          : {version}\n", result.stdout)
        self.assertIn("Application Name      : api service\\local\n", result.stdout)
        self.assertIn("Environment Name      :   development  \n", result.stdout)

    def test_incomplete_input_fails(self):
        cases = (
            (f"{BASICS}/01-system-report.sh", ""),
            (f"{BASICS}/02-session-audit.sh", "app\n"),
            (f"{BASICS}/03-arithmetic.sh", "17\n"),
            (f"{BASICS}/04-percentage.sh", "50\n50\n"),
            (f"{LOOPS}/01-validated-marks.sh", ""),
            (f"{LOOPS}/02-number-analysis.sh", ""),
            (f"{LOOPS}/03-menu-calculator.sh", "1\n"),
            (f"{ARRAYS}/04-product-lookup.sh", ""),
            (f"{ARRAYS}/05-name-collection.sh", "one\ntwo\n"),
            ("learning/bash-scripting/03-input-and-output/input.sh", "one\n"),
        )
        for path, input_text in cases:
            with self.subTest(path=path):
                self.run_script(path, input_text, status=1)

    def test_arithmetic_including_leading_zeros_and_negatives(self):
        cases = (
            ("17\n5\n", (22, 12, 85, 3, 2)),
            ("008\n2\n", (10, 6, 16, 4, 0)),
            ("-08\n2\n", (-6, -10, -16, -4, 0)),
            ("0\n-5\n", (-5, 5, 0, 0, 0)),
        )
        labels = ("Sum", "Difference", "Product", "Quotient", "Remainder")
        for input_text, values in cases:
            with self.subTest(input=input_text):
                result = self.run_script(f"{BASICS}/03-arithmetic.sh", input_text)
                expected = "".join(
                    f"{label}: {value}\n" for label, value in zip(labels, values)
                )
                self.assertEqual(result.stdout, expected)

    def test_arithmetic_rejects_nonintegers_and_oversized_input(self):
        for value in ("abc", "1+2", "3.5", "", "+2", "1000000000"):
            with self.subTest(value=value):
                result = self.run_script(
                    f"{BASICS}/03-arithmetic.sh", f"{value}\n2\n", status=1
                )
                self.assertIn("Use integers", result.stderr)
                self.assertEqual(result.stdout, "")

    def test_division_by_zero_reports_failure(self):
        for zero in ("0", "000", "-0"):
            with self.subTest(zero=zero):
                result = self.run_script(
                    f"{BASICS}/03-arithmetic.sh", f"10\n{zero}\n", status=1
                )
                self.assertIn("Cannot divide by zero", result.stderr)
                self.assertNotIn("Quotient:", result.stdout)

    def test_percentage_boundaries_and_decimal_input(self):
        cases = (
            ("0\n0\n0\n", "Total: 0/300\nPercentage: 0%\nFAIL\n"),
            ("50\n50\n50\n", "Total: 150/300\nPercentage: 50%\nPASS\n"),
            ("100\n100\n100\n", "Total: 300/300\nPercentage: 100%\nPASS\n"),
            ("008\n080\n100\n", "Total: 188/300\nPercentage: 62%\nPASS\n"),
        )
        for input_text, output in cases:
            with self.subTest(input=input_text):
                self.assertEqual(
                    self.run_script(f"{BASICS}/04-percentage.sh", input_text).stdout,
                    output,
                )

    def test_percentage_rejects_invalid_marks(self):
        inputs = [f"{value}\n50\n50\n" for value in
                  ("200", "-1", "abc", "3.5", "", "1000")]
        inputs.extend(("50\n101\n50\n", "50\n50\n101\n"))
        for input_text in inputs:
            with self.subTest(input=input_text):
                result = self.run_script(
                    f"{BASICS}/04-percentage.sh", input_text, status=1
                )
                self.assertIn("0 to 100", result.stderr)
                self.assertEqual(result.stdout, "")

    def test_second_largest_is_distinct(self):
        cases = (
            ((), -7),
            (("5", "5", "4"), 4),
            (("5", "4", "5"), 4),
            (("-10", "-3", "-7", "-3"), -7),
            (("0", "0", "-1"), -1),
            (("-10", "-10", "-20"), -20),
            (("08", "7", "8"), 7),
            (("0", "-0", "-1"), -1),
            (("1", "2"), 1),
        )
        for args, value in cases:
            with self.subTest(args=args):
                result = self.run_script(
                    f"{ARRAYS}/03-second-largest.sh", args=args
                )
                self.assertEqual(
                    result.stdout, f"Second largest distinct number: {value}\n"
                )

    def test_second_largest_requires_two_distinct_values(self):
        for args in (("7",), ("7", "7"), ("0", "-0")):
            with self.subTest(args=args):
                result = self.run_script(
                    f"{ARRAYS}/03-second-largest.sh", args=args, status=1
                )
                self.assertIn("two distinct integers", result.stderr)
                self.assertEqual(result.stdout, "")

    def test_second_largest_rejects_invalid_arguments(self):
        for value in ("abc", "1+2", "3.5", "", "1000000000"):
            with self.subTest(value=value):
                result = self.run_script(
                    f"{ARRAYS}/03-second-largest.sh", args=("5", value), status=1
                )
                self.assertIn("Use integers", result.stderr)

    def test_validated_marks_retries_and_handles_decimal_digits(self):
        result = self.run_script(
            f"{LOOPS}/01-validated-marks.sh", "abc\n101\n080\n"
        )
        self.assertEqual(result.stdout.count("Invalid marks"), 2)
        self.assertTrue(result.stdout.endswith("PASS\n"))
        self.assertEqual(
            self.run_script(f"{LOOPS}/01-validated-marks.sh", "39\n").stdout,
            "FAIL\n",
        )
        self.assertEqual(
            self.run_script(f"{LOOPS}/01-validated-marks.sh", "40\n").stdout,
            "PASS\n",
        )

    def test_number_analysis(self):
        result = self.run_script(f"{LOOPS}/02-number-analysis.sh", "8\n")
        self.assertIn("Accepted numbers: 1 2 4 5 7 8 ", result.stdout)
        self.assertIn("Sum: 27\nCount: 6\nEven accepted numbers: 3\n", result.stdout)

    def test_calculator_recovers_from_invalid_input_and_zero_divisor(self):
        result = self.run_script(
            f"{LOOPS}/03-menu-calculator.sh",
            "4\n10\n0\n1\nhello\n2\n1\n008\n2\n5\n",
        )
        for message in ("Cannot divide by zero.", "Invalid integers.",
                        "Result: 10", "Goodbye."):
            self.assertIn(message, result.stdout)

    def test_array_operations_preserve_sparse_indices_and_spaces(self):
        result = self.run_script(f"{ARRAYS}/01-array-operations.sh")
        self.assertEqual(
            result.stdout,
            "Total: 3\nIndex 1: Large Notebook\nIndex 2: Marker\nIndex 3: Eraser\n",
        )

    def test_marks_statistics(self):
        result = self.run_script(f"{ARRAYS}/02-marks-statistics.sh")
        self.assertEqual(
            result.stdout,
            "Total: 290\nAverage: 58\nMaximum: 90\nMinimum: 33\nPassed: 3\nFailed: 2\n",
        )

    def test_product_lookup(self):
        for product, output in (("Book", "Price: Rs. 250\n"),
                                ("Pencil", "Product not found\n"),
                                ("", "Product not found\n")):
            with self.subTest(product=product):
                self.assertEqual(
                    self.run_script(
                        f"{ARRAYS}/04-product-lookup.sh", f"{product}\n"
                    ).stdout,
                    output,
                )

    def test_name_collection_preserves_whitespace_backslashes_and_options(self):
        names = "  Shaikh Mahad  \nC:\\Projects\\Linux\n-n\n"
        result = self.run_script(f"{ARRAYS}/05-name-collection.sh", names)
        self.assertEqual(result.stdout, "Total names: 3\n" + names)


if __name__ == "__main__":
    unittest.main()
