from typing import Dict, List


class RecommendationEngine:

    def generate(self, metrics: Dict) -> List[str]:

        recommendations = []

        if metrics.get("storage_percent", 0) > 80:
            recommendations.append(
                "Storage usage is high. Consider cleanup or expansion."
            )

        if metrics.get("ram_percent", 0) > 80:
            recommendations.append("RAM utilization is high. Review running services.")

        unhealthy = metrics.get("total_containers", 0) - metrics.get(
            "healthy_containers", 0
        )

        if unhealthy > 0:
            recommendations.append(f"{unhealthy} container(s) require attention.")

        if not recommendations:
            recommendations.append("Infrastructure operating normally.")

        return recommendations
