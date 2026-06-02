from app.intelligence.health_scoring import HealthScoring
from app.intelligence.recommendation_engine import RecommendationEngine
from app.intelligence.report_generator import ReportGenerator


def main():

    metrics = {
        "storage_percent": 38,
        "ram_percent": 27,
        "total_containers": 4,
        "healthy_containers": 4,
        "services_ok": True,
    }

    health = HealthScoring().calculate(metrics)

    recommendations = RecommendationEngine().generate(metrics)

    report = ReportGenerator().generate(health, recommendations)

    print(report)


if __name__ == "__main__":
    main()
