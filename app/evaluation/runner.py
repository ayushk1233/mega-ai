import json

from app.evaluation.evaluator import Evaluator


DATASET_PATH = (
    "app/evaluation/benchmark_dataset.json"
)


def run_evaluations():

    with open(DATASET_PATH, "r") as file:
        benchmarks = json.load(file)

    evaluator = Evaluator()

    results = []

    for benchmark in benchmarks:

        result = evaluator.evaluate(
            benchmark
        )

        results.append(result)

    return results


if __name__ == "__main__":

    results = run_evaluations()

    for result in results:

        print(result)

    with open(
        "app/evaluation/reports/eval_report.json",
        "w"
    ) as report_file:

        json.dump(
            results,
            report_file,
            indent=2
        )

    print(
        "\nEvaluation report saved."
    )