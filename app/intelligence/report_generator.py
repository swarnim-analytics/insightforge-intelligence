"""
Infrastructure Intelligence Report Generator
"""

from typing import Dict, List


class ReportGenerator:

    def generate(self, health: Dict, recommendations: List[str]) -> str:

        report = []

        report.append("🖥 InsightForge Infrastructure Intelligence")

        report.append("")

        report.append(f"Health Score: {health['health_score']}/100")

        report.append(f"Status: {health['status']}")

        report.append("")

        report.append("Recommendations:")

        for item in recommendations:
            report.append(f"• {item}")

        return "\n".join(report)
