"""
Infrastructure Health Scoring Engine
"""

from typing import Dict


class HealthScoring:
    """
    Generates a health score from 0-100.
    """

    def calculate(self, metrics: Dict) -> Dict:
        score = 100

        # Storage
        storage_used = metrics.get("storage_percent", 0)

        if storage_used > 90:
            score -= 30
        elif storage_used > 80:
            score -= 20
        elif storage_used > 70:
            score -= 10

        # RAM
        ram_used = metrics.get("ram_percent", 0)

        if ram_used > 90:
            score -= 25
        elif ram_used > 80:
            score -= 15
        elif ram_used > 70:
            score -= 10

        # Containers
        total_containers = metrics.get("total_containers", 0)
        healthy_containers = metrics.get("healthy_containers", 0)

        unhealthy = total_containers - healthy_containers

        score -= unhealthy * 10

        # Service Availability
        services_ok = metrics.get("services_ok", True)

        if not services_ok:
            score -= 20

        score = max(0, min(score, 100))

        return {"health_score": score, "status": self._status(score)}

    def _status(self, score: int) -> str:
        if score >= 90:
            return "Excellent"

        if score >= 75:
            return "Healthy"

        if score >= 60:
            return "Warning"

        return "Critical"
