from app.intelligence.health_scoring import HealthScoring


def main():
    metrics = {
        "storage_percent": 38,
        "ram_percent": 27,
        "total_containers": 4,
        "healthy_containers": 4,
        "services_ok": True,
    }

    scorer = HealthScoring()

    result = scorer.calculate(metrics)

    print(result)


if __name__ == "__main__":
    main()
