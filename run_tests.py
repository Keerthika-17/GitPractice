
import unittest

with open("test-results.txt", "w", encoding="utf-8") as report:
    suite = unittest.defaultTestLoader.loadTestsFromName("test_hello")
    runner = unittest.TextTestRunner(stream=report, verbosity=2)
    result = runner.run(suite)

if not result.wasSuccessful():
    raise SystemExit(1)
