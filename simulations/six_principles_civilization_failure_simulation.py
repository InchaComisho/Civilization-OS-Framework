#!/usr/bin/env python3
"""
Six Principles Civilization Failure Simulation
=============================================

A conceptual diagnostic model for evaluating civilization stability
through the Six Principles of Natural Law:

    1. Natural Law
    2. Harmony
    3. Circulation
    4. Structure
    5. Order
    6. Wa

This is not a predictive historical or economic model.
It is a transparent Civilization OS diagnostic tool.

Core idea:
    Civilization stability is not additive.
    If one principle collapses, the whole system becomes unstable.

    stability = natural_law * harmony * circulation * structure * order * wa

Author: Master / inchacomusho / InchaComisho
License: CC BY 4.0
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List
import csv


@dataclass
class CivilizationScenario:
    name: str
    description: str
    natural_law: float
    harmony: float
    circulation: float
    structure: float
    order: float
    wa: float


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def principle_values(scenario: CivilizationScenario) -> Dict[str, float]:
    data = asdict(scenario)
    return {
        "natural_law": clamp(float(data["natural_law"])),
        "harmony": clamp(float(data["harmony"])),
        "circulation": clamp(float(data["circulation"])),
        "structure": clamp(float(data["structure"])),
        "order": clamp(float(data["order"])),
        "wa": clamp(float(data["wa"])),
    }


def civilization_stability_score(scenario: CivilizationScenario) -> float:
    values = principle_values(scenario)
    score = 1.0
    for value in values.values():
        score *= value
    return round(score, 4)


def average_alignment_score(scenario: CivilizationScenario) -> float:
    values = principle_values(scenario)
    return round(sum(values.values()) / len(values), 4)


def collapse_risk_score(scenario: CivilizationScenario) -> float:
    stability = civilization_stability_score(scenario)
    # Collapse risk is high when multiplicative stability is low.
    return round(1.0 - stability, 4)


def weakest_principle(scenario: CivilizationScenario) -> str:
    values = principle_values(scenario)
    key = min(values, key=values.get)
    labels = {
        "natural_law": "Natural Law",
        "harmony": "Harmony",
        "circulation": "Circulation",
        "structure": "Structure",
        "order": "Order",
        "wa": "Wa",
    }
    return labels[key]


def classify_stability(score: float) -> str:
    if score >= 0.60:
        return "High stability"
    if score >= 0.30:
        return "Moderate stability"
    if score >= 0.10:
        return "Low stability"
    if score >= 0.03:
        return "Severe instability"
    return "Critical instability"


def default_scenarios() -> List[CivilizationScenario]:
    return [
        CivilizationScenario(
            name="Current civilization",
            description="Linear growth, extraction, consumption, short-term profit, weakened circulation, and low Wa.",
            natural_law=0.35,
            harmony=0.30,
            circulation=0.25,
            structure=0.55,
            order=0.60,
            wa=0.20,
        ),
        CivilizationScenario(
            name="Technocratic control civilization",
            description="High structure and order, but weak harmony, circulation, and Wa.",
            natural_law=0.45,
            harmony=0.35,
            circulation=0.35,
            structure=0.80,
            order=0.85,
            wa=0.25,
        ),
        CivilizationScenario(
            name="Green but fragmented civilization",
            description="Improves natural law and circulation partially, but lacks social harmony and integrated order.",
            natural_law=0.65,
            harmony=0.45,
            circulation=0.60,
            structure=0.55,
            order=0.45,
            wa=0.40,
        ),
        CivilizationScenario(
            name="Circular economy without Wa",
            description="Strong circulation reforms, but remains competitive, divided, and short-term oriented.",
            natural_law=0.65,
            harmony=0.45,
            circulation=0.75,
            structure=0.65,
            order=0.55,
            wa=0.30,
        ),
        CivilizationScenario(
            name="Six Principles Civilization OS",
            description="Civilization OS aligned with Natural Law, Harmony, Circulation, Structure, Order, and Wa.",
            natural_law=0.85,
            harmony=0.85,
            circulation=0.90,
            structure=0.85,
            order=0.80,
            wa=0.90,
        ),
    ]


def run_simulation(output_csv: str = "six_principles_civilization_failure_results.csv") -> List[Dict[str, str]]:
    results: List[Dict[str, str]] = []
    for scenario in default_scenarios():
        stability = civilization_stability_score(scenario)
        average = average_alignment_score(scenario)
        risk = collapse_risk_score(scenario)
        result = {
            "scenario": scenario.name,
            "description": scenario.description,
            "natural_law": f"{clamp(scenario.natural_law):.2f}",
            "harmony": f"{clamp(scenario.harmony):.2f}",
            "circulation": f"{clamp(scenario.circulation):.2f}",
            "structure": f"{clamp(scenario.structure):.2f}",
            "order": f"{clamp(scenario.order):.2f}",
            "wa": f"{clamp(scenario.wa):.2f}",
            "average_alignment_score": f"{average:.4f}",
            "civilization_stability_score": f"{stability:.4f}",
            "collapse_risk_score": f"{risk:.4f}",
            "weakest_principle": weakest_principle(scenario),
            "stability_class": classify_stability(stability),
        }
        results.append(result)

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)

    return results


def print_results(results: List[Dict[str, str]]) -> None:
    print("Six Principles Civilization Failure Simulation")
    print("=" * 88)
    for result in results:
        print(f"Scenario: {result['scenario']}")
        print(f"Description: {result['description']}")
        print(
            "Principles: "
            f"Natural Law={result['natural_law']}, "
            f"Harmony={result['harmony']}, "
            f"Circulation={result['circulation']}, "
            f"Structure={result['structure']}, "
            f"Order={result['order']}, "
            f"Wa={result['wa']}"
        )
        print(f"Average alignment score: {result['average_alignment_score']}")
        print(f"Civilization stability score: {result['civilization_stability_score']}")
        print(f"Collapse risk score: {result['collapse_risk_score']}")
        print(f"Weakest principle: {result['weakest_principle']}")
        print(f"Stability class: {result['stability_class']}")
        print("-" * 88)


if __name__ == "__main__":
    simulation_results = run_simulation()
    print_results(simulation_results)
